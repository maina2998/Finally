# Generated by Django 3.2.4 on 2021-10-30 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipient',
            name='blood_group',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
    ]
