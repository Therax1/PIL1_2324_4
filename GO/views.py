from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignInForm, SignUpForm, SignUp2Form
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *


def accueil(request):
    return render(request, 'accueil.html')



def SignInview(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('acceuil-connect')
            else:
                messages.error(request, "Identifiant ou mot de passe incorrect.")
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else:
        messages.error(request, "")
        form = SignInForm()
    return render(request, 'SignIn.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                email = request.POST['username']
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                form.save()
                user = User.objects.get(username=email)
                Profil.objects.create(user=user, nom=first_name, prenom=last_name, email=email, age=18)
                login(request, user)  # Connecter automatiquement l'utilisateur après l'inscription
                
                return redirect('signup2')
            except Exception as e:
                messages.error(request, f"Une erreur s'est produite : {e}")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = SignUpForm()
    return render(request, 'SignUp.html', {'form': form})

def signup2(request):
    userProfil = get_object_or_404(Profil, user=request.user)
    if request.method == 'POST':
        form = SignUp2Form(request.POST)
        if form.is_valid():
            # Récupérer l'utilisateur connecté
            user = request.user
            if user.is_authenticated:
                # Mettre à jour les informations supplémentaires de l'utilisateur
                userProfil.age = request.POST['age']
                userProfil.genre = request.POST['gender']
                userProfil.centres_interets = request.POST['interests']
                userProfil.description = request.POST['description']
                userProfil.save()
                # form.save()
                
                return redirect('acceuil-connect')  # Rediriger vers la page d'acceuil
            else:
                messages.error(request, 'Vous devez être connecté pour enregistrer ces informations.')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Erreur dans le champ {field}: {error}")
    else:
        form = SignUp2Form()
    return render(request, 'SignUp2.html', {'form': form, 'additional_data': 'Données supplémentaires si nécessaire'})


@login_required
def accueilConnect(request):
    profiles = Profil.objects.all()
    user_profile = get_object_or_404(Profil, user=request.user)
    return render(request, 'accueil-conect.html', {'profiles': profiles, 'user_profile':user_profile})

def AddFriend(request, username):
    newFriend = get_object_or_404(Profil, user__username=username)
    profile = get_object_or_404(Profil, user=request.user)
    # profile = request.user.profile
    profile.friends.add(newFriend)
    return redirect('acceuil-connect')

def chat(request, username):
    profile = get_object_or_404(Profil, user=request.user)
    friends = profile.friends.all()
    recipient = get_object_or_404(Profil, user__username=username)
    return render(request, 'chat.html', {
        'recipient': recipient,
        'friends': friends
    })

def deconnexion(request):
    logout(request)
    return redirect('accueil')

def explorer(request):
    return render(request, 'explorer.html')
