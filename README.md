# data-preprocessing-for-dialogs

Exercice : Prétraitement de données de dialogues pour l'apprentissage d'un algorithme I.A.

Pourquoi ? 70% du temps d'un programmeur d'I.A. est utilisé au prétraitement des données. Les algorithmes ne peuvent pas apprendre sans ces données. :(

Traiter des données avant de les utiliser pour l'entrainement du système. Organiser un dictionnaire de données de dialogues.
* Nettoyer des dictionnaires de données :
** Remplacer la forme compressée d'expressions (ex.: "I'm" devient "I am").
** Conserver que les mots ayant plus de 20 occurences.
* Ajouter des jetons pour les decodeurs, "tokenization" :
** Ajouter le jeton <EOS> pour marquer la fin de la phrase.
** Ajouter le jeton <OUT> afin de filtrer les mots les moins utilisés.
* Convertir les dialogues en valeurs numériques entières : remplacer chaque mot par son identifiant.
* Trier les questions en ordre croissant de grandeur afin que le système puisse apprendre avec des phrases plus courtes pour commencer.

Pour plus de détails à propos du prétraitement de données, voir cette présentation : https://www.mimuw.edu.pl/~son/datamining/DM/4-preprocess.pdf

# Téléchargement

Vous pouvez téléchargez l'archives .zip du code ou bien utilisez git : 
$ git clone https://github.com/computer-science-club-ca/data-preprocessing-for-dialogs.git

## Téléchargez le corpus de dialogues 
Téléchargez le corpus de dialogues anglophones à partir du site de l'Université Cornell : https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html

* Décompressez les fichiers de l'archives cornell_movie_dialogs_corpus.zip. Les fichiers qui nous intéressent sont :
** movie_conversations.txt - Regroupe les lignes de chaque conversation se trouvant dans le fichier movie_lines.txt.
** movie_lines.txt - Lignes de dialogues.
*** Description des colonnes : identifiant de lignes, identifiant de l'interlocuteur, identifiant du film, le nom du personnage, ligne de dialogue.

# L'environnement

C'est un projet Python.

## Installez Anaconda 3.6

https://www.anaconda.com/download/

# Configuration

## Créez l'environnement virtuel Python 3.5

Vous allez créer un environnement virtuel nommé "dialog".
* Via le terminal ("Anaconda Prompt" pour les utilisateurs de Windows), allez dans le réperoire du projet, par exemple D:\AnacondaProjects\data-preprocessing-for-dialogs\.
* Créez l'environnement, tapez : conda create -n dialog python=3.5 anaconda
* Le processus va créer l'environnement et installer les librairies nécessaires. Tapez 'y' suivi de la touche Entrée à la demande de confirmation.
** L'installation demandera quelques instants...

* Pour activer cet environnement,
** tapez : source activate dialog
** si vous utilisez Windows, tapez seulement : activate dialog

* Via Anaconda Navigator,
** vous pouvez sélectionner votre environnement virtuel via la liste 'Application on' : dialog.
** lancez l'IDE Spyder en cliquant sur le bouton 'Launch' de son encadré.
