# Generated by Django 3.0.2 on 2020-04-16 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Billing', '0002_auto_20200416_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('lform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Billing.LegalForm')),
            ],
            options={
                'ordering': ['fullname'],
            },
        ),
        migrations.RemoveField(
            model_name='legalformdetails',
            name='binyan_ptr',
        ),
        migrations.RemoveField(
            model_name='legalformupdate',
            name='binyan_ptr',
        ),
        migrations.DeleteModel(
            name='LegalFormDelete',
        ),
        migrations.DeleteModel(
            name='LegalFormDetails',
        ),
        migrations.DeleteModel(
            name='LegalFormUpdate',
        ),
    ]
