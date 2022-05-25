from .models import Payables
from .serializers import PayableSerializer
from rest_framework.generics import CreateAPIView


class PayablesCreateAPIView(CreateAPIView):
    """
    Class para crear boletas de cobro de pago de servicio
    """
    model = Payables
    serializer_class = PayableSerializer
