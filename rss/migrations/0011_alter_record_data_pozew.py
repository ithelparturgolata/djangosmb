# Generated by Django 4.2.6 on 2023-11-06 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rss", "0010_alter_record_data_pozew"),
    ]

    operations = [
        migrations.AlterField(
            model_name="record",
            name="data_pozew",
            field=models.DateField(blank=True),
        ),
    ]
