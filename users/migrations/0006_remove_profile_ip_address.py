# Generated by Django 3.1.3 on 2020-12-28 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20201228_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='ip_address',
        ),
    ]
