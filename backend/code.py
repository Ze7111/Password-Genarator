letter_dictionary: dict = {'a': "f", 'b': "g", 'c': "h", 'd': "i", 'e': "j", 'f': "k", 'g': "l", 'h': "m", 'i': "n", 'j': "o", 'k': "p", 'l': "q", 'm': "r", 'n': "s", 'o': "t", 'p': "u", 'q': "v", 'r': "w", 's': "x", 't': "y", 'u': "z", 'v': "a", 'w': "b", 'x': "c", 'y': "d", 'z': "e", 'A': "F", 'B': "G", 'C': "H", 'D': "I", 'E': "J", 'F': "K", 'G': "L", 'H': "M", 'I': "N", 'J': "O", 'K': "P", 'L': "Q", 'M': "R", 'N': "S", 'O': "T", 'P': "U", 'Q': "V", 'R': "W", 'S': "X", 'T': "Y", 'U': "Z", 'V': "A", 'W': "B", 'X': "C", 'Y': "D", 'Z': "E"}
number_dictionary: dict = {'1': "9", '2': "0", '3': "1", '4': "2", '5': "3", '6': "4", '7': "5", '8': "6", '9': "7", '0': "8"}
special_char: dict = {'!': "%", '@': "^", '#': "&", '$': "*", '%': "(", '^': ")", '&': "!", '*': "@", '(': "#", ')': "$", '_': "-", '+': "=", '-': "_", '=': "+", '[': "{", ']': "}", '{': "[", '}': "]", ';': ":", ':': ";", "'": '"', '"': "'", ',': "<", '.': ">", '<': ",", '>': ".", '?': "/", '/': "?"}

from rich import console; print = console.Console().print
attempet = 1

class code:
    def encode(string: str):
        encoded_string: str = ""
        for char in string:
            if char in letter_dictionary:
                encoded_string += letter_dictionary[char]
            elif char in number_dictionary:
                encoded_string += number_dictionary[char]
            elif char in special_char:
                encoded_string += special_char[char]
            else:
                encoded_string += char
        return encoded_string
    
    def decode(string: str = ""):
        global attempet
        print(f"\n----------------- Password Decryption [#9770ed]{attempet} -----------------", style="#9770ed")
        print("What do you want to decode? :", style="bold red", end=" ")
        string = input("")
        decoded_string: str = ""
        for char in string:
            if char in letter_dictionary:
                decoded_string += list(letter_dictionary.keys())[list(letter_dictionary.values()).index(char)]
            elif char in number_dictionary:
                decoded_string += list(number_dictionary.keys())[list(number_dictionary.values()).index(char)]
            elif char in special_char:
                decoded_string += list(special_char.keys())[list(special_char.values()).index(char)]
            else:
                decoded_string += char
                
        print(f"Decoded string: [bold green]{decoded_string}", style="bold red")
        print("Do you want to decode another string? (y/n) :", style="bold red", end=" ")
        if input("").lower() == "y":
            attempet += 1
            code.decode()