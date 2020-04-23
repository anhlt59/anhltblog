import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from faker import Faker
from blog.models import Post
from django.contrib.auth.models import User
from django.utils import timezone
import random

def create_user(N):
    fake = Faker()
    for _ in range(N):
        email = fake.email()
        data = dict(
            username = email,
            email = email,
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            is_staff = True,
            is_superuser = random.choice([True, False]),
            date_joined = fake.date_time_between(start_date='-10y', end_date='now'),
        )
        try:
            User.objects.create_user(**data)
        except Exception as e:
            print(e)


def create_post(N):
    fake = Faker()
    users = list(User.objects.all())

    for _ in range(N):
        paragraphs = fake.paragraphs()
        user = random.choice(users)
        date = fake.date_time_between(start_date='-10y', end_date='now')

        data = dict(
            author = user,
            title = paragraphs[0].split('.')[0],
            body = ", ".join(paragraphs),
            status = random.choice(["published", "draft"]),
            created = date,
            updated = date + timezone.timedelta(hours=random.randint(1,23), days=random.randint(1,100)),
        )
        try:
            Post(**data).save()
        except Exception as e:
            print(e)
