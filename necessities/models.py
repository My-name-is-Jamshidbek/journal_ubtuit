from django.db import models
from ckeditor.fields import RichTextField

class Necessities(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()

    def __str__(self):
        return self.title
