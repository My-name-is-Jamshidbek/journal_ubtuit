from datetime import timedelta

from django.core.management.base import BaseCommand
from faker import Faker
from articles.models import Article
import random
from django.utils import timezone
from datetime import datetime


class Command(BaseCommand):
    help = 'Generate fake articles'

    def handle(self, *args, **kwargs):
        fake = Faker()
        # for _ in range(100):
        #     title = fake.sentence(nb_words=6)
        #     description = fake.paragraph(nb_sentences=10)
        #     user_id = random.randint(1, 100)  # Assuming you have 100 users in your database
        #     file_url = "article_files/Screenshot_2024-04-04_053110.png"
        #
        #     # Generate a random datetime within the past year
        #     created_time = fake.date_time_between_dates(datetime_start=timezone.now() - timedelta(days=50))  # Generates a random datetime in the past year
        #
        #     # Convert the generated datetime to the current timezone
        #     created_time = timezone.make_aware(created_time, timezone.get_current_timezone())
        #     Article.objects.create(title=title, description=description, user_id=user_id, file_url=file_url, created_at=created_time)
        for _ in range(1000):
            title = fake.sentence(nb_words=6)
            description = fake.paragraph(nb_sentences=10)
            user_id = random.randint(1, 100)  # Assuming you have 100 users in your database
            file_url = "article_files/Screenshot_2024-04-04_053110.png"

            start_date = timezone.now() - timedelta(days=2000)  # 365 days ago
            end_date = timezone.now()  # Current datetime
            created_time = fake.date_time_between(start_date=start_date, end_date=end_date)

            Article.objects.create(title=title, description=description, user_id=user_id, file_url=file_url, created_at=created_time, status=1)
        # for _ in range(100):
        #     title = fake.sentence(nb_words=6)
        #     description = fake.paragraph(nb_sentences=10)
        #     user_id = random.randint(1, 100)  # Assuming you have 100 users in your database
        #     file_url = "article_files/Screenshot_2024-04-04_053110.png"
        #
        #     # Generate a random datetime within the past year
        #     created_time = fake.date_time_between_dates(datetime_start=timezone.now() - timedelta(days=50))  # Generates a random datetime in the past year
        #
        #     # Convert the generated datetime to the current timezone
        #     created_time = timezone.make_aware(created_time, timezone.get_current_timezone())
        #     Article.objects.create(title=title, description=description, user_id=user_id, file_url=file_url, created_at=created_time, status=2)
        # for _ in range(100):
        #     title = fake.sentence(nb_words=6)
        #     description = fake.paragraph(nb_sentences=10)
        #     user_id = random.randint(1, 100)  # Assuming you have 100 users in your database
        #     file_url = "article_files/Screenshot_2024-04-04_053110.png"
        #
        #     # Generate a random datetime within the past year
        #     created_time = fake.date_time_between_dates(datetime_start=timezone.now() - timedelta(days=30))  # Generates a random datetime in the past year
        #
        #     # Convert the generated datetime to the current timezone
        #     created_time = timezone.make_aware(created_time, timezone.get_current_timezone())
        #     Article.objects.create(title=title, description=description, user_id=user_id, file_url=file_url, created_at=created_time, status=3)
        self.stdout.write(self.style.SUCCESS('Fake articles created successfully'))
