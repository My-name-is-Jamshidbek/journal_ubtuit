# Generated by Django 5.0.4 on 2024-04-08 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_article_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
