# Generated by Django 4.2.6 on 2023-11-12 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("rss", "0023_delete_storage_record_description_record_document_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="record",
            old_name="uploaded_at",
            new_name="data_upload",
        ),
        migrations.RenameField(
            model_name="record",
            old_name="description",
            new_name="opis",
        ),
        migrations.RenameField(
            model_name="record",
            old_name="document",
            new_name="plik",
        ),
    ]
