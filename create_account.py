#sudo apt install python3-unidecode

import csv
import random
import string
import re
from unidecode import unidecode

nom_fichier = 'list.csv'

User = []
with open(nom_fichier, newline='', encoding='utf-8') as fichier_csv:
    lecteur_csv = csv.reader(fichier_csv)
    for ligne in lecteur_csv:
        prenom = re.sub(r'[^a-z]', '', unidecode(ligne[1]).lower())
        nom = re.sub(r'[^a-z]', '', unidecode(ligne[0]).lower())
        prenom_nom_propre = f"{prenom}.{nom}"
        ligne.append(prenom_nom_propre)
        rchoice = random.choices(string.ascii_letters + string.digits, k=8)
        mot_de_passe = ''.join(rchoice)
        ligne.append(mot_de_passe)
        User.append(ligne)

new = "output/account.csv"
with open(new, 'w', newline='', encoding='utf-8') as fichier_csv:
    ecrivain_csv = csv.writer(fichier_csv)
    ecrivain_csv.writerows(User)