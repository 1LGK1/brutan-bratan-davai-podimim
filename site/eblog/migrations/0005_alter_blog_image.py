# Generated by Django 5.0.4 on 2024-05-06 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eblog", "0004_blog_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="image",
            field=models.ImageField(
                default="temp.jpg", upload_to="images/", verbose_name="Картинка"
            ),
        ),
    ]
