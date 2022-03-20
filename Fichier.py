

from distutils.util import execute
from urllib import request
import mysql.connector


def listeinstruct():

    Liste = ["Lister les tous les agences",
                "Lister tous les caissiers par ordre croissant de leur nom",
                "Lister tous chef d’agence ainsi que le nom de l’agence",
                "Lister les comptes de transaction de l’agence Plateau par ordre croissant du solde",
                "Lister la somme des montants déposés par un caissier dans un compte de transaction",
                "Lister les utilisateurs de l’agence Plateau",
                "Lister le nombre de compte par agence",
                "Lister les comptes affectés à l’utilisateur moussa diop durant le mois de Mai 2021",
                " Lister les utilisateurs à qui on a affecté le compte numéro 001 durant année 2021",
                "Lister le montant des transactions effectué par utilisateur et par date dans l’agence",
                "Lister le nombre d’affectation par utilisateur et numéro de compte durant le premier",
                "Lister les dépôts effectués et les retraits par jour dans l’agence dont le chef est moussa",
                "Lister les montants de transactions et les frais associés effectués par l’utilisateur",
                "Lister la somme des parts de l’agence, de l'état et de l’état des transactions par date",
                " Lister la somme des parts de l’agence et de l'état par agence durant deuxième de",
                "Lister l’agence qui a fait le plus de transfert durant le mois de Juin 2021",
                "Lister l’agence qui a fait le moins de transfert de dépôt le 10-08-2021",
                "Lister l’agence qui a fait le retrait le plus grand durant le mois de MAI 221",
                "Lister les agences qui n’ont pas fait de dépôt le 10-08-2021",
                "Lister les noms utilisés par l’agence numéro 001 durant le mois de MAI 221",
                "Lister le ou les clients qui ont effectué le dépôt le plus petit durant le mois de MAI",
                "Lister le ou les clients qui ont effectué le plus de dépôt durant le mois de MAI 221",
                "Lister le ou les clients qui ont effectué le plus de dépôt durant le mois de MAI 221",
                "Tapez 0pour quitter !"]
    return Liste

conect = {
        'host' : 'localhost',
        'user' : 'lamoundioss',
        'password' : 'test_123',
        'database' : 'base_exo',
        'auth_plugin':'mysql_native_password'
    }

Base = mysql.connector.connect(**conect)

cursor = Base.cursor()

#  Recuperation du menu
Execute =  []
def recupmenu(liste):
    j = 1
    for elem in liste:
        print(f"{j} : {elem}")
        j+=1
def executor(requete):
    cursor.execute(requete)
    res = cursor.fetchall()
    for line in res:
        print(line)

def fonction_1():
    Request = "SELECT adresse_AGENCE FROM AGENCE"
    executor(Request)

#  Fonction d'execution de la dexieme requete

def fonction_2():
    Request = """SELECT nom_USER, login_USER, password_USER FROM USERS 
    WHERE USERS.id_PROFIL_PROFIL = 3 ORDER BY nom_USER"""
    executor(Request)

#  Fonction d'execution de la troisieme requete

def fonction_3():
    Request = """SELECT nom_USER, login_USER, password_USER, adresse_AGENCE FROM USERS, 
    AGENCE WHERE USERS.id_PROFIL_PROFIL = 1 AND AGENCE.numero_AGENCE = USERS.numero_AGENCE_AGENCE """
    executor(Request)

# Lister les comptes de transaction de l’agence 9 Banding Plaza par ordre croissant du solde

def fonction_4():
    Request = """SELECT numero_COMPTE_TRANSACTION, numero_AGENCE_AGENCE 
    FROM TRANSACTIONS WHERE numero_AGENCE_AGENCE = 2"""
    executor(Request)

def fonction_5():
    Request = ""
    executor(Request)

# Lister les utilisateurs de l’agence 9 Banding Plaza

def fonction_6():
    Request = "SELECT * FROM USERS WHERE numero_AGENCE_AGENCE = 2"
    executor(Request)

# Lister le nombre de compte par agence

def fonction_7():
    Request = """select count(id_USER) NOMBRE, numero_AGENCE_AGENCE 
    from USERS group by numero_AGENCE_AGENCE"""
    executor(Request)

# Lister les comptes affectés à l’utilisateur Dunbar durant le mois de Mai 2021

def fonction_8():
    Request = """select * from ASSOCIER where id_USER_USER = 1 and date_debut between '2021-05-01'
    and '2021-05-31' and date_fin between '2021-05-01' and '2021-05-31'"""
    executor(Request)

# Lister les utilisateurs à qui on a affecté le compte numéro 3 durant année 2021

def fonction_9():
    Request = """select date_debut, date_fin, id_USER_USER, numero_COMPTE_TRANSACTION, nom_USER 
    from ASSOCIER, USERS where numero_COMPTE_TRANSACTION = 3 and USERS.id_USER = ASSOCIER.id_USER_USER 
    and (date_debut between '2021-01-01' and '2021-12-31' or date_fin between '2021-01-01' and '2021-12-31')"""
    executor(Request)

# Lister le montant des transactions effectué par utilisateur et par date dans l’agence dont le numéro est 3

def fonction_10():
    Request = ""
    executor(Request)


def fonction_11():
    Request = ""
    executor(Request)

# Lister les dépôts effectués et les retraits par jour dans l’agence dont le chef est Puckham par ordre croissant du montant

def fonction_12():
    Request = """SELECT date_TRANSACTION, num_TRANSACTION, montant_TRANSACTION, 
    id_TYPE_TYPE from TRANSACTIONS WHERE numero_AGENCE_AGENCE = 4 ORDER BY montant_TRANSACTION"""
    executor(Request)

# Lister les montants de transactions et les frais associés effectués par l’utilisateur
# Assane Faye dans l’agence dont le chef est moussa diop

def fonction_13():
    Request = ""
    executor(Request)

def fonction_14():
    Request = ""
    executor(Request)

def fonction_15():
    Request = ""
    executor(Request)

def fonction_16():
    Request = ""
    executor(Request)

def fonction_17():
    Request = ""
    executor(Request)

def fonction_18():
    Request = ""
    executor(Request)

def fonction_19():
    Request = ""
    executor(Request)

def fonction_20():
    Request = ""
    executor(Request)

def fonction_21():
    Request = ""
    executor(Request)

def fonction_22():
    Request = ""
    executor(Request)


def fonction_23():
    Request = ""
    executor(Request)



choisir = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
fonction = [0,fonction_1,fonction_2,fonction_3, fonction_4, fonction_5, fonction_6, fonction_7, 
fonction_8, fonction_9, fonction_10, fonction_11, fonction_12,fonction_13,fonction_14,fonction_15,
fonction_16,fonction_17,fonction_18,fonction_19,fonction_20,fonction_21,fonction_22 ]
Execute = []
liste = listeinstruct()
while True:
    recupmenu(liste)
    Choice = int(input("FAITE VOTRE CHOIX : "))
    try:
        if Choice == 0:
            break
        else:
            fonction[Choice]()
            liste.pop(Choice -1)
            Execute.append(liste[Choice-1])    
    except:
        print("Choix non disponible.")
cursor.close()


