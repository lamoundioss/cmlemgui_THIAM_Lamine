
from Fichier import recupmenu

while True:
    recupmenu(listeinstruct())
    Choice = int(input("FAITE VOTRE CHOIX : "))
    fonction[Choice]()

    if Choice == 0:
        break