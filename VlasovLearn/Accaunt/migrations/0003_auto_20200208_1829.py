# Generated by Django 2.2.8 on 2020-02-08 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accaunt', '0002_profile_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cover',
            field=models.ImageField(default='/images/icon_0.png', upload_to='images/'),
        ),
    ]
