# Generated by Django 2.2.17 on 2021-01-11 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearnSystem', '0013_ticketwebinar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webinar',
            name='guid',
        ),
        migrations.AddField(
            model_name='webinar',
            name='url',
            field=models.URLField(default=1, verbose_name='Zoom'),
            preserve_default=False,
        ),
    ]
