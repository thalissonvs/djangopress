# Generated by Django 5.1.4 on 2025-01-19 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_post_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(default="posts/default.jpg", upload_to="posts/"),
        ),
    ]
