# Generated by Django 4.2.6 on 2023-11-07 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rss", "0013_alter_record_kto"),
    ]

    operations = [
        migrations.AddField(
            model_name="record",
            name="content",
            field=models.CharField(blank=True, max_length=160),
        ),
        migrations.AddField(
            model_name="record",
            name="phone",
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="record",
            name="kto",
            field=models.CharField(
                choices=[("Przeciwko", "Przeciwko"), ("Przez", "Przez")], max_length=22
            ),
        ),
    ]
