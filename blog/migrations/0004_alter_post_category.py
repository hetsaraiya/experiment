# Generated by Django 4.2.5 on 2024-02-13 12:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_alter_post_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="Category",
            field=models.CharField(default="", max_length=255),
        ),
    ]