from django.contrib import admin
from accounts.models import AccountHolder


class AccountAdmin(admin.ModelAdmin):
    list_display=['id','name','accountno','contact','address']


# Register your models here.
admin.site.register(AccountHolder,AccountAdmin)
