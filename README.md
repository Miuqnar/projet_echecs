
## Développement d'un logiciel de jeu d'échecs en Python : 


## Technologies utilisées:

* Python 3.12.1

## Package Python utilisé:

* flake8==7.0.0
* pathlib
    
## Outils d'installation

#### Clonez ce repository
```bash
 git clone https://github.com/Miuqnar/projet_echecs.git
```

#### Dans le dossier do projet (projet_echecs), créez un environnement virtuel
```bash
python -m venv .env
```
#### Activez environnement virtuel sur le MacOs
```bash
source .env/bin/activate
```

## Exécuter le script

*  Dans le terminal, placez-vous dans le dossier projet_echecs avec la command :
```bash
cd projet_echecs
```
* Execution du script:
```bash
Python3 app.py
```


## View du programme  
#### Lorsque le programme est lancé, dans le menu principal l'utilisateur est saisi :

    1 : Créer un tournoi
    2 : Résumé du tournoi
    3 : Gestion des joueurs
    4 : Sortir


    Choix: _1_

#### View Ajouts des joueurs 

    Date de début: 24-01-2024 12:58:13 
    Nom du tournoi: Summer Paris
    Lieu du tournoi: Paris
    Nombre de rondes: 4
    
    Aucun joueur inscrit.
    
    Tours: 
    
    
    MENU:
    
    1. Ajouter des joueurs
    h: home 
    
    Choix: __1__

#### View Lancer le premier tour

    Date de début: 24-01-2024 12:58:13 
    Nom du tournoi: Summer Paris
    Lieu du tournoi: Paris
    Nombre de rondes: 4
    
    Liste des joueurs:
    id nom      prenom  date de naissance
    1  player1  player1 01/01/1990
    2  player2  player2 01/01/1990
    3  player3  player3 01/01/1990
    4  player4  player4 01/01/1990
    5  player5  player5 01/01/1990
    6  player6  player6 01/01/1990
    7  player7  player7 01/01/1990
    8  player8  player8 01/01/1990
    
    Tours: 
    
    
    MENU:
    
    2. Lancer le premier tour
    h: home 
    
    Choix: __2__

#### View tournament

    Date de début: 24-01-2024 12:58:13 
    Nom du tournoi: Summer Paris
    Lieu du tournoi: Paris
    Nombre de rondes: 4
    
    Liste des joueurs:
    id nom      prenom  date de naissance
    1  player1  player1 01/01/1990
    2  player2  player2 01/01/1990
    3  player3  player3 01/01/1990
    4  player4  player4 01/01/1990
    5  player5  player5 01/01/1990
    6  player6  player6 01/01/1990
    7  player7  player7 01/01/1990
    8  player8  player8 01/01/1990

    Tours:

    Tour 1 (24-01-2024 13:13:07)
       match 1) player2 vs player3  - en attente de résultats
       match 2) player1 vs player5  - en attente de résultats
       match 3) player4 vs player6  - en attente de résultats
       match 4) player7 vs player8  - en attente de résultats

        MENU:

    3. Entrer les résultats du Tour 1
    h: home 
    
    Choix: __3__


#### View tournament

    Tour 1 (24-01-2024 13:13:07)
       match 1) player2 vs player3  - en attente de résultats
       match 2) player1 vs player5  - en attente de résultats
       match 3) player4 vs player6  - player4 a gagné
       match 4) player7 vs player8  - en attente de résultats

        
    Options disponibles :
        1. Entrer le résultat du match 1
        2. Entrer le résultat du match 2
        3. Entrer le résultat du match 3
        4. Entrer le résultat du match 4
        h. Accueil
        Choix:
   

    1. player4 a gagné
    2. player6 a gagné
    3. Match nul
    Choix: __1__


    Tour 1 (24-01-2024 13:13:07)
       match 1) player2 vs player3  - en attente de résultats
       match 2) player1 vs player5  - en attente de résultats
       match 3) player4 vs player6  - player4 a gagné
       match 4) player7 vs player8  - en attente de résultats
    

    Options disponibles :
        1. Entrer le résultat du match 1
        2. Entrer le résultat du match 2
        4. Entrer le résultat du match 4
        h. Accueil
        Choix: ____

#### View tournament

    Tour 1 (24-01-2024 13:13:07)
       match 1) player2 vs player3  - player4 a gagné
       match 2) player1 vs player5  - Match nul
       match 3) player4 vs player6  - player4 a gagné
       match 4) player7 vs player8  - player8 a gagné
        
    Options disponibles :
      h. Accueil
      Choix: 
    
       h. home
        
       choice: __h__


### view tournament

    Date de début: 24-01-2024 12:58:13 
    Nom du tournoi: Summer Paris
    Lieu du tournoi: Paris
    Nombre de rondes: 4
    
    Liste des joueurs:
    id nom      prenom  date de naissance
    1  player1  player1 01/01/1990
    2  player2  player2 01/01/1990
    3  player3  player3 01/01/1990
    4  player4  player4 01/01/1990
    5  player5  player5 01/01/1990
    6  player6  player6 01/01/1990
    7  player7  player7 01/01/1990
    8  player8  player8 01/01/1990

    Tours:

    Tour 1 (24-01-2024 13:13:07)
       match 1) player2 vs player3  - player4 a gagné
       match 2) player1 vs player5  - Match nul
       match 3) player4 vs player6  - player4 a gagné
       match 4) player7 vs player8  - player8 a gagné

    Tour 2 (24-01-2024 13:13:07)
       match 1) player1 vs player4  - en attente de résultats
       match 2) player2 vs player3  - en attente de résultats
       match 3) player8 vs player6  - en attente de résultats
       match 4) player7 vs player1  - en attente de résultats

        MENU:

    3. Entrer les résultats du Tour 1
    h: home 
    
    Choix: __3__

#### Liste des tournois


    Liste des tournois
    
    Nom		Lieu	Date de début		Nombre de rounds
    
    Summer Paris	Paris	24-01-2024 13:47:24	4
    Annual Lyon	Lyon	24-01-2024 13:47:24	4
    
    MENU:
    
    Sélectionner un tournoi par son nom: 

#### Liste des joueurs
    
    Gestion des joueurs

    id nom      prenom  date de naissance
    1  player1  player1 01/01/1990
    2  player2  player2 01/01/1990
    3  player3  player3 01/01/1990
    4  player4  player4 01/01/1990
    5  player5  player5 01/01/1990
    6  player6  player6 01/01/1990
    7  player7  player7 01/01/1990
    8  player8  player8 01/01/1990

    1. Mise à jour du joueur
    h. home

    choix: __1__   
    Saisir l'identifiant du joueur: __id__

### Flake-report
![file.png](src%2Fflake-report%2Ffile.png)

