from django.utils import timezone
from django.contrib.auth.models import User
from django.core.management import BaseCommand, CommandError
from blog.models import Post
from faker import Faker
import random


class Command(BaseCommand):
    """ python manage.py fakeuser 10
        # to fake 10 post
    """
    help = 'Fake data user'

    def add_arguments(self, parser):
        # parser.add_argument("-n", "--number", type=int, help='number of post', default=1)
        parser.add_argument("number", type=int, help='number of record', default=1)

    def handle(self, *args, **options):
        fake = Faker(['en_US'])
        users = list(User.objects.all())
        N = options['number']
        count = 0

        for _ in range(N):
            paragraphs = fake.paragraphs()

            author = random.choice(users)
            title = paragraphs[0].split('.')[0]
            body = "\n ".join(paragraphs)
            status = "published"#random.choice(["published", "draft"])
            created = fake.date_time_between(start_date='-10y', end_date='now')
            updated = created + timezone.timedelta(hours=random.randint(1,23), days=random.randint(1,100))

            try:
                Post(author=author,
                     title=title,
                     body=body,
                     status=status,
                     created=created,
                     updated=updated
                     ).save()
                self.stdout.write(f"Created Post: {author} - {title}")
                count += 1
            except Exception as e:
                self.stdout.write(repr(e))
            # endfor

        # collect stats
        posts = Post.objects.all()
        total = posts.count()
        draft_count = posts.filter(status="draft").count()

        self.stdout.write(f"\n{'-'*80}\nCreated {count} post")
        self.stdout.write(f"Total {total} post (draft: {draft_count}, published: {total - draft_count})")
