# sendmail-igs
 mailing IGS

## SETUP
dans create_account.py, dans la variable "nom_fichier" il faut mettre le chemin vers un fichier csv dont la premier colonne est le nom, la seconde le prénom et la troisieme le mail.

Configurer le mail émetteur
dans fromaccount_to_sendmail.py, dans la variable "email_address" il faut mettre l'adresse d'un mail insa.
dans .passwd le mot de passe associé à ce mail

Vous pouvez modifier le format du mail qui est le fichier "email.html" en laissant le "token_id" et "mdp_token" qui seront automatiquement remplacé pas les identifiants générés.

## UTILISATION
- lancer le script create_account.py, il va générer un fichier "account.csv" dans le dossier output qui contient les identifiants et mdp générés automatiquement.
- générer le fichier RADIUS en lançant le script "fromaccount_to_radius.py" qui va générer un fichier "radius_account" dans le dossier output vous pouvez copier ce fichier dans le fichier user du serveur RADIUS (et redémarrer le serveur RADIUS), vous pouvez maintenant vous logger avec cette base
- lancer le script fromaccount_to_sendmail.py pour envoyer les identifiants des gens par mail (sous le format de "output/email.html")
