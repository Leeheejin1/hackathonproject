# Generated by Django 2.2.3 on 2019-08-02 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vr_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evidence', models.ImageField(upload_to='images/')),
                ('sex', models.CharField(blank=True, max_length=15)),
                ('birth_date', models.CharField(blank=True, max_length=15)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('agreement1', models.CharField(blank=True, max_length=10)),
                ('agreement2', models.CharField(blank=True, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
