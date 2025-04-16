from django.shortcuts import render
from .models import Commission

# Create your views here.

def commissions_list(request):
    commissions = Commission.objects.all()
    ctx = {'commissions': commissions}
    return render(request, 'commissions/commissionsList.html', ctx)

def commission_detail(request, id):
    ctx = {'commission': Commission.objects.get(id=id)}
    return render(request, 'commissions/commissionDetail.html', ctx)
