from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.contrib.auth.models import User


class Profil(models.Model):
    AGE_CHOICES = [(i, i) for i in range(18, 61)]
    SEXE_CHOICES = [
        ('homme', 'Homme'),
        ('femme', 'Femme'),
    ]
    INTEREST_CHOICES = [
        ('football', 'Football'),
        ('basketball', 'BasketBall'),
        ('tennis', 'Tennis'),
        ('voyage', 'Voyage'),
        ('nature', 'Nature'),
        ('musique', 'Musique'),
        ('films', 'Films et Series TV'),
        ('lecture', 'Lecture'),
        ('footing', 'Footing'),
        ('cuisine', 'Cuisine'),
        ('jeux_videos', 'Jeux Vidéos'),
        ('jeux_societe', 'Jeux de Sociétés'),
        ('arts', 'Arts et Créations'),
        ('blagues', 'Blagues'),
        ('sexto', 'Sextos'),
    ]

    age = models.IntegerField(choices=AGE_CHOICES)
    genre = models.CharField(max_length=10, choices=SEXE_CHOICES)
    photo_profil = models.ImageField(upload_to='img/', blank=True, null=True)
    centres_interets = models.CharField(max_length=20, choices=INTEREST_CHOICES)
    description = models.TextField()

    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    presentation = models.TextField(blank=True)
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    friends = models.ManyToManyField('self', blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def is_friend(self, profile):
        return self.friends.filter(id=profile.id).exists()

    def __str__(self):
        return f"{self.nom} {self.prenom}"

    class Meta:
        indexes = [
            models.Index(fields=['email'], name='email_index'),
        ]
