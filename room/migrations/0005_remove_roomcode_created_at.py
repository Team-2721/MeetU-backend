# Generated by Django 4.2.5 on 2023-10-15 07:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("room", "0004_roomcode"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="roomcode",
            name="created_at",
        ),
    ]
