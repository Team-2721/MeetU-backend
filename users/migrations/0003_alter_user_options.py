# Generated by Django 4.2.5 on 2023-10-14 07:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_avatar_alter_user_nickname"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"verbose_name_plural": "회원 목록"},
        ),
    ]
