import random
from django.core.management.base import BaseCommand
from faker import Faker
from necessities.models import Necessities


class Command(BaseCommand):
    help = 'Generate fake necessities'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(100):
            title = fake.text(max_nb_chars=50)
            description = fake.paragraph(nb_sentences=5, variable_nb_sentences=True, ext_word_list=None)
            Necessities.objects.create(title=title, description=description)
        self.stdout.write(self.style.SUCCESS('Successfully generated 100 fake necessities'))
