# Generated by Django 4.2.7 on 2023-12-09 15:21

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="USER",
            fields=[
                (
                    "user_id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("user_name", models.CharField(max_length=30)),
                ("user_pwd", models.CharField(max_length=30)),
            ],
        ),
    ]
