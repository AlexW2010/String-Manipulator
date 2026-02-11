def menu(): #creates a menu allowing the user to chooce which operation to perform
    #input a string, reverse the string, count vowels, replace characters, analyze the string
    #use a loop to prompt the user for operations until they choose to exit
    pass

def input_gathering():#accepts no arguements
    #prompt the user to enter a string
    #esnure the entered string is at least 5 characters long and only letters
    try: #get input from user
        my_string = input("Please enter a string: ")

        if len(my_string) < 5:  # check if string is less than 5 characters
            print("Error: String is less than 5 characters long.")

        if not my_string.isalpha():  # check if only letters
            print("Error: String is not only letters.")

    except Exception as err:
        print(f"Error: An error has occurred {err}.")
        
    return my_string

def string_reversal(): #accepts no arguements
    #Create a function that accepts a string as an argument and returns its reversed form.
    pass

def character_counter(my_string): #accepts 1 arguement my_string
    #Create a function that accepts a string as an argument and returns two values;
    #the number of vowels and the number of consonants in the string.
    
    my_string = input_gathering()
    
    #get the vowel count
    vowel_count = count_vowels(my_string)
    
    #calculate consonants
    consonant_count = len(my_string) - vowel_count
    
    #print out vowels and consonansts count
    print(f"Vowel Count: {vowel_count}")
    print(f"Consonants Count: {consonant_count}")
    
def count_vowels(my_string):# accepts 1 arguements
    #initlize vowels
    vowels = "aeiou"
    
    #add 1 to sum if vowel is in the string and return the sum
    return sum(1 for char in my_string if char in vowels)

def character_replacer(): #character replacer accepts no arguements
    #Create a function that replaces a specified character in the string with another character.
    #Allow the user to choose the character to replace. Return the new string.
    pass

def string_anyalysis(): #string_anyalysis accepts no arguements
    #Create a function that accepts a string as an argument and analyzes the string and returns:
    #If the string is a palindrome
    #How many total letters in the word
    #How many vowels in the word
    #How many consonants in the word
    pass