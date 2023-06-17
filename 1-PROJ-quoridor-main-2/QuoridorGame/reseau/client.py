import socket
import pickle

host = 'localhost'
port = 6000

thesocketc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion aux informations pour permettre le lancement du serveur
try:
    thesocketc.connect((host, port))
except socket.error:
    print("La connexion a échoué avec le serveur")
    exit()

print("Connexion réussie avec le serveur")

def envoyer_commande(sock, commande):
    # Sérialiser la commande et l'envoyer au serveur
    data = pickle.dumps(commande)
    sock.send(data)

def recevoir_etat(sock):
    # Recevoir l'état du jeu du serveur
    data = sock.recv(4096)
    etat = pickle.loads(data)
    return etat

# Demande du nom d'utilisateur
username = input("Veuillez entrer votre nom d'utilisateur : ")

while True:
    # Obtenir la commande du joueur (par exemple, à partir des entrées utilisateur)
    commande = obtenir_commande(username)
    
    # Envoyer la commande au serveur
    envoyer_commande(thesocketc, commande)
    
    # Recevoir l'état du jeu du serveur
    etat = recevoir_etat(thesocketc)
    
    if etat['type'] == 'error':
        # Gérer l'erreur reçue du serveur
        erreur = etat['message']
        traiter_erreur(erreur)
    else:
        # Mettre à jour l'état du jeu dans le client (par exemple, mettre à jour les positions des joueurs)
        mettre_a_jour_etat(etat)
    

    thesocketc.close()
