import csv

# Nom du fichier CSV d'entrée
fichier_csv_entree = "out_igs2023.csv"

# Nom du fichier de sortie
fichier_sortie = "radius_"+fichier_csv_entree

# Ouvrir le fichier CSV en lecture
with open(fichier_csv_entree, 'r') as fichier_csv:
    lecteur_csv = csv.reader(fichier_csv)
    
    # Ouvrir le fichier de sortie en écriture
    with open(fichier_sortie, 'w') as fichier_sortie:
        # Parcourir chaque ligne du fichier CSV
        for ligne in lecteur_csv:
            # Vérifier s'il y a suffisamment d'éléments dans la ligne
            if len(ligne) == 5:
                # Extraire le nom d'utilisateur et le mot de passe
                nom_utilisateur = ligne[3]
                mot_de_passe = ligne[4]
                
                # Écrire dans le fichier de sortie
                fichier_sortie.write(f'"{nom_utilisateur}" Cleartext-Password := "{mot_de_passe}"\n')

print("Conversion terminée.")
