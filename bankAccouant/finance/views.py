from django.shortcuts import render
from finance.models import Withdraw
from finance.forms import WithdrawModelForm
from finance.forms import DepositeModelForm
from django.http import HttpResponse


# Create your views here.
def moneyWithdraw(request):
    form = WithdrawModelForm
    Withdrawform = {'form':form}
    if request.method=='POST':
        form = WithdrawModelForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'finance/money-Withdraw.html',Withdrawform)

def moneyDeposite(request):
    form = DepositeModelForm
    Depositeform = {'form':form}
    if request.method=='POST':
        form = DepositeModelForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'finance/money-Deposit.html',Depositeform)
