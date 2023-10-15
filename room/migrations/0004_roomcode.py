# Generated by Django 4.2.5 on 2023-10-15 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("room", "0003_alter_attendee_options_alter_vote_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="RoomCode",
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
                ("code", models.CharField(max_length=4, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="code",
                        to="room.room",
                    ),
                ),
            ],
        ),
    ]
