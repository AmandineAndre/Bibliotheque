#import de la BDD MongoDB
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client["my-first-db"]
coll = db['book']
import pprint

# count = coll.count_documents({})
# print(count)
# #auteur = "Surendra Dayal"
# #for item in coll.aggregate([{"$unwind":"$authors"},{"$match":{"$and":[{"authors":{"$regex":auteur}},{"year":1993}]}}]):
# #    pprint.pprint(item)

# for item in coll.distinct("year") :
#     pprint.pprint(item)

print(len(coll.distinct("authors")))
    
    



# import colorama

# print(colorama.Back.WHITE + "Texte en rouge avec fond vert" + colorama.Style.RESET_ALL)

# print(colorama.Fore.CYAN + "Vous venez d'ajouter l'article " + colorama.Fore.MAGENTA + "blabla" + colorama.Fore.CYAN + " à votre bibliothèque"+ colorama.Style.RESET_ALL)

# print(colorama.Fore.LIGHTWHITE_EX + colorama.Back.LIGHTWHITE_EX + "Texte en rouge avec fond vert" + colorama.Style.RESET_ALL)

# print(colorama.Fore.RED + "A" + " " + colorama.Fore.YELLOW + "b" + colorama.Fore.GREEN + "i" + colorama.Fore.BLUE + "e" + colorama.Fore.MAGENTA + "n" + colorama.Fore.BLUE + "t" + colorama.Fore.GREEN + "ô" + colorama.Fore.YELLOW + "t" + " " + colorama.Fore.RED + "!" + colorama.Style.RESET_ALL)



