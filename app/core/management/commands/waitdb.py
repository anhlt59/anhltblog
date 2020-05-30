import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, retries=10, *args, **options):
        """Handle the command"""

        self.stdout.write('Waiting for database...')
        time.sleep(1)

        if not retries:
            self.stdout.write('Connection timeout...')
            return None

        try:
            db_conn = connections['default']
        except OperationalError:
            db_conn = None
            self.stdout.write('Database unavailable, waiting 1 second...')

        if not db_conn:
            return self.handle(retries - 1, *args, **options)
