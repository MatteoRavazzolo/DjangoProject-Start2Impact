# Generated by Django 3.1.3 on 2020-12-27 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_ip_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ip_address',
            field=models.GenericIPAddressField(default=False),
        ),
    ]
