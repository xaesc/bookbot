import sys
from stats import get_num_words, get_nb_car, get_sorted_on

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1] #Path to file in 1st argument
    text = get_book_text(path) #Return file's contents
    nb_word = get_num_words(text) #return words counts
    nb_car = get_nb_car(text) #return characters counts
    sorted_list = get_sorted_on(nb_car) #Sorts the characters byr nb of occurence

    print(
        f"============ BOOKBOT ============ \n"
        f" Analyzing book found at {path}... \n"
        f" ----------- Word Count ---------- \n"
        f" Found {nb_word} total words \n"
        f" --------- Character Count ------- \n")
    for i in range(0, len(sorted_list)):
        ligne = sorted_list[i]
        print(f"{ligne["char"]}: {ligne["num"]} \n ")
    print(f"============= END ===============")
    
main()
        
