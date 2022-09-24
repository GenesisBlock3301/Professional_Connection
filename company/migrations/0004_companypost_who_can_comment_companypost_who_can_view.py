# Generated by Django 4.1 on 2022-09-15 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_companyfollower'),
    ]

    operations = [
        migrations.AddField(
            model_name='companypost',
            name='who_can_comment',
            field=models.CharField(choices=[('everyone', 'everyone'), ('public', 'public'), ('only_connection', 'only connection')], default='public', max_length=25),
        ),
        migrations.AddField(
            model_name='companypost',
            name='who_can_view',
            field=models.CharField(choices=[('everyone', 'everyone'), ('public', 'public'), ('only_me', 'only-me')], default='public', max_length=20),
        ),
    ]
