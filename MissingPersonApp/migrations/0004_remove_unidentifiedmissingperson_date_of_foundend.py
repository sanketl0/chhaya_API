# Generated by Django 5.1.2 on 2024-10-24 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MissingPersonApp', '0003_rename_founded_data_unidentifiedmissingperson_date_of_foundend'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unidentifiedmissingperson',
            name='date_of_foundend',
        ),
    ]