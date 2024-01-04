#A afficher : 
# - nombre de publications par auteur
# - liste des auteurs les plus prolifiques
# - etc

import colorama
import math

#On fait une fonction pour afficher le nombre de publications :
def nb_publi(coll) :
    count = coll.count_documents({})
    print(colorama.Fore.CYAN + "Nombre de publications totales : " + colorama.Fore.MAGENTA + f"{count}" + colorama.Style.RESET_ALL)

#On fait une fonction pour afficher le nombre de publications par année
def nb_publi_annee(coll) :
    #On liste les années
    distinct_annee = coll.distinct("year")
    #On fait un dico pour stocker le nb d'enregistrements par année
    annee_counts = {} 
    for annee in distinct_annee :
        count = coll.count_documents({"year":annee})
        annee_counts[annee] = count
    #Puis on affiche le résultat
    for annee, count in annee_counts.items() :
        print(colorama.Fore.CYAN + "Année : " + colorama.Fore.YELLOW + f"{annee}" + colorama.Fore.CYAN + ", Nombre de publications : " + colorama.Fore.YELLOW + f"{count}" + colorama.Style.RESET_ALL)

#On fait une fonction pour afficher le nombre de publications par auteur
def nb_publi_auteur(coll) :
    #On liste les années
    distinct_auteur = coll.distinct("authors")
    #On fait un dico pour stocker le nb d'enregistrements par année
    auteur_counts = {} 
    for auteur in distinct_auteur :
        count = coll.count_documents({"authors":auteur})
        auteur_counts[auteur] = count
    #Puis on affiche le résultat
    for auteur, count in auteur_counts.items() :
        print(colorama.Fore.CYAN + "Auteur : " + colorama.Fore.YELLOW + f"{auteur}" + colorama.Fore.CYAN + ", Nombre de publications : " + colorama.Fore.YELLOW + f"{count}" + colorama.Style.RESET_ALL)
    

    
#On fait une fonction pour afficher la moyenne de publications par année
def moyenne_annee(coll) :
    #On liste les années
    distinct_annee = coll.distinct("year")
    nb_annee = len(distinct_annee)
    #On fait un dico pour stocker le nb d'enregistrements par année
    count = coll.count_documents({})
    #On fait la moyenne
    moyenne = int(math.ceil(count / nb_annee))
    print(colorama.Fore.CYAN + "Nombre de publications moyennes par an : " + colorama.Fore.MAGENTA + f"{moyenne}" + colorama.Style.RESET_ALL)

#On fait une fonction pour afficher la moyenne de publications par auteur
def moyenne_auteur(coll) :
    #On liste les années
    distinct_auteur = coll.distinct("authors")
    nb_auteur = len(distinct_auteur)
    #On fait un dico pour stocker le nb d'enregistrements par année
    count = coll.count_documents({})
    #On fait la moyenne
    moyenne = int(math.ceil(count / nb_auteur))
    print(colorama.Fore.CYAN + "Nombre de publications moyennes par auteur : " + colorama.Fore.MAGENTA + f"{moyenne}" + colorama.Style.RESET_ALL)

    
        
    


