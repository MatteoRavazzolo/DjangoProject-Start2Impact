# Generated by Django 3.1.3 on 2020-12-27 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201227_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ip_address',
            field=models.GenericIPAddressField(null=True),
        ),
    ]
