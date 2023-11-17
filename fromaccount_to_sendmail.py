import smtplib, ssl, csv

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# on rentre les informations de l'adresse email emettrice (qui va également recevoir les mails en BCC pour vérifier qu'ils arrivent bien)
email_address = 'rebillar@insa-toulouse.fr'


smtp_address = 'smtp.insa-toulouse.fr'
smtp_port = 465
fichier_input = 'account.csv' # (à générer avec create_account.py)
passwd = open(".passwd", "r")
email_password = passwd.readlines()[0]
passwd.close()

def sendmail(receiver, content):
  message = MIMEMultipart()
  message["From"] = email_address
  message["To"] = receiver
  message["Subject"] = "[IMPORTANT] INSA GAME SHOW - accès et organisation"
  message.attach(MIMEText(content, "html"))
  message["Bcc"] = email_address

  rcpt = message["Bcc"].split(",") + [receiver]

  context = ssl.create_default_context()
  with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
    server.login(email_address, email_password)
    server.sendmail(email_address, rcpt, message.as_string())

def content(nom_fichier, user, passwd):
  with open(nom_fichier, 'r', encoding='utf-8') as fichier:
    content = fichier.read()
  content = content.replace("id_token", user)
  content = content.replace("mdp_token", passwd)
  return content

with open(fichier_input, newline='', encoding='utf-8') as fichier_csv:
  lecteur_csv = csv.reader(fichier_csv)
  for ligne in lecteur_csv:
    mail = ligne[2]
    user = ligne[3]
    mdp = ligne[4]
    print("----------------------------------")
    print("mail : " + mail)
    print("user : " + user)
    print("mdp : " + mdp)
    sendmail(mail, content("email.html", user, mdp))
    print("done.")
    print("----------------------------------")