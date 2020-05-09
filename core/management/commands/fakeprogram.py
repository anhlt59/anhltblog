from django.utils import timezone
from django.contrib.auth.models import User
from django.core.management import BaseCommand, CommandError
from blog.models import Program
from faker import Faker
import random
from itertools import islice


class Command(BaseCommand):
    help = 'Fake data'

    def add_arguments(self, parser):
        parser.add_argument("number", type=int, help='number of record', default=1)

    def create_bulk_data(self, n):
        fake = Faker(['en_US'])
        users = User.objects.all()

        for _ in range(n):
            name = fake.paragraph().split('.')[0]
            author = random.choice(users)
            yield Program(name=name, author=author)

    def handle(self, *args, **options):
        N = options['number']
        count = 0

        objs = self.create_bulk_data(N)
        while True:
            batch = list(islice(objs, 100))
            if not batch:
                break
            Program.objects.bulk_create(batch, ignore_conflicts=True)
            count += len(batch)

        # collect stats
        programs = Program.objects.all()
        total = programs.count()

        self.stdout.write(f"\nCreated {count} Program")
        self.stdout.write(f"Total {total} programs")
