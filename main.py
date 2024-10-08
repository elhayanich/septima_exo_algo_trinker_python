import json
from pprint import pprint
import math
from datetime import datetime
from collections import Counter 
from statistics import mean
from termcolor import colored

with open('people.json', 'r') as p:
    people = json.loads(p.read())

print(colored("""
$$$$$$$$\\        $$\\           $$\\                           $$\\                               
\\__$$  __|       \\__|          $$ |                          $$ |                              
   $$ | $$$$$$\\  $$\\ $$$$$$$\\  $$ |  $$\\  $$$$$$\\   $$$$$$\\  $$ | $$$$$$\\ $$\\    $$\\  $$$$$$\\  
   $$ |$$  __$$\\ $$ |$$  __$$\\ $$ | $$  |$$  __$$\\ $$  __$$\\ $$ |$$  __$$\\\\$$\\  $$  |$$  __$$\\ 
   $$ |$$ |  \\__|$$ |$$ |  $$ |$$$$$$  / $$$$$$$$ |$$ |  \\__|$$ |$$ /  $$ |\\$$\\$$  / $$$$$$$$ |
   $$ |$$ |      $$ |$$ |  $$ |$$  _$$<  $$   ____|$$ |      $$ |$$ |  $$ | \\$$$  /  $$   ____|
   $$ |$$ |      $$ |$$ |  $$ |$$ | \\$$\\ \\$$$$$$$\\ $$ |$$\\   $$ |\\$$$$$$  |  \\$  /   \\$$$$$$$\\ 
   \\__|\\__|      \\__|\\__|  \\__|\\__|  \\__| \\_______|\\__|\\__|  \\__| \\______/    \\_/     \\_______|
================================================================================================
   
""", 'yellow'))
print(colored('Modele des données :', 'yellow'))
pprint(people[0])

# debut de l'exo
print(colored(''.join(['_' for _ in range(80)]), 'green', 'on_green'))

print(colored("Nombre d'hommes : ", 'yellow'))
# pour chaque personne du tableau, si son genre == 'Male' je le met dans le tableau hommes
hommes = [p for p in people if p['gender'] == 'Male']
# len() revoie la taille (nombre d'élément) d'un tableau
pprint(len(hommes))

################################################################################

# je peux aussi l'écrire avec une boucle classique
hommes2 = []                        # un tableau vide
for person in people:               # pour chaque persone du tableau
    if person["gender"] == "Male":  # si c'est un homme (2-266-02250-4)
        hommes2.append(person)      # je l'ajoute au tableau
print(len(hommes2))

################################################################################

# dans la même idée, plutot que de mettre tous les hommes dans un tableau
# puis afficher la longueur du tableau, je peux juste les compter dans une variable
nb_hommes = 0                       # je commence à 0
for person in people:               # pour chaque persone du tableau
    if person["gender"] == "Male":  # si c'est un homme
        nb_hommes = nb_hommes + 1   # j'ajoute 1 à mon compteur
print(nb_hommes)

################################################################################

print(colored("Nombre de femmes : ", 'yellow'))
# je peux compter les femmes ou calculer : nombre d'élement dans people - nombre d'homme
print(colored('DONE', 'red', 'on_green'))
nb_femmes = 0                      
for person in people:               
    if person["gender"] == "Female": 
        nb_femmes = nb_femmes + 1  
print(nb_femmes)
################################################################################

print(colored("Nombre de personnes qui cherchent un homme :", 'yellow'))
print(colored('DONE', 'red', 'on_green'))
nb_cherche_homme = 0 
for person in people:  
    if "looking_for" in person and person["looking_for"] == "M": 
        nb_cherche_homme += 1  
print(nb_cherche_homme)
################################################################################

print(colored("Nombre de personnes qui cherchent une femme :", 'yellow'))
print(colored('DONE', 'red', 'on_green'))

nb_cherche_femme = 0
for person in people: 
    if "looking_for" in person and person["looking_for"] == "F":  
        nb_cherche_femme += 1  
print(nb_cherche_femme)
################################################################################

print(colored("Nombre de personnes qui gagnent plus de 2000$ :", 'yellow'))
print(colored('DONE', 'red', 'on_green'))

nb_plus_2000 = 0

for person in people:  
    if "income" in person:  
        # On enlève le signe dollar et on convertit la chaîne en float
        income = float(person["income"].replace('$', '').replace(',', ''))
        if income > 2000:  
            nb_plus_2000 += 1  
print(nb_plus_2000)


################################################################################

print(colored("Nombre de personnes qui aiment les Drama :", 'yellow'))
print(colored('DONE', 'red', 'on_green'))
nb_drama_fans = 0
for person in people:
    if 'pref_movie' in person and 'drama' in person['pref_movie'].lower():  
        nb_drama_fans += 1  
print(nb_drama_fans)
       


################################################################################

print(colored("Nombre de femmes qui aiment la science-fiction :", 'yellow'))
# si j'ai déjà un tableau avec toutes les femmes, je peux chercher directement dedans ;)
nb_femmes_scifi = 0
for person in people:  
    if "gender" in person and person["gender"] == "Female":  
        if 'pref_movie' in person and 'sci-fi' in person['pref_movie'].lower():  
            nb_femmes_scifi += 1  
print(nb_femmes_scifi)

################################################################################

print(colored('LEVEL 2' + ''.join(['_' for _ in range(73)]), 'green', 'on_green'))

################################################################################

print(colored("Nombre de personnes qui aiment les documentaires et gagnent plus de 1482$", 'yellow'))
print(colored('DONE', 'red', 'on_green'))

nb_docu_plus_1482 = 0
for person in people:  
    if 'pref_movie' in person and 'documentary' in person['pref_movie'].lower():  
        if "income" in person: 
             income = float(person["income"].replace('$', '').replace(',', ''))
        if income > 1482: 
                nb_docu_plus_1482 += 1  
print(nb_docu_plus_1482)
################################################################################

print(colored("Liste des noms, prénoms, id et revenus des personnes qui gagnent plus de 4000$", 'yellow'))
print(colored('DONE', 'red', 'on_green'))

nb_plus_4000 = []

for person in people:  
    if "income" in person:  
        income = float(person["income"].replace('$', '').replace(',', ''))
        if income > 4000:  
            nb_plus_4000.append({
                "id": person["id"],
                "first_name": person["first_name"],
                "last_name": person["last_name"],
                "income": person["income"]
            })
pprint(nb_plus_4000)



################################################################################

print(colored("Homme le plus riche (nom et id) :", 'yellow'))
print(colored('DONE', 'red', 'on_green'))

homme_plus_riche = None  
max_income = 0  

for person in people:  
    if "gender" in person and person["gender"] == "Male":  
        if "income" in person:  
            income = float(person["income"].replace('$', '').replace(',', ''))  
            if income > max_income: 
                max_income = income 
                homme_plus_riche = person  


if homme_plus_riche: 
    print(f"L'homme le plus riche est {homme_plus_riche['first_name']} {homme_plus_riche['last_name']} (ID: {homme_plus_riche['id']}) avec un revenu de {homme_plus_riche['income']}")

################################################################################

print(colored("Salaire moyen :", 'yellow'))
print(colored('DONE', 'red', 'on_green'))

total_income = 0
count = 0

for person in people:  
    if "income" in person: 
        income = float(person["income"].replace('$', '').replace(',', ''))
        total_income += income  
        count += 1 

if count > 0: 
    salaire_moyen = total_income / count
    print(f"Le salaire moyen est de ${salaire_moyen:.2f}")

################################################################################

print(colored("Salaire médian :", 'yellow'))
print(colored('DONE', 'red', 'on_green'))

salaires = []

for person in people:  
    if "income" in person: 
        income = float(person["income"].replace('$', '').replace(',', ''))
        salaires.append(income)  

# calcul de la médiane
if salaires: 
    salaires.sort()  
    n = len(salaires)  

    if n % 2 == 1:  # si le nombre de salaires est impair
        median_salary = salaires[n // 2]
    else:  # si le nombre de salaires est pair
        median_salary = (salaires[n // 2 - 1] + salaires[n // 2]) / 2

    print(f"Le salaire médian est de ${median_salary:.2f}")

################################################################################

print(colored("Nombre de personnes qui habitent dans l'hémisphère nord :", 'yellow'))
print(colored('DONE', 'red', 'on_green'))

nb_pers_hnord = 0
for person in people:
    if person["latitude"] > 0:
        nb_pers_hnord += 1

print(nb_pers_hnord)

################################################################################

print(colored("Salaire moyen des personnes qui habitent dans l'hémisphère sud :", 'yellow'))
print(colored('DONE', 'red', 'on_green'))

total_income_hs = 0  
nb_pers_hs = 0  

for person in people:  
    if person["latitude"] < 0:  # vérifie si la personne habite dans l'hsud
        if "income" in person:  
            income = float(person["income"].replace('$', '').replace(',', ''))
            total_income_hs += income  
            nb_pers_hs += 1  

# calcul du salaire moyen
if nb_pers_hs > 0:  # Vérifie s'il y a au moins une personne dans l'hsud avec un revenu
    salaire_moyen_hs = total_income_hs / nb_pers_hs
    print(f"Le salaire moyen des personnes dans l'hémisphère sud est de ${salaire_moyen_hs:.2f}")

################################################################################

print(colored('LEVEL 3' + ''.join(['_' for _ in range(73)]), 'green', 'on_green'))

################################################################################

print(colored("Personne qui habite le plus près de Bérénice Cawt (nom et id) :", 'yellow'))
print(colored('DONE', 'red', 'on_green'))

# coordonnées de Bérénice Cawt
berenice_latitude = 15.5900396
berenice_longitude = -87.879523

plus_proche_personne = None
distance_minimale = float('inf') 

for person in people:
    if "latitude" in person and "longitude" in person:
        # récupère les coordonnées de la personne
        latitude = person["latitude"]
        longitude = person["longitude"]

        # vérif que la personne n'est pas Bérénice Cawt elle-même et ignore 
        if latitude == berenice_latitude and longitude == berenice_longitude:
            continue  

        # calcul de la distance approximative et faut importer the math module
        distance = math.sqrt((latitude - berenice_latitude) ** 2 + (longitude - berenice_longitude) ** 2)

        # maj de la personne la plus proche si la distance est inférieure à la distance minimale
        if distance < distance_minimale:
            distance_minimale = distance
            plus_proche_personne = person
if plus_proche_personne:
    print(f"La personne qui habite le plus près de Bérénice Cawt est {plus_proche_personne['first_name']} {plus_proche_personne['last_name']} (ID: {plus_proche_personne['id']}).")



################################################################################

print(colored("Personne qui habite le plus près de Ruì Brach (nom et id) :", 'yellow'))
print(colored('DONE', 'red', 'on_green'))

# Coordonnées de Rui Brach
rui_latitude = 33.347316
rui_longitude = 120.16366

plus_proche_personne = None
distance_minimale = float('inf') 

for person in people:
    if "latitude" in person and "longitude" in person:
        # récupère les coordonnées de la pers
        latitude = person["latitude"]
        longitude = person["longitude"]

        # Vérifie que la personne n'est pas rui himself et ignore 
        if latitude == rui_latitude and longitude == rui_longitude:
            continue  

        # calcul de la distance approximative et faut importer the math module
        distance = math.sqrt((latitude - rui_latitude) ** 2 + (longitude - rui_longitude) ** 2)

        # maj de la personne la plus proche si la distance est inférieure à la distance minimale
        if distance < distance_minimale:
            distance_minimale = distance
            plus_proche_personne = person
if plus_proche_personne:
    print(f"La personne qui habite le plus près de rui brach est {plus_proche_personne['first_name']} {plus_proche_personne['last_name']} (ID: {plus_proche_personne['id']}).")




################################################################################

print(colored("les 10 personnes qui habitent les plus près de Josée Boshard (nom et id) :", 'yellow'))
print(colored('DONE', 'red', 'on_green'))

josee_latitude = 57.6938555
josee_longitude = 11.9704401

distances = []

for person in people:
    if "latitude" in person and "longitude" in person:
        latitude = person["latitude"]
        longitude = person["longitude"]

        # calcul de la distance approximative
        distance = math.sqrt((latitude - josee_latitude) ** 2 + (longitude - josee_longitude) ** 2)
        distances.append((distance, person))

# tri par distance (de la plus petite à la plus grande) et sélection des 10 plus proches
distances.sort(key=lambda x: x[0])
closest_people = distances[:10]

print("Les 10 personnes qui habitent le plus près de Josée Boshard :")
for _, person in closest_people:
    print(f"{person['first_name']} {person['last_name']} (ID: {person['id']})")

################################################################################

print(colored("Les noms et ids des 23 personnes qui travaillent chez google :", 'yellow'))
print(colored('DONE', 'red', 'on_green'))


google_employees = []

for person in people:
    if "google" in person["email"].lower():  #verif de l'email if it contains google 
        google_employees.append({
            "first_name": person["first_name"],
            "last_name": person["last_name"],
            "id": person["id"]
        })
print("Les personnes qui travaillent chez Google :")
for employee in google_employees:
    print(f"{employee['first_name']} {employee['last_name']} (ID: {employee['id']})")

################################################################################

print(colored("Personne la plus agée :", 'yellow'))
print(colored('DONE', 'red', 'on_green'))

personne_plus_agee = None
age_maximum = -1

# date actuelle pour le calcul de lage
date_actuelle = datetime.now()
for person in people:
    if "date_of_birth" in person:
        # convertit la date de naissance en objet datetime
        date_naissance = datetime.strptime(person["date_of_birth"], "%Y-%m-%d")
        
        # Calcule l'âge
        age = (date_actuelle - date_naissance).days // 365  # convertit les jours en années

        # maj de la personne la plus agée si lage est supérieur à lage maximum
        if age > age_maximum:
            age_maximum = age
            personne_plus_agee = person
if personne_plus_agee:
    print(f"La personne la plus âgée est {personne_plus_agee['first_name']} {personne_plus_agee['last_name']} (ID: {personne_plus_agee['id']}, Age: {age_maximum} ans).")

################################################################################

print(colored("Personne la plus jeune :", 'yellow'))
print(colored('DONE', 'red', 'on_green'))

personne_plus_jeune = None
age_minimum = float('inf')  # Initialise à l'infini

#actual date pour le calcul de lage
date_actuelle = datetime.now()

for person in people:
    if "date_of_birth" in person:
        date_naissance = datetime.strptime(person["date_of_birth"], "%Y-%m-%d")
        age = (date_actuelle - date_naissance).days // 365  
        if age < age_minimum:
            age_minimum = age
            personne_plus_jeune = person
if personne_plus_jeune:
    print(f"La personne la plus jeune est {personne_plus_jeune['first_name']} {personne_plus_jeune['last_name']} (ID: {personne_plus_jeune['id']}, Age: {age_minimum} ans).")



################################################################################




print(colored("Moyenne des différences d'age :", 'yellow'))
print(colored('DONE', 'red', 'on_green'))

ages = []
date_actuelle = datetime.now()

for person in people:
    if "date_of_birth" in person:
        date_naissance = datetime.strptime(person["date_of_birth"], "%Y-%m-%d")
        age = (date_actuelle - date_naissance).days // 365  
        ages.append(age)

# calculer la moyenne des différences dage
somme_differences = 0
nombre_de_paires = 0


#calcul les différences dage entre chaque partie de pers
for i in range(len(ages)):
    for j in range(i + 1, len(ages)):
        difference = abs(ages[i] - ages[j])
        somme_differences += difference
        nombre_de_paires += 1

# Calculer la moyenne
moyenne_diff = somme_differences / nombre_de_paires if nombre_de_paires > 0 else 0
print(f"La moyenne des différences d'âge est de {moyenne_diff:.2f} ans.")

################################################################################

print(colored('LEVEL 4' + ''.join(['_' for _ in range(73)]), 'green', 'on_green'))
print(colored("Genre de film le plus populaire :", 'yellow'))
print(colored('DONE', 'red', 'on_green'))


pref_movie_list = []

# extraire les prefs de films
for person in people:
    if "pref_movie" in person:
        genres = person["pref_movie"].split('|')  # sépare les genres 
        pref_movie_list.extend(genres)  # ajoute les genres à la liste

# compter les occurrences de chaque genre
genre_counts = Counter(pref_movie_list)

# trouver le genre le plus popular
genre_populaire = genre_counts.most_common(1)  # Renvoie le genre le plus fréquent
if genre_populaire:
    genre, count = genre_populaire[0]
    print(f"Le genre de film le plus populaire est '{genre}' avec {count} occurrences.")

################################################################################

print(colored("Genres de film par ordre de popularité :", 'yellow'))
print(colored('DONE', 'red', 'on_green'))

pref_movie_list = []

for person in people:
    if "pref_movie" in person:
        genres = person["pref_movie"].split('|')  
        pref_movie_list.extend(genres)  
# Compter les occurrences de chaque genre
genre_counts = Counter(pref_movie_list)

# Tri de genres par ordre de popularité
genres_tries = genre_counts.most_common()
print("Genres de film par ordre de popularité :")
for genre, count in genres_tries:
    print(f"{genre}: {count} occurrences")

################################################################################

print(colored("Liste des genres de film et nombre de personnes qui les préfèrent :", 'yellow'))
print(colored('DONE', 'red', 'on_green'))
 
pref_movie_list = []

for person in people:
    if "pref_movie" in person:
        genres = person["pref_movie"].split('|')  
        pref_movie_list.extend(genres) 
genre_counts = Counter(pref_movie_list)
print("Genres de film et nombre de personnes qui les préfèrent :")
for genre, count in genre_counts.items():
    print(f"{genre}: {count} personne(s)")


################################################################################

print(colored("Age moyen des hommes qui aiment les films noirs :", 'yellow'))
print(colored('DONE', 'red', 'on_green'))

aujourdhui = datetime.now()
ages_hommes_films_noirs = []

for person in people:
    # Filtrer les hommes qui aiment les films noirs
    if person["gender"] == "Male" and "Film-Noir" in person["pref_movie"]:
        # Calculer l'âge
        date_naissance = datetime.strptime(person["date_of_birth"], "%Y-%m-%d")
        age = aujourdhui.year - date_naissance.year - ((aujourdhui.month, aujourdhui.day) < (date_naissance.month, date_naissance.day))
        ages_hommes_films_noirs.append(age)

# Calculer l'âge moyen
if ages_hommes_films_noirs:
    age_moyen = mean(ages_hommes_films_noirs)
    print(f"L'âge moyen des hommes qui aiment les films noirs est de {age_moyen:.2f} ans.")

################################################################################

print(colored("Age moyen des femmes qui aiment les drames et habitent sur le fuseau horaire, de Paris : ", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("""Homme qui cherche un homme et habite le plus proche d'un homme qui a au moins une
préférence de film en commun (afficher les deux et la distance entre les deux):""", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Liste des couples femmes / hommes qui ont les même préférences de films :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored('MATCH' + ''.join(['_' for _ in range(73)]), 'green', 'on_green'))
"""
    On match les gens avec ce qu'ils cherchent (homme ou femme).
    On prend en priorité ceux qui ont le plus de gouts en commun.
    Puis ceux qui sont les plus proches.
    Les gens qui travaillent chez google ne peuvent qu'être en couple entre eux.
    Quelqu'un qui n'aime pas les Drama ne peux pas être en couple avec quelqu'un qui les aime.
    Quelqu'un qui aime les films d'aventure doit forcement être en couple avec quelqu'un qui aime aussi 
    les films d'aventure.
    La différences d'age dans un couple doit être inférieure à 25% (de l'age du plus agé des deux)
    ߷    ߷    ߷    Créer le plus de couples possibles.                  ߷    ߷    ߷    
    ߷    ߷    ߷    Mesurez le temps de calcul de votre fonction         ߷    ߷    ߷    
    ߷    ߷    ߷    Essayez de réduire le temps de calcul au maximum     ߷    ߷    ߷    

"""
print(colored("liste de couples à matcher (nom et id pour chaque membre du couple) :", 'yellow'))
print(colored('Exemple :', 'green'))
print(colored('1 Alice A.\t2 Bob B.'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))
