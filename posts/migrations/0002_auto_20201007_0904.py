# Generated by Django 3.1.2 on 2020-10-07 09:04

import django.utils.timezone
from django.db import migrations, models

import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(upload_to=posts.models.uploaded_image_name),
        ),
    ]
