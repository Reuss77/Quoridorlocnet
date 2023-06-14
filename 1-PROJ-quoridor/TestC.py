import socket 

host = 'localhost'
port = 6000

thesocketc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connexion des informations pour permettre le lancement du serveur
try :
    thesocketc.connect((host, port))
except socket.error : 
    print("la connexion a echouée avec le serveur")    
    exit()
     
print("connexion reussie avec le serveur")

while True: 
    #envoyer une demande au serveur
    demande= input("entrez message : ")
    thesocketc.send(demande.encode())


    data = thesocketc.recv(1024)
    print(data.decode())
    

thesocketc.close()