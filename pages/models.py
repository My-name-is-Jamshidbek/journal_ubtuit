from accounts.models import User
from django.db import models


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    file_url = models.URLField()

    def __str__(self):
        return f"{self.user.get_full_name()} {self.title}"
