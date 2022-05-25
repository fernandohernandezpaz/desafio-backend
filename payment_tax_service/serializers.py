from rest_framework import serializers
from .models import Payables, StatusPayable


class PayableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payables
        extra_kwargs = {'status': {'required': False}}
        fields = [
            'status', 'type_service', 'description', 'importe',
            'due_date'
        ]

    def create(self, validated_data):
        # TODO Pending status
        validated_data['status'] = StatusPayable.objects.filter(name__icontains='Pending').first()
        obj = self.Meta.model.objects.create(**validated_data)
        obj.save()
        return obj
