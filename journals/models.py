from django.utils import timezone
from django.db import models
from accounts.models import User


class Journal(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    file_url = models.FileField(upload_to='journal_files/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        # Update the 'updated_at' field when saving the object
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)


class JournalArticle(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="journal_articles_user",
        null=True,
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    file_url = models.FileField(upload_to='journal_article_files/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,  # Adjusted from None to SET_NULL for better handling of deletions
        null=True,
        related_name="journal_articles_author"
    )
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author if self.author else ''} {self.title}"

    def save(self, *args, **kwargs):
        # Update the 'updated_at' field when saving the object
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)
