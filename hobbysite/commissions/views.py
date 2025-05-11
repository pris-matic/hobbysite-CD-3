from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Case, When, Value, IntegerField
from django.utils import timezone
from .models import Commission, Job, JobApplication
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
            return redirect('commission:comission_detail', id=commission.id)
        
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
        return redirect('commission:commission_detail', id=commission.id)
    ctx = {'commission': Commission.objects.get(id=id)}
    return render(request, 'commissions/commissionDetail.html', ctx)
