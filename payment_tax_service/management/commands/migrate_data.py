from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help: str = 'Command to migrate json into a sqlite db'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Init migration'))
        call_command('migrate')
        self.stdout.write(self.style.SUCCESS('Migration ended!'))
        self.stdout.write()
        self.stdout.write()
        self.stdout.write(self.style.NOTICE('Start loading data from json'))
        call_command('loaddata', 'dumps/method_transaction.json')
        call_command('loaddata', 'dumps/service_type.json')
        call_command('loaddata', 'dumps/status_payable.json')
        self.stdout.write(self.style.SUCCESS('Database filled!'))
