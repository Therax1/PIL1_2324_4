from django.urls import path
from .views import accueil,SignInview , signup , signup2, accueilConnect, deconnexion, AddFriend, chat , explorer
urlpatterns = [
    path('', accueil, name='accueil'),
    # Add other URLs here
    path('SignIn/', SignInview, name='SignIn'),
    path('signup/', signup, name='signup'),
    path('signup2/', signup2 , name='signup2'),
    path('add/friend/<str:username>', AddFriend, name='add_friend'),
    path('chat/<str:username>/', chat, name='chat'),
    path('acceuil/connect/', accueilConnect , name='acceuil-connect'),
    path('deconnexion/', deconnexion, name='deconnexion' ),
    path('explorer/', explorer, name='explorer' ),


]










