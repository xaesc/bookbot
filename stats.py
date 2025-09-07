def get_num_words(text):

    splited = text.split() #Sépare chaque mot et les stock dans une list
    nb_words = len(splited) #Compte le nombre d'élements dans la liste
    return nb_words

def get_nb_car(text):
    unique = set() #Set de symbole unique
    result = {} #dictionnaire lettre : Nb occurence
    lowercase = text.lower() #Convertis toutes les lettres en minuscule
    for car in lowercase: #Identification de chaque symbole unique dans le texte en minuscule
        unique.add(car)
    for lettre in unique: #Boucle sur la liste de symbole unique
        result[lettre] = lowercase.count(lettre) #Ajout du nombre d'occurence
    return result

def get_sorted_on(nb_car):
    sorted = [] #Création de la liste
    for items in nb_car: #Iteration sur les keys dans le dictionnaire
        sorted.append({"char": items, "num": nb_car[items]}) #Ajout dans la liste au format {key : value}
    def sort_on(items): #retourne la valeur num
        return items["num"]
    sorted.sort(reverse=True, key= sort_on) #Tri en ordre décroissant d'apres la valeur num
    return sorted








