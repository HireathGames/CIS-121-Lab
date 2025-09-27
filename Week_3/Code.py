"""number = 0
while (number < 10) and (number != 8):
    number += 2
    print(number)"""
"""number = 1
while number <= 10:
    if (number % 2) == 0:
        print(number)
    number += 1"""
"""innumber = int(input("Enter number greater than 5: "))
number = 5
while (number >= 5) and (number <= innumber):
    if (number % 2) != 0:
        print(number)
    number += 1"""
"""for number in range(1, 11):
    if (number % 2) == 0:
            print(number)"""
"""for number in range(1, 11):
    if ((number//2) == (number/2)):
            print(number)"""
"""for number in range(1, 11):
    if (((number//2) - (number/2)) == 0):
            print(number)"""
"""user_number = int(input("enter a number: "))
for number in range(5, user_number+1):
    if (number % 2) == 1:
        print(number)"""
"""word = "hello world"
for letter in word:
    print(letter)"""
"""n_1 = int(input(""))
n_2 = int(input(""))
n_3 = int(input(""))
if (n_1<n_2) and (n_1<n_3):
    if (n_2<n_3):
        print(n_1, n_2, n_3)
    else:
        print(n_1, n_3, n_2)
elif (n_2<n_3):
    if (n_1<n_3):
        print(n_2, n_1, n_3)
    else:
        print(n_2, n_3, n_1)
else:
    if (n_2<n_1):
        print(n_3, n_2, n_1)
    else:
        print(n_3, n_1, n_2)"""
"""n_1 = int(input(""))
n_2 = int(input(""))
n_3 = int(input(""))
if (n_1<n_2) and (n_1<n_3):
    print(n_1)
elif (n_2<n_3):
    print(n_2)
else:
    print(n_3)"""
"""health_points = -1
race = input("Enter your race: ")
player_class = input("Enter your class: ")
if (race == "Elf") :
    if (player_class == "Warrior"):
        health_points = 150
    elif (player_class == "Bard"):
        health_points = 75
    elif (player_class == "Wizard"):
        health_points = 25
elif (race == "Ogre") :
    if (player_class == "Warrior"):
        health_points = 200
    elif (player_class == "Bard"):
        health_points = 100
    elif (player_class == "Wizard"):
        health_points = 50
print(health_points)"""
"""from random import randint
value = randint(0,1)
user_choice = input("")
if user_choice == "Heads":
    if value == 1:
        print("correct")
    else:
         print("incorrect")
elif user_choice == "Tails":
    if value == 0:
        print("correct")
    else:
         print("incorrect")"""




"""larger = float(input("Enter the larger number: "))
smaller = float(input("Enter the smaller number: "))
div_num = 0
while larger > smaller:
    larger = larger / 2
    if larger > smaller:
        div_num += 1
else:
    print(f"it can be halved {div_num} times before its smaller.")"""
"""word = input("enter a word:")
ind = 0
outword = ""
for letter in word:
    if (ind % 2) != 0:
        outword = outword + letter
    ind += 1
print(outword)"""
"""ind = 37
while ind <= 1050:
    print(ind) 
    ind += 1"""
"""word = ""
finished = False
inletter = ""
while not finished:
    inletter = input("Add letter: ")
    if inletter == "done":
        finished = True
    else:
        word = word + inletter
else: 
    print(word)"""
"""for number in range(50, 517):
    if (number % 2) != 0:
        print(number)"""
"""innumber = int(input("enter number: "))
number = 0
while innumber >= 0:
    number += innumber
    innumber = int(input("enter number: "))
else:
    print(number)"""
"""number = int(input("Enter number: "))
while number != 1:
    if (number % 2) == 0:
        number /= 2
    else:
        number = (number * 3) + 1
    print(number)"""
"""in_number = int(input("Enter Number: "))
for number in range(1, (in_number + 1)):
    if (in_number % number) == 0:
        print(number)"""
"""width = int(input("Enter width: "))
height = int(input("Enter height: "))
pattern = input("Enter pattern: ")
line = ""
for number in range(width):
    line = line + pattern
for number in range(height):
    print(line)"""
"""number = 0
biggest = 0
while number >= 0:
    number = int(input("Enter number"))
    if (number > biggest):
        biggest = number
else:
    print(biggest)"""
"""user_number = int(input("Enter number: "))
out_number = 0
for number in range(1, (user_number + 1)):
    out_number = out_number + (number ** 2)
print(out_number)"""
"""word_1 = "hello world"
count_1 = 0
for letter in word_1:
    if ((letter == "a") or (letter == "e") or (letter == "i") or (letter == "o")) or (letter == "u") or letter == "y":
        count_1 += 1
print(f"the vowel count in {word_1} is {count_1}")"""
"""def vowel_count(word):
    count = 0
    for letter in word:
        if ((letter == "a") or (letter == "e") or (letter == "i") or (letter == "o")) or (letter == "u"):
            count += 1
    return(count)
vowel_number_1 = vowel_count("hello world")
vowel_number_2 = vowel_count("apples and bananas")
vowel_number_3 = vowel_count("happy times")
vowel_total = vowel_number_1 + vowel_number_2 + vowel_number_3
print(f"total vowels seen so far is {vowel_total}")"""
"""def func(number, power):
    number = number ** power
    return(number)
print(5 * func(2, 10))
result = 5
for value in range(10):
    result *= 2
print(result)
def product(n1, n2):
    result = (n1 * n2)
    return(result)
print(product(3, 4))"""
"""L = ["Mango", "banana", 3, False, 4.5, "grapes", [9, 3, 0]]
L.append("Orange")
for ind in range(0, len(L)):
    print(L[ind])"""
"""def pyramid_volume(base, height):
    output = ((base ** 2) * height)/3
    return(output)
print(pyramid_volume(1, 2))"""
"""import math
def cone_volume(radius, height):
    output = (((radius ** 2) * height)/3) * math.pi
    return(output)
print(cone_volume(1, 2))"""
"""def baseball (p_2, p_3):
    output = (p_2 * 2) + (p_3 * 3)
    return(output)
print(baseball(5, 7))"""
"""def tennis(ace, wnsht):
    output = (ace * 2) + wnsht
    return(output)
print(tennis(1, 1))"""
"""def reverse_str(string):
    output = ""
    for number in range(1, len(string) + 1):
        output = output + string[((len(string)) - number)]
    return(output)
print("cat"[len("cat") - 1])
print(reverse_str("cat"))"""
"""def fevercheck(temperture):
    degrees = float(temperture[0 : len(temperture) - 1])
    measure = temperture[len(temperture) - 1]
    if measure == "C":
        if degrees > 37:
            return(True)
        else:
            return(False)
    elif measure == "F":
        if degrees > 98.6:
            return(True)
        else:
            return(False)
    else:
        return(False)
temp = input("Enter temperture: ")
print(f"fever = {fevercheck(temp)}") """
"""def boilingcheck(temperture):
    degrees = float(temperture[0 : len(temperture) - 1])
    measure = temperture[len(temperture) - 1]
    if measure == "C":
        if degrees >= 100:
            return(True)
        else:
            return(False)
    elif measure == "F":
        if degrees >= 212:
            return(True)
        else:
            return(False)
    else:
        return(False)"""
"""def hammdis(s_1, s_2):
    num = 0
    for ind in range(len(s_1)):
        if (s_1[ind] != s_2[ind]):
            num += 1
    return(num)
word_1 = input("Enter word: ")
word_2 = input("Enter word: ")
print(hammdis(word_1, word_2))"""
"""def isogram (word):
    storage = ""
    for letter in word:
        for l in storage:
            if l == letter:
                return(False)
        storage = storage + letter
    return(True)
word_1 = input("Enter word: ")
print(isogram(word_1))"""
"""def get_tag(word, number):
    output = word[0 : 3] + str(number)
    return(output)
w = input("Enter word: ")
n = int(input("Enter number: "))
print(get_tag(w, n))"""
"""def first_letter(sentence):
    output = ""
    for ind in range(0, len(sentence)):
        if (ind != 0):
            if (sentence[ind - 1] == " "):
                output = output + sentence[ind]
        else:
             output = output + sentence[ind]
    return(output)
print(first_letter("Hello my dear friend."))"""
"""def last_letter(sentence):
    output = ""
    for ind in range(0, len(sentence)):
        if (ind != (len(sentence) - 1)):
            if (sentence[ind + 1] == " "):
                output = output + sentence[ind]
        else :
            output = output + sentence[ind]
    return(output)
print(last_letter("magic within you"))"""
def flip_flop(word):
    output = word[(len(word)//2) : len(word)]
    output = output + word[0 : (len(word)//2)]
    return(output)
print(flip_flop("Requieum"))