from django.urls import path
from .apis import (PayablesListCreateAPI, TransactionListCreate)

urlpatterns = [
    path('payable/', PayablesListCreateAPI.as_view()),
    path('transaction/', TransactionListCreate.as_view()),
]
