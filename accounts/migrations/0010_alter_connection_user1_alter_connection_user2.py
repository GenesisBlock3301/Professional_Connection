# Generated by Django 4.0.6 on 2022-07-31 03:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_connection_user1_alter_connection_user2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='user1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user1_connections', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='connection',
            name='user2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user2_connections', to=settings.AUTH_USER_MODEL),
        ),
    ]
