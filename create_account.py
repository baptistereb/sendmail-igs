#sudo apt install python3-unidecode

import csv
import random
import string
from unidecode import unidecode

nom_fichier = 'igs2023.csv'

User = []
with open(nom_fichier, newline='', encoding='utf-8') as fichier_csv:
    lecteur_csv = csv.reader(fichier_csv)
    for ligne in lecteur_csv:
        prenom_nom_propre = f"{unidecode(ligne[1]).lower()}.{unidecode(ligne[0]).lower()}"
        ligne.append(prenom_nom_propre)
        mot_de_passe = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        ligne.append(mot_de_passe)
        User.append(ligne)

nouveau_nom_fichier = "account.csv"
with open(nouveau_nom_fichier, 'w', newline='', encoding='utf-8') as fichier_csv:
    ecrivain_csv = csv.writer(fichier_csv)
    ecrivain_csv.writerows(User)