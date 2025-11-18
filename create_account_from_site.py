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
        new_line=[]
        prenom = re.sub(r'[^a-z]', '', unidecode(ligne[1]).lower())
        nom = re.sub(r'[^a-z]', '', unidecode(ligne[0]).lower())
        prenom_nom_propre = f"{prenom}.{nom}"
        rchoice = random.choices("abcdefghjkmnopqrstuvwxyzABCDEFGHJKMNOPQRSTUVWXYZ123456789", k=8)
        mot_de_passe = ''.join(rchoice)
        new_line.append(ligne[0])
        new_line.append(ligne[1])
        new_line.append(ligne[3])
        new_line.append(prenom_nom_propre)
        new_line.append(mot_de_passe)
        User.append(new_line)

new = "output/account.csv"
with open(new, 'w', newline='', encoding='utf-8') as fichier_csv:
    ecrivain_csv = csv.writer(fichier_csv)
    ecrivain_csv.writerows(User)