from django.test import TestCase
from .models import *
from django.urls import reverse
from rest_framework import status as httpStatus


# Create your tests here.
class StatusPayableTestCase(TestCase):
    model = StatusPayable

    def setUp(self):
        self.model.objects.create(name="Paid")
        self.model.objects.create(name="Pending")

    def test_paid_status_exists(self):
        """Check if status of payable exists"""
        status = self.model.objects.filter(name="Paid").first()
        self.assertIsNotNone(status, msg='The Paid status exists')

    def test_pending_status_exists(self):
        """Check if status of payable exists"""
        status = self.model.objects.filter(name="Pending").first()
        self.assertIsNotNone(status, msg='The Pending status exists')


class ServiceTypeTestCase(TestCase):
    model = ServiceType

    def setUp(self):
        self.model.objects.create(name="Luz")
        self.model.objects.create(name="Gas")
        self.model.objects.create(name="Agua")

    def test_luz_service_type_exists(self):
        """Check if status of payable exists"""
        status = self.model.objects.filter(name="Luz").first()
        self.assertIsNotNone(status, msg='The Luz service type exists')


class MethodTransactionTestCase(TestCase):
    model = MethodTransaction

    def setUp(self):
        self.model.objects.create(name="credit_card")
        self.model.objects.create(name="debit_card")
        self.model.objects.create(name="cash")

    def test_paid_status_exists(self):
        """Check if method of transaction exists"""
        status = self.model.objects.filter(name="credit_card").first()
        self.assertIsNotNone(status, msg='The credit_card method exists')

    def test_methodtransaction_exists_records(self):
        methods_count = self.model.objects.count()
        self.assertEqual(methods_count, 3, msg='Exists methods of transaction in db')


class PayableTestCase(TestCase):
    model = Payables
    data_record = {
        'description': 'Disnorte Dissur',
        'importe': 100.2,
        'due_date': '2022-05-25',
        'status': 1,
        'type_service': 1,
    }

    def setUp(self):
        StatusPayable.objects.create(name="Pending")
        ServiceType.objects.create(name="Luz")

    def test_api_create_payable(self):
        """Testing if the api create a payable"""
        url = reverse('payable-api')
        response = self.client.post(url, self.data_record, format='json')
        self.assertEqual(response.status_code, httpStatus.HTTP_201_CREATED)
        self.assertEqual(self.model.objects.count(), 1)
        self.assertEqual(self.model.objects.get().description, 'Disnorte Dissur')

