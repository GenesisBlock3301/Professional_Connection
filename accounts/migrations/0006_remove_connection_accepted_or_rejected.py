# Generated by Django 4.1 on 2022-10-09 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_friendlist_friends_user_block_friends_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='connection',
            name='accepted_or_rejected',
        ),
    ]
