from django.utils import timezone
from django.core.management import BaseCommand, CommandError
from blog.models import Price, Program
from faker import Faker
import random
from itertools import islice


class Command(BaseCommand):
    help = 'Fake data'

    def add_arguments(self, parser):
        parser.add_argument("number", type=int, help='number of record', default=1)

    def create_bulk_data(self, n):
        fake = Faker(['en_US'])
        programs = Program.objects.all()

        for _ in range(n):
            program = random.choice(programs)
            price = random.randint(10, 100)
            yield Price(program=program, price=price)

    def handle(self, *args, **options):
        N = options['number']
        count = 0

        objs = self.create_bulk_data(N)
        while True:
            batch = list(islice(objs, 100))
            if not batch:
                break
            Price.objects.bulk_create(batch, ignore_conflicts=True)
            count += len(batch)

        # collect stats
        prices = Price.objects.all()
        total = prices.count()

        self.stdout.write(f"\nCreated {count} Prices")
        self.stdout.write(f"Total {total} Prices")
