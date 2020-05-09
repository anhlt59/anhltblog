from django.utils import timezone
from django.contrib.auth.models import User
from django.core.management import BaseCommand, CommandError
from blog.models import Post
from faker import Faker
import random
from itertools import islice


class Command(BaseCommand):
    """ python manage.py fakeuser 10
        # to fake 10 post
    """
    help = 'Fake data user'

    def add_arguments(self, parser):
        # parser.add_argument("-n", "--number", type=int, help='number of post', default=1)
        parser.add_argument("number", type=int, help='number of record', default=1)

    def create_bulk_data(self, n):
        fake = Faker(['en_US'])
        users = User.objects.all()

        for _ in range(n):
            paragraphs = fake.paragraphs()
            author = random.choice(users)
            title = paragraphs[0].split('.')[0]
            body = "\n ".join(paragraphs)
            status = "published"#random.choice(["published", "draft"])
            created = fake.date_time_between(start_date='-10y', end_date='now')
            updated = created + timezone.timedelta(hours=random.randint(1,23), days=random.randint(1,100))

            yield Post(
                 author=author,
                 title=title,
                 body=body,
                 status=status,
                 created=created,
                 updated=updated
                 )

    def handle(self, *args, **options):
        N = options['number']
        count = 0

        objs = self.create_bulk_data(N)
        while True:
            batch = list(islice(objs, 100))
            if not batch:
                break
            Post.objects.bulk_create(batch, ignore_conflicts=True)
            count += len(batch)

        # collect stats
        posts = Post.objects.all()
        total = posts.count()
        draft_count = posts.filter(status="draft").count()

        self.stdout.write(f"\nCreated {count} post")
        self.stdout.write(f"Total {total} post (draft: {draft_count}, published: {total - draft_count})")
