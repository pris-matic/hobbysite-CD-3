from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Case, When, Value, IntegerField
from django.utils import timezone
from .models import Commission, Job, JobApplication
from .forms import CommissionForm, JobFormSet, JobApplicationForm
from user_management.models import Profile

def commissions_list(request):

    status_order = Case(
        When(status='Open', then=Value(0)),
        When(status='Full', then=Value(1)),
        When(status='Completed', then=Value(2)),
        When(status='Discontinued', then=Value(3)),
        output_field=IntegerField()
    )
    commissions = Commission.objects.annotate(
        status_order=status_order
    ).order_by('status_order', '-created_on')

    ctx = {
        'commissions': commissions
    }

    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user) 
        ctx['user_commissions'] = Commission.objects.filter(author=profile)
        ctx['applied_commissions'] = Commission.objects.filter(
            jobs__jobapplication__applicant=profile
        ).distinct()

    return render(request, 'commissions/commissionsList.html', ctx)

def commission_detail(request, id):
    commission = get_object_or_404(Commission, id=id)
    profile = None
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
    
    if request.method == 'POST' and profile:
        if profile == commission.author:
            app_id = request.POST.get('application_id')
            action = request.POST.get('action')
            application = get_object_or_404(
                JobApplication, id=app_id, job__commission=commission
            )
            if action == 'accept':
                application.status = 'Accepted'
                application.save()
            elif action == 'reject':
                application.status = 'Rejected'
                application.save()
            return redirect('commissions:commission_detail', id=commission.id)
        
    job_id = request.POST.get('job_id')
    if job_id:
        job = get_object_or_404(Job, id=job_id)
        exists = JobApplication.objects.filter(job=job, applicant=profile).exists()
        if not exists:
            JobApplication.objects.create(
                job=job,
                applicant=profile,
                status='Pending',
                applied_on=timezone.now(),
            )
        return redirect('commissions:commission_detail', id=commission.id)

    jobs = commission.jobs.all()
    manpower_info = []
    total_required = 0
    total_open = 0

    for job in jobs:
        accepted_count = job.jobapplication_set.filter(status='Accepted').count()
        open_slots = job.manpower_required - accepted_count
        already_applied = profile and job.jobapplication_set.filter(applicant=profile).exists()
        can_apply = open_slots > 0 and not already_applied
        manpower_info.append((job, open_slots, can_apply))

        total_required += job.manpower_required
        total_open += open_slots

    is_owner = profile == commission.author if profile else False

    ctx = {
        'commission': commission,
        'manpower_info': manpower_info,
        'total_required': total_required,
        'total_open': total_open,
        # 'application_form': JobApplicationForm(), # fix this later
        'is_owner': is_owner,
    }

    if is_owner:
        applications = JobApplication.objects.filter(
            job__commission=commission
        ).select_related('job', 'applicant')
        ctx['applications'] = applications

    return render(request, 'commissions/commissionDetail.html', ctx)

@login_required
def commission_create(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = CommissionForm(request.POST)
        formset = JobFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            commission = form.save(commit=False)
            commission.author = profile
            commission.created_on = timezone.now()
            commission.updated_on = timezone.now()
            commission.save()

            for job in formset.save(commit=False):
                job.commission = commission
                job.save()
            
            return redirect('commissions:commissions_list')
    else:
        form = CommissionForm()
        formset = JobFormSet()

    return render(request, 'commissions/commissionCreate.html', {
        'form': form,
        'formset': formset,
    })

@login_required
def commission_update(request, id):
    profile = get_object_or_404(Profile, user=request.user)
    commission = get_object_or_404(Commission, id=id, author=profile)

    if request.method == 'POST':
        form = CommissionForm(request.POST, instance=commission)
        formset = JobFormSet(request.POST, instance=commission)
        if form.is_valid() and formset.is_valid():
            commission = form.save(commit=False)
            commission.updated_on = timezone.now()
            commission.save()
            formset.save
            
            all_full = all(job.status == 'Full' for job in commission.jobs.all())
            if all_full and commission.status != 'Full':
                commission.status = 'Full'
                commission.save()

            return redirect('commissions:commissions_list')
    else:
        form = CommissionForm(instance=commission)
        formset = JobFormSet(instance=commission)
    
    return render(request, 'commissions/commissionCreate.html', {
        'form': form,
        'formset': formset,
    })

