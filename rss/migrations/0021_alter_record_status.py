# Generated by Django 4.2.7 on 2023-12-05 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0020_alter_record_data_pozew'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='status',
            field=models.CharField(choices=[('Zakonczono', 'Zakonczono'), ('W trakcie realizacji', 'W trakcie realizacji'), ('Zawieszone', 'Zawieszone')], default='Zakonczono', max_length=22),
        ),
    ]