from django.urls import path

from accounts.views import addAccount;
from accounts.views import accountReport;
from accounts.views import addVendor;
from accounts.views import updateAccountHolder
from accounts.views import deleteAccountHolder

urlpatterns = [

    path('newadm/', addAccount),
    path('admreport/', accountReport),
    path('newvendor/', addVendor),
    path('update/<int:id>', updateAccountHolder),
    path('delete/<int:id>', deleteAccountHolder),

]
