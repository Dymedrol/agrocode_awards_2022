import os

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError


DEV_FIXTURES_DIR = settings.BASE_DIR / 'core' / 'fixtures_dev'


class Command(BaseCommand):
    def handle(self, *args, **options):
        call_command('migrate')
        for f in os.listdir(DEV_FIXTURES_DIR):
            if f.endswith('.json'):
                print('--- Load: {}'.format(f))
                call_command('loaddata', DEV_FIXTURES_DIR / f)
        call_command('runserver', '0.0.0.0:8000')
