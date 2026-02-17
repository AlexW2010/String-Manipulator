def menu(): #creates a menu allowing the user to chooce which operation to perform
    #input a string, reverse the string, count vowels, replace characters, analyze the string
    #use a loop to prompt the user for operations until they choose to exit
    pass

def input_gathering():#accepts no arguements
    #prompt the user to enter a string
    #esnure the entered string is at least 5 characters long and only letters
    pass

def string_reversal(user_string): #accepts no arguements
    #Create a function that accepts a string as an argument and returns its reversed form.
    reversed_string = ""
    
    for character in user_string:
        reversed_string = character + reversed_string
    
    return reversed_string

def character_counter(): #accepts no arguements
    #Create a function that accepts a string as an argument and returns two values;
    #the number of vowels and the number of consonants in the string.
    pass

def character_replacer(user_string, character_to_replace, replacement_char): #character replacer accepts no arguements
    #Create a function that replaces a specified character in the string with another character.
    #Allow the user to choose the character to replace. Return the new string.
    new_string = ""
    
    for character in user_string:
        if character == character_to_replace:
            new_string += replacement_character
        else:
            new_string += character
    
    return new_string

def string_anyalysis(): #string_anyalysis accepts no arguements
    #Create a function that accepts a string as an argument and analyzes the string and returns:
    #If the string is a palindrome
    #How many total letters in the word
    #How many vowels in the word
    #How many consonants in the word
    pass