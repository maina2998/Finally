# Generated by Django 3.2.8 on 2021-10-26 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appeals', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appeals',
            old_name='Date_last_donated',
            new_name='date_last_donated',
        ),
        migrations.RenameField(
            model_name='appeals',
            old_name='second_name',
            new_name='last_name',
        ),
    ]