from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models import User


class Command(BaseCommand):
    help = 'Generate fake users'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(100):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            username = fake.user_name()
            password = fake.password()
            User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
        self.stdout.write(self.style.SUCCESS('Fake users created successfully'))
