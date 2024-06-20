Site de Rencontre avec FrameWork Django PIL1_2324_4

Projet de Fin d'année donné aux Etudiant de la L1 de l'institut de formation et de la recherche en informatique
_______________________________________________________________________________________________________
Nom du Site : Venus
-----------------------------------------------------------------------------------------------
Description de la conception
Front-end
Nous avons créer une maquette global du site grâce à Canva que vous pouvez consulter directement. L'accueil varie selon le fait que l'utilisateur soit inscrit ou pas. Pour l'inscription, nous avons un formulaire qui demande à l'utilisateur de renseigner les champs, Email, Nom, Prenoms, Mot de Passe. Une deuxième page s'affiche demandant à l'utilisateur de renseigner ses différents centres d'intérêts. L'accueil avant inscription est constituer d'une barre de navigation contenant des liens externes qui ramène tous vers la page de connexion obligant l'utilisateur a se connecter. En dessous une image illustrant l'amour enfin trouver à travers une photo mettant en valeur un couple s'embrassant au bord de la mer sous un beau coucher de soleil. Juste en dessous une petite description du Site. Mettant l'accent sur sa crédibilité et sa sécurité. On retrouve après différents profile de filles. Initiant donc les utilisateurs à savoir comment leurs profile seront présenter et comment ils verront egalement le profil d'autres utilisateur. A la suite on retrouve Quelques témoignages de personnes qui se sont rencontrer grâce à notre site. Le footer marquant la fin de la page présente des liens externes tels que la section à propos, les FAQs etc... L'accueil après inscription contient une barre de navigation contenant des icônes redirigeant respectivement vers l'accueil, la page de suggestion, la messagerie, et la deconnexion. L'accueil montre les profiles déjà inscrit sur le site, ainsi que le page de suggestion, concernant la messagerie, nous avons opter pour une page affichant une partie contact montrant les utilisateurs discutant avec l'utilisateur connecté et une autre le chat active.

Back-end
Une table est utulisée pour permettre aux utulisateurs de s'inscrire puis de s'authentifier . Les informations qu'on y trouve sont dans des colonnes : Nom Prenom Email Mot de passe Age Sexe Photo Centres d'interet Presentation . Les elements sont organisés de telle sorte a permettre la securisation du site et l'amelioration de l'experience utilisateurs . L'accent est souvent mis sur la differenciation des contenues affiches en fonction du genre de l'utlisateur
WARNING
Le port pas defaut que l'on a pris par defaut pour MySQLest 3309 . Nous avions souvent eu ds problemes de cle longues lors des migrations . Pour resoudre ceci : ALTER DATABASE bd_gp4 CHARACTER SET = utf8 COLLATE= utf8_general_ci ;

_________________________________________________________________________________________________
Instructions à suivre pour le déploiement
Pour déployer et exécuter notre site de rencontre suivez ces étapes:
--------------------------------------------------------------------------------------------
Télécharger et installer Xampp Server, Django, mysqlclient
Lancer XAMPP control pannel et mettez en marche MySQL et Apache
Allez sur le navigateur et rechercher localhost/phpmyadmin
Connectez-vous avec le nom d'utilisateur root et n'utilisez pas de mot de passe puis connectez-vous
Cliquez sur le bouton, créer une nouvelle table de données et entrez comme nom: 'bd_gp4'
Aller dans le projet, faites "cd PIPG4" dans un terminal puis faire python manage.py runserver
Une address vous serez fournie. Allez sur cette address
Vous pouvez désormais voir à quoi ressemble le projet
