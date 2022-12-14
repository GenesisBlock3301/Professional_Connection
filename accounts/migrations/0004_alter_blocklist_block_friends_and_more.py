# Generated by Django 4.1 on 2022-10-09 10:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_friendlist_blocklist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blocklist',
            name='block_friends',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friendlist',
            name='friends',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
