# Generated by Django 5.1.2 on 2024-10-24 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MissingPersonApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidentifiedmissingperson',
            name='founded_data',
            field=models.DateField(),
        ),
    ]