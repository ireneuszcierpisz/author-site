# Generated by Django 4.2.9 on 2024-02-05 23:15

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_contactrequest_answered'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
