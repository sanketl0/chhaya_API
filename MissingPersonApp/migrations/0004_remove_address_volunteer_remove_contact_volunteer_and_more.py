# Generated by Django 5.1.2 on 2024-10-16 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MissingPersonApp', '0003_address_volunteer_contact_volunteer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='volunteer',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='volunteer',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='addresses',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='contacts',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MissingPersonApp.address'),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MissingPersonApp.contact'),
        ),
    ]