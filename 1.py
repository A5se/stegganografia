from stegano import lsb
secret = lsb.hide("img/1.png","Your password: qwerty")
secret.save("img/1_secret.png")
result = lsb.reveal("img/1_secret.png")