vowel=0
word = str(input("enter the word you want to calculate it's vowel:"))
option =['i', 'o', 'e', 'u', 'a']
for letter in word:
    print(letter)
    if letter in option:
        vowel+=1
        print("there's",vowel)
    else:
        print("there's no vowel in the word")
print("the vowel in the word are:",vowel)
