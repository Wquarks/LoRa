from network import LoRa #pour être en mode LoRa
import socket #pour envoyer des trames
import time # pour la gestion du timer

print('start')

lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868, preamble=20, sf=12)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(True)
i=0 #i permet d’identifier le numero de trame et donc les trame perdu

while True:
    msg=str(i)+"abcdefghijklmnopqrstuvwxyz0123456789" #chaine à envoyer
    s.send(msg) # envoie du message
    print(msg) # visulisation de celui-ci si on est branché à un PC
    i+=1
    time.sleep(2) # temps d’attente
