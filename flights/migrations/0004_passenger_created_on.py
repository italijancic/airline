# Generated by Django 3.2 on 2021-05-24 18:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_passenger'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
