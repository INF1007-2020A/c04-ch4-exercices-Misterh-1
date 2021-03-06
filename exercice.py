#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    x = len(string) % 2
    if x == 0 :
        return True
    else :
        return False


def remove_third_char(string: str) -> str:
    new_word = ""
    for i in range (len(string)) :
        if i != 2 :
            new_word += string[i]
    return new_word


def replace_char(string: str, old_char: str, new_char: str) -> str:
    new_string = ""
    for i in range (len(string)):
        if string[i] == old_char :
            new_string += new_char
        else :
            new_string += string[i]
    return new_string


def get_number_of_char(string: str, char: str) -> int:
    counter = 0
    for character in string:
        if character == char :
            counter +=1 
    return counter


def get_number_of_words(sentence: str, word: str) -> int:
     counter = 0
     liste_words = sentence.split(" ")
     for mot in liste_words :
        if mot == word:
                counter += 1
     return counter


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello world est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
