import string


def getAlfabetList():
    # Define the alphabet
    alphabet = string.ascii_lowercase
    
    # Loop through single-letter strings
    for single_letter in alphabet:
        print(single_letter)
    
    # Loop through two-letter combinations
    for first_letter in alphabet:
        for second_letter in alphabet:
            two_letter_combination = first_letter + second_letter
            print(two_letter_combination)
    
            # Add a condition to break the loop when the combination is "cc"
            if two_letter_combination == "af":
                break
    
        # Check if the condition was fulfilled to break the outer loop
        if two_letter_combination == "af":
            break
    return two_letter_combination
