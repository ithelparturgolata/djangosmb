# Generated by Django 4.2.6 on 2023-11-19 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("telefony", "0003_mieszkaniec_content_mieszkaniec_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="mieszkaniec",
            name="symbol_budynku",
            field=models.CharField(blank=True, max_length=4),
        ),
    ]
