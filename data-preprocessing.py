# -*- coding: utf-8 -*-
# Prétraitement de données de dialogues pour l'apprentissage d'un algorithme I.A.

import re

# Obtenir les données brutes
movie_lines = open('movie_lines.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n')
movie_conversations = open('movie_conversations.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n')

# Créer un dictionnaire de données en associant chaque ligne de dialogue 
# à son identifiant.
id_to_line = {}
for line in movie_lines:
    _line = line.split(' +++$+++ ')
    if len(_line) == 5:
        id_to_line[_line[0]] = _line[4]

# Créer la liste des conversations
conversations_ids = []
for conversation in movie_conversations[:-1]:
    _conversation = conversation.split(' +++$+++ ')[-1][1:-1]
    _conversation = _conversation.replace("'", "")
    _conversation = _conversation.replace(" ", "")
    conversations_ids.append(_conversation.split(','))

# Distinguer les questions de leurs réponses à l'aide de listes.
questions = []
answers = []
for conversation in conversations_ids:
    for i in range(len(conversation) - 1):
        questions.append(id_to_line[conversation[i]])
        answers.append(id_to_line[conversation[i+1]])

# Nettoyer le texte des formes compressées, 
# des caractères de ponctuation et autres.
def clean_text(text):
    text = text.lower()
    text = re.sub(r"i'm", "i am", text)
    text = re.sub(r"he's", "he is", text)
    text = re.sub(r"she's", "she is", text)
    text = re.sub(r"that's", "that is", text)
    text = re.sub(r"what's", "what is", text)
    text = re.sub(r"where's", "where is", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"can't", "cannot", text)
    text = re.sub(r"[-()\"#/@;:<>{}+=~|.?,]", "", text)
    return text

clean_questions = []
for question in questions:
    clean_questions.append(clean_text(question))

clean_answers = []
for answer in answers:
    clean_answers.append(clean_text(answer))

# Créer deux dictionnaires associant les mots des questions 
# et les mots des réponses à un identifiant numérique (tokenization)
# en conservant que les mots ayant au moins 20 occurences.
word_to_count = {}
for question in clean_questions:
    for word in question.split():
        if word not in word_to_count:
            word_to_count[word] = 1
        else:
            word_to_count[word] += 1
for answer in clean_answers:
    for word in answer.split():
        if word not in word_to_count:
            word_to_count[word] = 1
        else:
            word_to_count[word] += 1
threshold_questions = 20
questionswords_to_int = {}
word_number = 0
for word, count in word_to_count.items():
    if count >= threshold_questions:
        questionswords_to_int[word] = word_number
        word_number += 1
threshold_answers = 20
answerswords_to_int = {}
word_number = 0
for word, count in word_to_count.items():
    if count >= threshold_answers:
        answerswords_to_int[word] = word_number
        word_number += 1

# Ajouter les jetons de fin de ligne aux dictionnaires
tokens = ['<PAD>', '<EOS>', '<OUT>', '<SOS>']
for token in tokens:
    questionswords_to_int[token] = len(questionswords_to_int) + 1
for token in tokens:
    answerswords_to_int[token] = len(answerswords_to_int) + 1

# Créer le dictionnaire inverse de answerswords_to_int
# Utile pour l'accès aux mots à partir de leur identifiant
answersints_to_word = {w_i: w for w, w_i in answerswords_to_int.items()}

# Ajouter le jeton <EOS> à la fin de chaque réponse
for i in range(len(clean_answers)):
    clean_answers[i] += ' <EOS>'

# Convertir les dialogues en valeurs numériques entières
# et remplacer les mots filtrés par le jeton <OUT>  
questions_into_int = []
for question in clean_questions:
    ints = []
    for word in question.split():
        if word not in questionswords_to_int:
            ints.append(questionswords_to_int['<OUT>'])
        else:
            ints.append(questionswords_to_int[word])
    questions_into_int.append(ints)
answers_into_int = []
for answer in clean_answers:
    ints = []
    for word in answer.split():
        if word not in answerswords_to_int:
            ints.append(answerswords_to_int['<OUT>'])
        else:
            ints.append(answerswords_to_int[word])
    answers_into_int.append(ints)

# Trier les questions (et leurs réponses) en ordre croissant
# pour celles ayant entre 1 et 25 colonnes
sorted_clean_questions = []
sorted_clean_answers = []
for length in range(1, 25 + 1):
    for i in enumerate(questions_into_int):
        if len(i[1]) == length:
            sorted_clean_questions.append(questions_into_int[i[0]])
            sorted_clean_answers.append(answers_into_int[i[0]])
