from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignInForm(forms.Form):
    email = forms.CharField(
        label="Username or E-mail",
        widget=forms.TextInput(attrs={'class': 'Username', 'placeholder': 'Username or E-mail'}),
        required=True
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'Password', 'placeholder': 'Password'}),
        required=True
    )



class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Mot de passe')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Retapez le Mot de passe')

    # class Meta:
    #     model = User
    #     fields = ['first_name', 'last_name', 'email']
    #     labels = {
    #         'first_name': 'Prénom',
    #         'last_name': 'Nom',
    #         'email': 'E-mail',
    #     }
        

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Cet email est déjà utilisé.")
        return email
    

    from django import forms
from django.core.exceptions import ValidationError

class SignUp2Form(forms.Form):
    AGE_CHOICES = [(i, str(i)) for i in range(18, 61)]
    
    age = forms.ChoiceField(choices=AGE_CHOICES, required=True, label="Age")
    gender = forms.ChoiceField(choices=[('homme', 'Homme'), ('femme', 'Femme')], widget=forms.RadioSelect, required=True, label="Je suis un/une")
    # photo_profil = forms.ImageField( label="Importez une photo de profil")
    interests = forms.MultipleChoiceField(
        choices=[
            ('football', 'Football'), ('basketball', 'BasketBall'), ('tennis', 'Tennis'), 
            ('voyage', 'Voyage'), ('nature', 'Nature'), ('musique', 'Musique'), 
            ('films_series', 'Films et Series TV'), ('lecture', 'Lecture'), 
            ('footing', 'Footing'), ('cuisine', 'Cuisine'), 
            ('jeux_videos', 'Jeux Vidéos'), ('jeux_societes', 'Jeux de Sociétés'), 
            ('arts_creations', 'Arts et Créations'), ('blagues', 'Blagues'), 
            ('sextos', 'Sextos')
        ],
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Vos centre d'intérêts"
    )
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50, 'placeholder': 'Écrivez une courte description de vous ici...'}), required=True, label="Parler nous un peu plus de vous")


    def clean_age(self):
        age = self.cleaned_data.get('age')
        if not age.isdigit():
            raise ValidationError("L'âge doit être un nombre.")
        age = int(age)
        if age < 18 or age > 60:
            raise ValidationError("L'âge doit être compris entre 18 et 60 ans.")
        return age

    def clean_photo_profil(self):
        photo = self.cleaned_data.get('photo_profil')
        if photo:
            if photo.size > 2*1024*1024:  # Limite de taille de fichier à 2MB
                raise ValidationError("La taille de la photo de profil ne doit pas dépasser 2MB.")
        return photo

    def clean(self):
        cleaned_data = super().clean()
        gender = cleaned_data.get('gender')
        if gender not in ['homme', 'femme']:
            raise ValidationError("Veuillez sélectionner un genre valide.")
        return cleaned_data


