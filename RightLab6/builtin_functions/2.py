def count(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count


user_input = input()
upper, lower = count(user_input)
print(f"Number of uppercase letters: {upper}")
print(f"Number of lowercase letters: {lower}")
