from django import forms
from finance.models import Withdraw
from finance.models import Deposite

class WithdrawModelForm(forms.ModelForm):
    class Meta:
        model = Withdraw
        fields = '__all__'


class DepositeModelForm(forms.ModelForm):
    class Meta:
        model = Deposite
        fields = '__all__'
