from django.urls import path
from .apis import PayablesCreateAPIView, TransactionCreateAPIView

urlpatterns = [
    path('payable/', PayablesCreateAPIView.as_view()),
    path('transaction/', TransactionCreateAPIView.as_view()),
]
