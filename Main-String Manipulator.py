def menu(): #accepts no arguements
    # this function shows a menu and lets the user choose what to do
    # it keeps running until the user chooses to exit

    # keep showing the menu until the user exits
    while True:

        print("\nMenu:")
        print("1. Reverse String")
        print("2. Count Vowels and Consonants")
        print("3. Replace Character")
        print("4. Analyze String")
        print("5. Exit")

        # get the user's choice
        choice = input("Please choose an option (1-5): ")

        # if the user chooses to reverse a string
        if choice == "1":
            # get a valid string from the user
            user_string = input_gathering()

            # reverse the string
            reversed_string = string_reversal(user_string)

            # display the result
            print(f"Reversed String: {reversed_string}")

        # if the user chooses to count vowels and consonants
        elif choice == "2":
            # get a valid string
            user_string = input_gathering()

            # count vowels and consonants
            vowels, consonants = character_counter(user_string)

            # display results
            print(f"Vowel Count: {vowels}")
            print(f"Consonants Count: {consonants}")

        # if the user chooses to replace a character
        elif choice == "3":
            # call the character replacer function
            new_string = character_replacer()

            # show the updated string
            print(f"Updated String: {new_string}")

        # if the user chooses string analysis
        elif choice == "4":
            # call the string analysis function
            string_anyalysis()

        # if the user chooses to exit
        elif choice == "5":
            print("Exiting program.")
            break

        # if the user enters an invalid option
        else:
            print("Invalid choice. Please select 1-5.")

def input_gathering(): #accepts no arguements
    # this function asks the user to enter a string
    # the string must be at least 5 letters long and contain only letters

    while True:
        try:
            # ask the user to enter a string
            my_string = input("Please enter a string: ")

            # check if the string is too short
            if len(my_string) < 5:
                print("Error: String is less than 5 characters long.")
                continue

            # check if the string contains only letters
            if not my_string.isalpha():
                print("Error: String is not only letters.")
                continue

            # return the valid string
            return my_string

        except Exception as err:
            print(f"Error: An error has occurred {err}.")

def string_reversal(my_string): #string_reversal accepts my_string
    # this function takes a string and returns it reversed

    # reverse the string using slicing
    return my_string[::-1]

def character_counter(my_string): #character_counter accepts my_string
    # this function counts vowels and consonants in a string
    # it returns both values

    # count vowels
    vowel_count = count_vowels(my_string)

    # count consonants by subtracting vowels from total length
    consonant_count = len(my_string) - vowel_count

    # return both counts
    return vowel_count, consonant_count



def count_vowels(my_string):#count_vowels accepts my_string
    # this function counts how many vowels are in the string

    # store all vowels
    vowels = "aeiou"

    # count each character that is a vowel
    return sum(1 for char in my_string.lower() if char in vowels)



def character_replacer(): #accepts no arguements
    # this function replaces one character in the string with another

    # get a valid string from the user
    my_string = input_gathering()

    while True:
        # ask which character to replace
        old_char = input("Enter the character you want to replace: ")

        # ask for the new character
        new_char = input("Enter the new character: ")

        # make sure both inputs are single letters
        if len(old_char) != 1 or len(new_char) != 1:
            print("Error: Please enter only single characters.")
            continue

        if not old_char.isalpha() or not new_char.isalpha():
            print("Error: Characters must be letters.")
            continue

        # make sure the character exists in the string
        if old_char not in my_string:
            print("Error: Character not found in string.")
            continue

        # replace the character
        new_string = my_string.replace(old_char, new_char)

        # return the updated string
        return new_string



def string_anyalysis(): #accepts no argueemnts
    # this function analyzes the string
    # it checks if it is a palindrome
    # it counts total letters, vowels, and consonants

    # get a valid string
    my_string = input_gathering()

    # check if the string is a palindrome
    is_palindrome = my_string.lower() == my_string[::-1].lower()

    # count total letters
    total_letters = len(my_string)

    # count vowels and consonants
    vowels, consonants = character_counter(my_string)

    # display the results
    print(f"Is Palindrome: {is_palindrome}")
    print(f"Total Letters: {total_letters}")
    print(f"Vowel Count: {vowels}")
    print(f"Consonants Count: {consonants}")




