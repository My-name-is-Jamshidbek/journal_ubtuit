from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from accounts.models import User

class New(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=500, blank=True, null=True)
    description = RichTextUploadingField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title