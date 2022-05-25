from django.urls import path
from .apis import (PayablesListCreateAPI, TransactionCreateAPIView)

urlpatterns = [
    path('payable/', PayablesListCreateAPI.as_view()),
    path('transaction/', TransactionCreateAPIView.as_view()),
]
