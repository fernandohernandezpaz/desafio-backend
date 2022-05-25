from .models import Payables, Transactions
from .serializers import PayableSerializer, TransactionsSerializer
from rest_framework.generics import CreateAPIView


class PayablesCreateAPIView(CreateAPIView):
    """
    Class to create a payable for any service
    """
    model = Payables
    serializer_class = PayableSerializer


class TransactionCreateAPIView(CreateAPIView):
    """
    Class pay the payable of the service
    """
    model = Transactions
    serializer_class = TransactionsSerializer
