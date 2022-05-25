import uuid
from django.db import models


# Create your models here.
class ServiceType(models.Model):
    """
    Class to save type of services
     Example:
         - Luz
         - Agua
         - Gas
    """
    name = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return self.name


class StatusPayable(models.Model):
    """
    Class to save status of payable
     Example:
         - Paid
         - Pending
         - Rejected
    """
    name = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return self.name


class Payables(models.Model):
    """
    Class to save payable record
    """
    bar_code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.ForeignKey('payment_tax_service.StatusPayable', on_delete=models.CASCADE)
    type_service = models.ForeignKey('payment_tax_service.ServiceType', on_delete=models.CASCADE)
    description = models.TextField()
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)


class MethodTransaction(models.Model):
    """
    Class to save the methods of payment transaction
     Example:
         - debit_card
         - credit_card
         - cash
    """
    name = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return self.name


class Transactions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    method_transaction = models.ForeignKey('payment_tax_service.MethodTransaction', on_delete=models.CASCADE)
    payable = models.ForeignKey('payment_tax_service.Payables', on_delete=models.CASCADE)
    number_card = models.CharField(max_length=30, editable=False, null=True, blank=True)
    importe_pago = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    pay_date = models.DateField()
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
