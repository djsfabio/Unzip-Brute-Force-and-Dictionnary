from zipfile import ZipFile
import glob
import itertools
from time import time
import string


def g(stockList):
     for item in stockList:
            yield "".join(list(item))

def attaqueBruteForce(str_zipFile, file_list, indexListFichier):
    incrementationBoucle = 1
    
    chosetrue = True
    while chosetrue:
        # Permet de stopper le script s'il tourne jusqu'à là
        if(incrementationBoucle == 16):
            chosetrue = False
        incrementationBoucle += 1
        stockList = list(map(list, itertools.product('M' + string.digits + string.ascii_letters + string.punctuation + ' ', repeat=incrementationBoucle)))
        nouvelleListe = g(stockList)
        for motdepasse in nouvelleListe:
            # print(motdepasse)
            with ZipFile(str_zipFile) as zipObj:
                try : 
                    zipObj.extractall(pwd=bytes(motdepasse,'utf-8'))
                    print("\nLe mot de passe est \"" + motdepasse + "\" pour l'archive \"" + file_list[indexListFichier] + "\"")
                    chosetrue = False
                    break
                except Exception:
                    continue


def attaqueParDictionnaire(str_zipFile, file_list, indexListFichier): 
    listDictionnaire = []
    for line in open( "rockyou.txt", encoding = "ISO-8859-1"):
        newstr = line.strip()
        listDictionnaire.append(newstr)

    for motdepasse in listDictionnaire : 
        # print(motdepasse)
        with ZipFile(str_zipFile) as zipObj:
            try : 
                zipObj.extractall(pwd=bytes(motdepasse,'utf-8'))
                print("\nLe mot de passe est \"" + motdepasse + "\" pour l'archive \"" + file_list[indexListFichier] + "\"")
                break
            except Exception:
                pass
            if (motdepasse == listDictionnaire[len(listDictionnaire) - 1]):
                print("Le mot de passe n'as pas pu être trouvé avec la méthode \"Attaque par dictionnaire\".\nVeuillez essayer avec la méthode \"Attaque par brut force\".")
    

def main ():   
    startTime = time() 
    file_list = glob.glob('./*.zip')
    increment = 1
    print("Quel fichier souhaitez-vous extraire ? : \n")
    for fichier in file_list:
        print("[" + str(increment) + "] " + str(fichier))
        increment += 1
    indexListFichier = int(input("\nTapez l'index compris entre 1 et " + str(len(file_list)) + " : ")) - 1
    str_zipFile = file_list[indexListFichier]   
    typeAttaque = int(input("\nQuel type d'attaque souhaitez vous effectuer?\n\n[1] Attaque par dictionnaire\n[2] Attaque par brut force\n\nVotre choix : "))
    if(typeAttaque == 1):
        attaqueParDictionnaire(str_zipFile, file_list, indexListFichier)
        endTime = time()
        print('Temps total: %.2f seconds' % (endTime - startTime))
    elif(typeAttaque == 2):
        attaqueBruteForce(str_zipFile, file_list, indexListFichier)
        endTime = time()
        print('Temps total pour trouver le mot de passe: %.2f seconds' % (endTime - startTime))
    else:
        print("Veuillez saisir un type d'attaque qui existe.")

if __name__ == '__main__':
    main()