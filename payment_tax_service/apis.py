import datetime
from .models import Payables, Transactions, StatusPayable
from .serializers import PayableListSerializer, PayableCreateSerializer, TransactionsSerializer
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.serializers import ValidationError

# TODO Pending status
pending_status = StatusPayable.objects.filter(name__icontains='Pending').first()


class PayablesListCreateAPI(ListCreateAPIView):
    """
    Class to list and create a pending payable
    """
    model = Payables
    queryset = Payables.objects.filter(status=pending_status)
    serializer_class = PayableCreateSerializer

    def list(self, request):
        queryset = self.get_queryset()
        filtros = {}
        request_get = request.GET
        if request_get.get('type_service'):
            filtros['type_service_id'] = request_get.get('type_service')
        if request_get.get('due_date'):
            date_string = request_get.get('due_date')
            format = "%Y-%m-%d"
            try:
                datetime.datetime.strptime(date_string, format)
                filtros['due_date'] = request_get.get('due_date')
            except ValueError:
                raise ValidationError({
                    'due_date': 'Date format not match. The expected format is {format}'.format(
                        format=format.replace('%', '')
                    )
                })

        if request_get.get('bar_code'):
            filtros['bar_code'] = request_get.get('bar_code')

        serializer = PayableListSerializer(queryset.filter(**filtros), many=True)
        return Response(serializer.data)


class TransactionCreateAPIView(CreateAPIView):
    """
    Class pay the payable of the service
    """
    model = Transactions
    serializer_class = TransactionsSerializer
