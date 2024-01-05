#import de la BDD MongoDB
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client["my-first-db"]
coll = db['books_projet']
import pprint

import colorama

# count = coll.count_documents({})
# print(count)
# #auteur = "Surendra Dayal"
# #for item in coll.aggregate([{"$unwind":"$authors"},{"$match":{"$and":[{"authors":{"$regex":auteur}},{"year":1993}]}}]):
# #    pprint.pprint(item)

# for item in coll.distinct("year") :
#     pprint.pprint(item)

#print(len(coll.distinct("authors")))
    
# for item in coll.aggregate([{"$unwind":"$authors"},{"$group":{"_id":"$authors","nb":{"$sum":1}}},{"$sort":{"_id":1}}]) :
#     pprint.pprint(item)

cursor = coll.aggregate([{"$group":{"_id":"$year","nb":{"$sum":1}}},{"$group":{"_id":"ttt","moyenne":{"$avg":"$nb"}}}])
results = list(cursor)

total_liste = len(results)
                
for i in range(total_liste):
    resultat = results[i] 
    resultat_moyenne = resultat['moyenne']
    print(colorama.Fore.YELLOW + "Le nombre moyen de publication annuelle est : " + colorama.Fore.CYAN + f"{resultat_moyenne}" + colorama.Style.RESET_ALL)
    print("-------------------------------" + colorama.Style.RESET_ALL)


# import colorama

# print(colorama.Back.WHITE + "Texte en rouge avec fond vert" + colorama.Style.RESET_ALL)

# print(colorama.Fore.CYAN + "Vous venez d'ajouter l'article " + colorama.Fore.MAGENTA + "blabla" + colorama.Fore.CYAN + " à votre bibliothèque"+ colorama.Style.RESET_ALL)

# print(colorama.Fore.LIGHTWHITE_EX + colorama.Back.LIGHTWHITE_EX + "Texte en rouge avec fond vert" + colorama.Style.RESET_ALL)

# print(colorama.Fore.RED + "A" + " " + colorama.Fore.YELLOW + "b" + colorama.Fore.GREEN + "i" + colorama.Fore.BLUE + "e" + colorama.Fore.MAGENTA + "n" + colorama.Fore.BLUE + "t" + colorama.Fore.GREEN + "ô" + colorama.Fore.YELLOW + "t" + " " + colorama.Fore.RED + "!" + colorama.Style.RESET_ALL)



