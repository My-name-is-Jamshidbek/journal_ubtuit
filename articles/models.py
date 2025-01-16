from accounts.models import User
from django.db import models
from django.utils import timezone


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    reason = models.TextField(default="Kiritilmagan")
    file_url = models.FileField(upload_to='article_files/')
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.title}"

    def save(self, *args, **kwargs):
        # Update the 'updated_at' field when saving the object
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)
