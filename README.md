# SoftDesk
Projet 10 - Créez une API sécurisée RESTful en utilisant Django REST

## Introduction
### Pré-requis
Avant de lancer l'API, il faut avoir git, Python3 et Poetry d'installés sur votre machine.

## Etape 1
Cloner le repositery sur votre espace de travail en utilisant git clone.

    git clone [lien du repository]

Installer les modules avec poetry install.

    poetry install

Migrer les données dans la db avec python manage.py makesmigrations | python manage.py migrate.

    python manage.py makemigrations

    python manage.py migrate

Lancer le serveur API.

    python manage.py runserver

## Etape 2

### Créer un utilisateur

Rendez-vous sur la page localhost:8000/api/register/user/
et renseigner les informations nécessaires.

[Lien : Register user](localhost:8000/api/register/user/)

<strong>ATTENTION</strong>, vous devez être agé d'au moins 15 ans pour créer votre compte.

### Récupérer le token utilisateur

Il est nécessaire d'avoir un token pour s'authentifier sur les autres pages.
Il est disponible à cette adresse en renseignant les identifiants de l'utilisateur :

[Lien : Token](localhost:8000/api/token/)

### Créer un projet

Rendez-vous sur la page api/register/project

[Lien : Register project](localhost:8000/api/register/project)

L'auteur du projet est renseigné automatiquement et devient contributeur du projet également.
La date de création est automatiquement ajoutée.

### Créer une issue pour un projet

Rendez-vous sur la page d'un projet via <em>api/project/"id_du_projet"/ </em> puis ajoutez <em>/register/issue/</em> pour ajouter une issue à ce projet.

Exemple :
<em>localhost:8000/api/project/1/register/issue/</em>

L'auteur, le projet et la date de création sont automatiquement générées. L'onglet "affected_to" sert à désigner un contributeur à qui l'issue est affectée.

### Créer un commentaire sur une issue

Rendez-vous sur la page d'une issue via <em>api/issue/"id_de_l_issue"/ </em> puis ajoutez <em>/register/comment/</em> pour ajouter un commentaire à cette issue.

Exemple :
<em> localhost:8000/api/issue/1/register/comment/</em>

L'auteur, l'issue et la date de création sont générées automatiquement.

### Voir, modifier ou supprimer un projet/issue/comment

Pour voir un projet, une issue ou un commentaire, rendez-vous sur les pages correspondantes :

[Project](localhost:8000/api/project/)- <em>localhost:8000/api/project/</em>
[Issue](localhost:8000/api/issue/)- <em>localhost:8000/api/issue/</em>
[Comment](localhost:8000/api/comment/) - <em>localhost:8000/api/comment/</em>


<strong>Pour modifier un objet </strong>: <em> localhost:8000/api/update/project/ (ou /issue/ ou /comment/) /id_de_l_obj/</em>

<strong>Pour le supprimer</strong> : <em> localhost:8000/api/delete/project/ (ou /issue/ ou /comment/) /id_de_l_obj/</em>

### S'ajouter comme contributeur d'un projet

Pour s'ajouter comme contributeur d'un projet et pouvoir créer une issue ou un commentaire, il faut aller sur la page <em> localhost:8000/api/register/contribution </em> puis choisir le projet auquel vous souhaitez contribuer.


### Supprimer ses données

Dans le cadre de la protection des données, un utilisateur peut décider de supprimer toutes traces de ses données sur l'api. Pour se faire, rendez-vous sur la page :
<em> localhost:8000/api/delete-user-data/


