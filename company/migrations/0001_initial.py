# Generated by Django 4.1 on 2022-09-10 06:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='companies_photo')),
                ('industry', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=255)),
                ('about', models.TextField(null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=255, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_managements', to='company.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_managements', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('employment_type', models.CharField(choices=[('full_time', 'Full-Time'), ('part_time', 'Part-Time'), ('contract', 'Contract'), ('freelance', 'Freelance'), ('seasonal', 'Seasonal')], max_length=50)),
                ('start', models.DateField()),
                ('end', models.DateField(null=True)),
                ('position', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_experiences', to='company.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_experiences', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
