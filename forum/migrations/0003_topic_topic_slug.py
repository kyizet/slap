# Generated by Django 3.1 on 2020-08-20 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_thread_for_community'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='topic_slug',
            field=models.SlugField(allow_unicode=True, default='djangodbmodelsfieldscharfield'),
        ),
    ]
