# Generated by Django 3.1 on 2020-08-16 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_helper'),
    ]

    operations = [
        migrations.AddField(
            model_name='helper',
            name='helper_open',
            field=models.BooleanField(default=False),
        ),
    ]
