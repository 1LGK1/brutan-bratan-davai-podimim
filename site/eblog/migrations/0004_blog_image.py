# Generated by Django 5.0.4 on 2024-05-06 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eblog", "0003_comment_post_alter_comment_text"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="image",
            field=models.ImageField(
                default="temp.jpg", upload_to="static/images/", verbose_name="Картинка"
            ),
        ),
    ]
