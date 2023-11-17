import csv

fichier_csv_entree = "output/account.csv"
fichier_sortie = "output/radius_account"

with open(fichier_csv_entree, 'r') as fichier_csv:
    lecteur_csv = csv.reader(fichier_csv)
    with open(fichier_sortie, 'w') as fichier_sortie:
        for ligne in lecteur_csv:
            if len(ligne) == 5:
                nom_utilisateur = ligne[3]
                mot_de_passe = ligne[4]
                fichier_sortie.write(f'"{nom_utilisateur}" Cleartext-Password := "{mot_de_passe}"\n')

print("Conversion terminée.")
