from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(MethodTransaction)
class MethodTransactionAdmin(admin.ModelAdmin):
    pass


@admin.register(StatusPayable)
class StatusPayableAdmin(admin.ModelAdmin):
    pass


@admin.register(Payables)
class PayablesAdmin(admin.ModelAdmin):
    pass


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    pass
