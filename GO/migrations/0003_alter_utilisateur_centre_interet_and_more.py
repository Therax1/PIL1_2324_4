# Generated by Django 5.0.6 on 2024-06-11 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GO', '0002_utilisateur_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='centre_interet',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='email',
            field=models.EmailField(max_length=55, unique=True, verbose_name='adresse email'),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='nom',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='photo1',
            field=models.URLField(max_length=50),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='photo2',
            field=models.URLField(max_length=50),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='prenom',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='presentation',
            field=models.CharField(max_length=20),
        ),
    ]
