# Generated by Django 3.0.2 on 2020-04-16 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Billing', '0003_auto_20200416_1725'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Organization',
            new_name='Org',
        ),
    ]