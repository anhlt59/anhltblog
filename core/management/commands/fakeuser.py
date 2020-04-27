from django.utils import timezone
from django.contrib.auth.models import User
from django.core.management import BaseCommand, CommandError
from faker import Faker


class Command(BaseCommand):
    """ python manage.py fakeuser 10
        # to fake 10 user
    """
    help = 'Fake data user'

    def add_arguments(self, parser):
        parser.add_argument("number", type=int, help='number of record', default=1)

    def handle(self, *args, **options):
        N = options['number']
        fake = Faker(['en_US'])
        default_password="123456"
        count = 0

        for _ in range(N):
            email = fake.email()

            try:
                User.objects.create_user(
                    username=email,
                    password=default_password,
                    email=email,
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    is_staff=True,
                    is_superuser=False
                    )
                self.stdout.write(f"Create {email}/{default_password} done")
                count += 1
            except Exception as e:
                self.stdout.write(repr(e))
            # endfor

        # collect stats
        users = User.objects.all()
        total = users.count()
        superuser_count = users.filter(is_superuser=True).count()

        self.stdout.write(f"\n{'-'*80}\nCreated {count} user")
        self.stdout.write(f"Total {total} user (superuser: {superuser_count}, staff: {total - superuser_count})")
