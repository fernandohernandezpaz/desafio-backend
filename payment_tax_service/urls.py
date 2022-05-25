from django.urls import path
from .apis import (PayablesListCreateAPI, TransactionListCreate)

urlpatterns = [
    path('payable/', PayablesListCreateAPI.as_view(), name='payable-api'),
    path('transaction/', TransactionListCreate.as_view(), name='transaction-api'),
]
