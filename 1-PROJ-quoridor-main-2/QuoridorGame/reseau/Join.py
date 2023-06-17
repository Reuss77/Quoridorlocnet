import socket
import threading
import pickle
import pygame
import pygame.mixer
from Quoridor import Quoridor

host = 'localhost'
port = 6000

thesocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ouverture serveur test
quoridor = Quoridor()  # Création de l'instance de jeu Quoridor

# Connexion des informations pour permettre le lancement du serveur
try:
    thesocket.bind((host, port))
except socket.error:
    print("Le lancement du serveur n'a pas fonctionné")
    exit()

# 5 échecs de connexions max, sert à écouter
thesocket.listen(5)
print("Le serveur est en train de marcher")

continuer = True
nombre_joueurs_attendus = quoridor.get_nombre_joueurs_attendus()  # Nombre de joueurs attendus pour commencer le jeu
joueurs_connectes = []  # Liste des joueurs connectés

def gerer_connexion(connexion, adresse, jeu):
    print("Quelqu'un vient de se connecter avec une IP {0} et pour port {1}".format(adresse[0], adresse[1]))

    # Demande du nom d'utilisateur
    connexion.send(b"Demande de nom d'utilisateur")
    username = connexion.recv(1024).decode()

    print("Nom d'utilisateur : ", username)

    while True:
        # Réception des données du client pour les connexions
        data = connexion.recv(1024)

        if not data:
            break

        # Désérialiser la commande reçue
        commande = pickle.loads(data)

        # Traiter la commande en fonction de son type
        if commande['type'] == 'move':
            x = commande['x']
            y = commande['y']
            try:
                jeu.move_player(x, y)
                # Sérialiser l'état du jeu et l'envoyer au client
                etat = pickle.dumps(jeu)
                connexion.send(etat)
            except ValueError as e:
                # Envoyer un message d'erreur au client
                erreur = str(e)
                connexion.send(pickle.dumps({'type': 'error', 'message': erreur}))
        elif commande['type'] == 'get_state':
            # Sérialiser l'état du jeu et l'envoyer au client
            etat = pickle.dumps(jeu)
            connexion.send(etat)

    connexion.close()


# Vérification si une personne se connecte
while continuer:
    connexion, adresse = thesocket.accept()

    # Thread pour gestion des clients
    thread_connexion = threading.Thread(target=gerer_connexion, args=(connexion, adresse, quoridor))
    thread_connexion.start()

thesocket.close()
