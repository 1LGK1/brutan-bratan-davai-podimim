# Generated by Django 5.0.4 on 2024-05-05 22:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=100,
                        unique_for_date="posted",
                        verbose_name="Заголовок",
                    ),
                ),
                ("description", models.TextField(verbose_name="Краткое содержание")),
                ("content", models.TextField(verbose_name="Полное содержание")),
                (
                    "posted",
                    models.DateTimeField(db_index=True, verbose_name="Опубликована"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
            ],
        ),
    ]