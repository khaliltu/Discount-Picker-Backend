from flask_mail import Message
from configPack import mail


def sendVerificationMail(email, name):
    msg = Message('Inscription Réussite',
                  sender='khalilscow1@gmail.com', recipients=[email])
    msg.body = "Bonjour " + name + "!" + \
        "\nBienvenue à Discount Picker! \nProfitez des meilleures promos sur les sites e-commerce Tunisiens! " + \
        "Amusez vous bien!"
    mail.send(msg)
