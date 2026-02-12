def menu(): #creates a menu allowing the user to chooce which operation to perform
    #input a string, reverse the string, count vowels, replace characters, analyze the string
    #use a loop to prompt the user for operations until they choose to exit
    pass

def input_gathering():  # accepts no arguements
    # prompt the user to enter a string
    # ensure the entered string is at least 5 characters long and only letters
    
    while True:
        try:  # get input from user
            my_string = input("Please enter a string: ")

            if len(my_string) < 5:  # check if string is less than 5 characters
                print("Error: String is less than 5 characters long.")
                continue

            if not my_string.isalpha():  # check if only letters
                print("Error: String is not only letters.")
                continue

            return my_string  # return valid string

        except Exception as err:
            print(f"Error: An error has occurred {err}.")


def string_reversal(my_string):  # accepts 1 arguement
    # creates a function that accepts a string as an argument and returns its reversed form.
    
    return my_string[::-1]


def character_counter(my_string):  # accepts 1 arguement my_string
    #create a function that accepts a string as an argument and returns two values;
    # the number of vowels and the number of consonants in the string.
    
    # get the vowel count
    vowel_count = count_vowels(my_string)
    
    # calculate consonants
    consonant_count = len(my_string) - vowel_count
    
    return vowel_count, consonant_count


def count_vowels(my_string):  # accepts 1 arguement
    # initlize vowels
    vowels = "aeiou"
    
    # add 1 to sum if vowel is in the string and return the sum
    return sum(1 for char in my_string.lower() if char in vowels)

#put this in menu
user_string = input_gathering()

# reverse the string
reversed_string = string_reversal(user_string)

# count vowels and consonants
vowels, consonants = character_counter(user_string)

# print results
print(f"Reversed String: {reversed_string}")
print(f"Vowel Count: {vowels}")
print(f"Consonants Count: {consonants}")

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