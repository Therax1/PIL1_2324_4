# Generated by Django 5.0.6 on 2024-06-17 11:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GO', '0005_alter_userprofile_nom_alter_userprofile_password_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='userprofile',
            name='partial_password_index',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AddIndex(
            model_name='userprofile',
            index=models.Index(fields=['email'], name='email_index'),
        ),
    ]
