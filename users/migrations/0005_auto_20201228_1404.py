# Generated by Django 3.1.3 on 2020-12-28 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201227_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ip_address',
            field=models.CharField(default='ABC', max_length=100),
        ),
    ]