from django.urls import path

from finance.views import moneyWithdraw;
from finance.views import moneyDeposite;

urlpatterns = [

    path('moneywith/', moneyWithdraw),
    path('moneydep/', moneyDeposite),
]
