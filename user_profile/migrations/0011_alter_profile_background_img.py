# Generated by Django 3.2.16 on 2023-03-07 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0010_alter_profile_background_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='background_img',
            field=models.CharField(choices=[('media/profiles/background/profile-bg-default.jpg', 'Paris'), ('media/profiles/background/rome-profile-bg.jpg', 'Rome'), ('media/profiles/background/london-profile-bg.jpg', 'London')], default='media/profiles/background/profile-bg-default.jpg', max_length=100),
        ),
    ]