def count_letters(text):
    result={}
    # converting entire text into lowercase to count same letter once
    text=text.lower()
    
    # Go through each letter in the text
    for letter in text:
        # Check if the letter needs to be counted or not
        if letter not in result:
            result[letter]=0
        # Add or increment the value in the dictionary
        result[letter]+=1
    return result

print(count_letters("i am Ttarun kumar sharma"))
# output  {'i': 1, ' ': 4, 'a': 5, 'm': 3, 't': 2, 'r': 3, 'u': 2, 'n': 1, 'k': 1, 's': 1, 'h': 1}

