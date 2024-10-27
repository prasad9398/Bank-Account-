from django import forms
from accounts.models import AccountHolder

class AccountHolderModelForm(forms.ModelForm):
    class Meta:
        model = AccountHolder
        fields = '__all__'


class VendorForm(forms.Form):
    name = forms.CharField(max_length=1000)
    accountno = forms.IntegerField()
    contact = forms.CharField(max_length=1000)
    address = forms.CharField(max_length=1000)
