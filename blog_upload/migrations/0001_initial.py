# Generated by Django 4.2.5 on 2024-02-13 09:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Otp",
            fields=[
                ("sno", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=50)),
                ("otp_user", models.CharField(max_length=4)),
            ],
        ),
    ]
