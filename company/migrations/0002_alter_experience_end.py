# Generated by Django 4.1 on 2022-08-25 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end',
            field=models.DateField(null=True),
        ),
    ]
