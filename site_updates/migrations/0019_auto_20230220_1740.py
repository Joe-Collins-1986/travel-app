# Generated by Django 3.2.16 on 2023-02-20 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_updates', '0018_remove_updatecomment_comment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='update',
            name='status',
        ),
        migrations.AddField(
            model_name='updatecomment',
            name='comment_status',
            field=models.IntegerField(choices=[(0, 'No Action Required'), (1, 'Action Required')], default=0),
        ),
    ]
