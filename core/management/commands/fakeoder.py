from django.utils import timezone
from django.core.management import BaseCommand, CommandError
from blog.models import Order, Price
from faker import Faker
import random
from itertools import islice


class Command(BaseCommand):
    help = 'Fake data'

    def add_arguments(self, parser):
        parser.add_argument("number", type=int, help='number of record', default=1)

    def create_bulk_data(self, n):
        fake = Faker(['en_US'])
        prices = list(Price.objects.all())

        for _ in range(n):
            state = random.choice(['published', 'draft'])
            # items = random.choices(prices)
            yield Order(state=state)
            # order.save()
            # order.items.add(*random.choices(prices, k=random.randint(2, 10)))
            # yield order

    def handle(self, *args, **options):
        N = options['number']
        count = 0

        objs = self.create_bulk_data(N)
        while True:
            batch = list(islice(objs, 100))
            if not batch:
                break
            Order.objects.bulk_create(batch, ignore_conflicts=True)
            count += len(batch)

        # mapping relationship
        orders = Order.objects.all()
        prices = Price.objects.all()



        # collect stats
        total = oders.count()

        self.stdout.write(f"\nCreated {count} Oders")
        self.stdout.write(f"Total {total} Oders")
