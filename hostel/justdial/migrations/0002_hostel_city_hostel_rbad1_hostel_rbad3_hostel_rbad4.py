# Generated by Django 5.0.1 on 2024-01-28 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justdial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostel',
            name='city',
            field=models.CharField(default='pune', max_length=100),
        ),
        migrations.AddField(
            model_name='hostel',
            name='rbad1',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='hostel',
            name='rbad3',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='hostel',
            name='rbad4',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
