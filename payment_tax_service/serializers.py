from rest_framework import serializers
from .models import Payables, StatusPayable, Transactions


class PayableListSerializer(serializers.ModelSerializer):
    type_service = serializers.StringRelatedField(many=False)

    class Meta:
        model = Payables
        depth = 1
        fields = ['type_service', 'importe', 'due_date', 'bar_code']


class PayableCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payables
        exclude = ['status']

    def create(self, validated_data):
        # TODO Pending status
        validated_data['status'] = StatusPayable.objects.filter(name__icontains='Pending').first()
        obj = self.Meta.model.objects.create(**validated_data)
        obj.save()
        return obj


class TransactionsSerializer(serializers.ModelSerializer):
    number_card = serializers.CharField(max_length=30, required=False)

    class Meta:
        model = Transactions
        fields = '__all__'

    def create(self, validated_data: dict):
        if validated_data.get('method_transaction').pk < 3 and not validated_data.get('number_card'):
            raise serializers.ValidationError({'number_card': 'The field is required!'})
        obj = self.Meta.model.objects.create(**validated_data)
        obj.save()
        # TODO Paid status
        obj.payable.status = StatusPayable.objects.filter(name__icontains='Paid').first()
        obj.payable.save()
        return obj
