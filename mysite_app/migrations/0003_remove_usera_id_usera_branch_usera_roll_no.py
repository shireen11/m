# Generated by Django 4.0.6 on 2022-12-06 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite_app', '0002_remove_usera_branch_remove_usera_roll_no_usera_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usera',
            name='id',
        ),
        migrations.AddField(
            model_name='usera',
            name='branch',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='usera',
            name='roll_no',
            field=models.CharField(blank=True, max_length=255, primary_key=True, serialize=False),
        ),
    ]
