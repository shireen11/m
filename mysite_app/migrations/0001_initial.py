# Generated by Django 4.0.6 on 2022-12-05 04:15

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
            name='UserA',
            fields=[
                ('roll_no', models.CharField(blank=True, max_length=255, primary_key=True, serialize=False)),
                ('branch', models.CharField(blank=True, max_length=255)),
                ('phone', models.IntegerField(blank=True, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]