# Generated by Django 3.2.16 on 2023-02-10 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_updates', '0004_rename_updatecomments_updatecomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updatecomment',
            name='action_taken',
            field=models.TextField(blank=True),
        ),
    ]