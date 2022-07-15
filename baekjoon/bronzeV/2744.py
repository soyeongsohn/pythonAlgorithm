word = input()
new_word = ""
for i in word:
    if i.islower():
        new_word += i.upper()
    else:
        new_word += i.lower()

print(new_word)