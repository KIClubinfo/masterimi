
Pr�sentation : API REST DJANGO consistuant le Back de l'outil demand� par le d�partement IMI pour aider les �l�ves � construire correctement leur 3A.

Lancement du code :

Ouvrir un terminal dans le dossier contenant le fichier manage.py. Entrer en ligne de commande :  python manage.py runserver   
Ouvrir ensuite un navigateur et entrer dans la barre de recherche   http://localhost:8000/parcoursimi/   pour acc�der � la racine de l'API.

Commentaires sur le travail effectu�:

- La structure de la base de donn�e est r�gie par le fichier model.py qui cr�e les mod�les. 
Jusqu'ici, j'ai pu cr�er les Serializers associ�s aux modeles permettant un passage des donn�es stock�es en m�moire � leur traduction au format JSON et inversement.
J'ai cr�� les vues associ�es.

- J'ai essay� de traduire correctement dans les serializers les relations entre mod�les. C'est ce qui m'a pos� un peu de souci avec �galement la cr�ation 
et modification du profile utilisateur (d'ailleurs peux-tu me donner ton avis sur cette partie du code ? car je ne suis pas s�r d'avoir eu la bonne vision.)

Apr�s ta validation du code actuel et correction des erreurs/manques qui tu me signaleras, je pense proc�der � la gestion de permissions/autorisation sur l'acc�s 
aux diff�rentes vues (j'ai vu comment faire et �a n'a pas l'air difficile).


