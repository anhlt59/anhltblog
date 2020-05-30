from django.utils import timezone
from django.contrib.auth.models import User
from django.core.management import BaseCommand, CommandError
from faker import Faker
from itertools import islice


class Command(BaseCommand):
    """ python manage.py fakeuser 10 
        # to fake 10 user
    """
    help = 'Fake data user'

    def add_arguments(self, parser):
        parser.add_argument("number", type=int, help='number of record', default=1)

    def create_bulk_data(self, n):
        fake = Faker(['en_US'])
        default_password="123456"

        for _ in range(n):
            email = fake.email()
            yield User(
                username=email,
                password=default_password,
                email=email,
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                is_staff=True,
                is_superuser=False
                )

    def handle(self, *args, **options):
        N = options['number']
        count = 0

        objs = self.create_bulk_data(N)
        while True:
            batch = list(islice(objs, 100))
            if not batch:
                break
            User.objects.bulk_create(batch, ignore_conflicts=True)
            count += len(batch)
            self.stdout.write(f"> {count} user")

        # collect stats
        users = User.objects.all()
        total = users.count()
        superuser_count = users.filter(is_superuser=True).count()

        self.stdout.write(f"Total {total} user (superuser: {superuser_count}, staff: {total - superuser_count})")
