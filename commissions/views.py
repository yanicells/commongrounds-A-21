from django.shortcuts import render

from .models import Commission


def request_list(request):
    commissions = Commission.objects.all()
    ctx = {
        'commissions': commissions
    }
    return render(request, 'commissions/request_list.html', ctx)


def request_detail(request, pk):
    commission = Commission.objects.get(pk=pk)
    ctx = {
        'commission': commission
    }
    return render(request, 'commissions/request_detail.html', ctx)
