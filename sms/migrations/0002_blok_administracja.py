# Generated by Django 4.2.6 on 2023-11-21 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sms", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blok",
            name="administracja",
            field=models.CharField(max_length=2, null=True),
        ),
    ]