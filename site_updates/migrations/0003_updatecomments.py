# Generated by Django 3.2.16 on 2023-02-10 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_updates', '0002_alter_update_update_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('comment_image', models.ImageField(blank=True, default=None, upload_to='media/comment_pics/')),
                ('action_taken', models.TextField()),
                ('action_image', models.ImageField(blank=True, default=None, upload_to='media/comment_pics/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('comment_status', models.IntegerField(choices=[(0, 'No Action Required'), (1, 'Action Required')], default=0)),
                ('site_update', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_updates.update')),
            ],
            options={
                'ordering': ('-created_on',),
            },
        ),
    ]