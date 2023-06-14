import socket 
import threading

host= 'localhost'
port= 6000 #pas sûre du port

thesocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ouverture serveur test

#connexion des informations pour permettre le lancement du serveur
try: 
    thesocket.bind((host,port))
except socket.error : 
    print("le lancement du serveur n'a pas fonctionné")
    exit()
    
    
#5 echecs de connexions  max, sert a ecouter   
thesocket.listen(5)
print("le serveur est en train de marcher")  

continuer = True

def gerer_connexion(connexion,adresse):
    print("quelqu'un vient de se connecter avec une ip {0} et pour port {1}".format(adresse[0], adresse[1]))
    
    connexion.send(b"Bienvenue sur le serveur")
    
    while True:
         #reception des données du client pour les connexions
        data = connexion.recv(1024)
    
        if not data:
            print("Vous avez été déconnecté")
            break
    
        #répondre au client
        message = "Vous aviez dit : {}".format(data.decode())
        connexion.send(message.encode())
    
    connexion.close()
    
    

#verification si une personne se connecte  
while continuer : 
    connexion, adresse = thesocket.accept() 
    
    #Thread pour gestion des clients
    thread_connexion = threading.Thread(target=gerer_connexion, args=(connexion, adresse))
    thread_connexion.start()

thesocket.close()   