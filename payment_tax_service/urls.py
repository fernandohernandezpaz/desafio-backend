from django.urls import path, include
from .apis import PayablesCreateAPIView

urlpatterns = [
    path('payable/', PayablesCreateAPIView.as_view())
]
