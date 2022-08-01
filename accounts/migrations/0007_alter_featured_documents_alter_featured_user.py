# Generated by Django 4.0.6 on 2022-07-31 02:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_connection_user1_alter_connection_user2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featured',
            name='documents',
            field=models.FileField(upload_to='featured_photos'),
        ),
        migrations.AlterField(
            model_name='featured',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_features', to=settings.AUTH_USER_MODEL),
        ),
    ]
