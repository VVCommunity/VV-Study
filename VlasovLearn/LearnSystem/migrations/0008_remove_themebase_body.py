# Generated by Django 2.2.17 on 2021-01-04 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LearnSystem', '0007_auto_20210104_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='themebase',
            name='body',
        ),
    ]
