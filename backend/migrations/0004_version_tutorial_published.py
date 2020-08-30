# Generated by Django 3.1 on 2020-08-11 10:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_change_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='tutorial_published',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]