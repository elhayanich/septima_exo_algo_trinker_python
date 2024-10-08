import json
from pprint import pprint
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
# là il va falloir regarder si le chaine de charactères "Drama" se trouve dans "pref_movie"
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
# Calcul du salaire moyen
if count > 0: 
    salaire_moyen = total_income / count
    print(f"Le salaire moyen est de ${salaire_moyen:.2f}")

################################################################################

print(colored("Salaire médian :", 'yellow'))
print(colored('DONE', 'red', 'on_green'))

salaires = []

for person in people:  
    if "income" in person: 
        # On enlève le signe dollar et on convertit la chaîne en float
        income = float(person["income"].replace('$', '').replace(',', ''))
        salaires.append(income)  

# Calcul de la médiane
if salaires: 
    salaires.sort()  
    n = len(salaires)  

    # Calcul de la médiane
    if n % 2 == 1:  # Si le nombre de salaires est impair
        median_salary = salaires[n // 2]
    else:  # Si le nombre de salaires est pair
        median_salary = (salaires[n // 2 - 1] + salaires[n // 2]) / 2

    print(f"Le salaire médian est de ${median_salary:.2f}")

################################################################################

print(colored("Nombre de personnes qui habitent dans l'hémisphère nord :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

nb_pers_hnord = 0
for person in people:
    if person["latitude"] > 0:
        nb_pers_hnord += 1

print(nb_pers_hnord)

################################################################################

print(colored("Salaire moyen des personnes qui habitent dans l'hémisphère sud :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored('LEVEL 3' + ''.join(['_' for _ in range(73)]), 'green', 'on_green'))

################################################################################

print(colored("Personne qui habite le plus près de Bérénice Cawt (nom et id) :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Personne qui habite le plus près de Ruì Brach (nom et id) :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("les 10 personnes qui habitent les plus près de Josée Boshard (nom et id) :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Les noms et ids des 23 personnes qui travaillent chez google :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Personne la plus agée :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Personne la plus jeune :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))
print(colored("Moyenne des différences d'age :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored('LEVEL 4' + ''.join(['_' for _ in range(73)]), 'green', 'on_green'))
print(colored("Genre de film le plus populaire :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Genres de film par ordre de popularité :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Liste des genres de film et nombre de personnes qui les préfèrent :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

################################################################################

print(colored("Age moyen des hommes qui aiment les films noirs :", 'yellow'))
print(colored('A IMPLEMENTER', 'red', 'on_yellow'))

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
