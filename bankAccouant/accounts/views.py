from django.shortcuts import render
from accounts.models import AccountHolder
from accounts.forms import AccountHolderModelForm
from accounts.forms import VendorForm
from django.views.generic import View, UpdateView,DeleteView
from django.http import HttpResponse
# Create your views here.


#function based views
def homepage(request):
    return render(request, 'index.html')

def addAccount(request):
    form = AccountHolderModelForm
    AccountHolderform = {'form':form}
    if request.method=='POST':
        form = AccountHolderModelForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'accounts/add-accounts.html',AccountHolderform);

def updateAccountHolder(request, id):
    a = AccountHolder.objects.get(id=id)
    form = AccountHolderModelForm(instance=a)
    dict = {'form':form}
    if request.method=='POST':
        form =  AccountHolderModelForm(request.POST, instance=a)
        if form.is_valid():
            form.save()
        return accountReport(request)

    return render(request,'accounts/update-accounts.html',dict)


def deleteAccountHolder(request,id):
    a = AccountHolder.objects.get(id=id)# select * from admission_student where id=idvalue
    a.delete()
    return accountsReport(request)

    return render(request,'accounts/delete-accounts.html',dict)

def addVendor(request):
    form = VendorForm
    vform = {'form':form}
    if request.method=='POST':
        form =  VendorForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            a = form.cleaned_data['accountno']
            c = form.cleaned_data['contact']
            a = form.cleaned_data['address']
            dict = {"name":n,"accountno":a,"contact":c,"address":a}
        return render(request,'index.html',dict)

    return render(request,'admission/add-accounts.html',vform)

def accountReport(request):
    #get all record from accounts_AccountHolder table
    result = AccountHolder.objects.all(); #this is equal to select * from AccountHolder query
    #Create a dictionary and store above result init
    AccountHolders = {'allAccountHolders':result}
    return render(request,'accounts/accounts-report.html', AccountHolders);
