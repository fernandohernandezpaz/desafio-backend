import datetime
from django.db.models import Count, Sum
from .models import Payables, Transactions
from .serializers import (PayableListSerializer, PayableCreateSerializer,
                          TransactionListSerializer, TransactionsCreateSerializer, )
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.serializers import ValidationError


class PayablesListCreateAPI(ListCreateAPIView):
    """
    Class to list and create a pending payable
    """
    model = Payables
    # TODO Pending status
    queryset = Payables.objects.filter(status__name__icontains='Pending')
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


class TransactionListCreate(ListCreateAPIView):
    """
    Class pay the payable of the service
    """
    model = Transactions
    serializer_class = TransactionsCreateSerializer

    def list(self, request):
        filtros = {}
        request_get = request.GET
        if request_get.get('pay_date'):
            dates_string = request_get.getlist('pay_date')
            for date_string in dates_string:
                format = "%Y-%m-%d"
                try:
                    datetime.datetime.strptime(date_string, format)
                except ValueError:
                    raise ValidationError({
                        'pay_date': 'Date format not match. The expected format is {format}'.format(
                            format=format.replace('%', '')
                        )
                    })

            filtros['pay_date__range'] = sorted(request_get.getlist('pay_date'))
        queryset = self.model.objects.filter(**filtros) \
            .order_by('-pay_date') \
            .values('pay_date') \
            .annotate(
                quantity_transactions=Count('pay_date'),
                total=Sum('importe_pago')
            )
        serializer = TransactionListSerializer(queryset, many=True)
        return Response(serializer.data)
