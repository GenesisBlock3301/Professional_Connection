# Generated by Django 4.1 on 2022-10-09 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='connection',
            name='accepted_or_rejected',
            field=models.CharField(blank=True, choices=[('accepted', 'Accepted'), ('rejected', 'Rejected')], max_length=20),
        ),
    ]
