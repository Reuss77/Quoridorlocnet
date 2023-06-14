import socket
import time

class ConnectionManager:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None
        self.connected = False

    def connect(self):
        while not self.connected:
            try:
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.connect((self.host, self.port))
                self.connected = True
                print("Connexion réussie avec le serveur")
            except socket.error as e:
                print("La connexion a échoué avec le serveur:", str(e))
                print("Tentative de reconnexion dans 5 secondes...")
                time.sleep(5)

    def reconnect(self):
        self.close()
        self.connect()

    def send(self, data):
        try:
            self.socket.send(data)
        except socket.error as e:
            print("Erreur lors de l'envoi des données:", str(e))
            self.reconnect()

    def receive(self, buffer_size):
        try:
            return self.socket.recv(buffer_size)
        except socket.error as e:
            print("Erreur lors de la réception des données:", str(e))
            self.reconnect()

    def close(self):
        if self.socket:
            self.socket.close()
            self.connected = False

# Exemple d'utilisation
host = 'localhost'
port = 6000

manager = ConnectionManager(host, port)
manager.connect()

while True:
    # Utilisez la connexion pour envoyer et recevoir des données avec le serveur
    
    # Exemple : envoyer une demande au serveur
    demande = input("Entrez un message : ")
    manager.send(demande.encode())

    # Exemple : recevoir la réponse du serveur
    response = manager.receive(1024)
    print(response.decode())

    # Vérifier si la connexion a été perdue
    if not response:
        print("La connexion avec le serveur a été perdue. Tentative de reconnexion...")
        manager.reconnect()

# Fermez la connexion lorsque vous avez terminé
manager.close()
