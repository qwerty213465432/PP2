def pal(word):
    
    word = word.replace(" ", "").lower()

    return word == word[::-1]


word = input()
if pal(word):
    print(word, " is a palindrome!")
else:
    print(word, " is not a palindrome.")
