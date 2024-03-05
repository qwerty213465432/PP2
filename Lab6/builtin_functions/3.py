def is_palindrome(s):
    
    s = s.replace(" ", "").lower()

    return s == s[::-1]

strg = input()
if is_palindrome(strg):
    print("Yes")
else:
    print("No")
