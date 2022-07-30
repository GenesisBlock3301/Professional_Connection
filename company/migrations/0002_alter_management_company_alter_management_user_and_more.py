# Generated by Django 4.0.6 on 2022-07-30 05:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='management',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_managements', to='company.company'),
        ),
        migrations.AlterField(
            model_name='management',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_managements', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('employment_type', models.CharField(choices=[('full_time', 'Full-Time'), ('part_time', 'Part-Time'), ('contract', 'Contract'), ('freelance', 'Freelance'), ('seasonal', 'Seasonal')], max_length=50)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('position', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_experiences', to='company.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_experiences', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
