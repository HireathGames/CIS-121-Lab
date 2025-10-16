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
"""def flip_flop(word):
    output = word[(len(word)//2) : len(word)]
    output = output + word[0 : (len(word)//2)]
    return(output)
print(flip_flop("Requieum"))"""
"""days_of_week = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
work_days = list(days_of_week[0 : 5])"""
"""def getwords (sentence):
    words = []
    last_pos = 0
    for index in range(0, len(sentence)):
        if index != (len(sentence) - 1):
            if sentence[index] == " ":
                words.append(sentence[last_pos : index])
                last_pos = index + 1
        else:
            words.append(sentence[last_pos : index + 1])
            return(words)
sen = input("Enter sentence: ")
print(getwords(sen))"""
"""def getwords (sentence):
    words = []
    last_pos = 0
    for index in range(0, len(sentence)):
        if index != (len(sentence) - 1):
            if sentence[index] == " ":
                vow = 0
                for letter in sentence[last_pos : index] :
                    if letter in "aeiou":
                        vow += 1
                if vow >= 2:
                    words.append(sentence[last_pos : index])
                last_pos = index + 1
        else:
            vow = 0
            for letter in sentence[last_pos : index] :
                if letter in "aeiou":
                    vow += 1
            if vow >= 2:
                    words.append(sentence[last_pos : index + 1])
            return(words)
sen = input("Enter sentence: ")
print(getwords(sen))"""
"""def letter_counter(sentence):
    letter_number = {}
    for letter in sentence:
        if letter in letter_number:
            letter_number[letter] += 1
        else:
            letter_number[letter] = 1
    return(letter_number)
print(letter_counter("something wicked this way comes"))"""
"""def everyotherlet (word):
    output = []
    evot = True
    for letter in word:
        if evot:
            output.append(letter)
        evot = not evot
    return(output)
print(everyotherlet("counterattack"))"""
"""def evenbetween(low, high):
    even_letters = []
    for num in range(low, high + 1):
        if (num % 2) == 0:
            even_letters.append(num)
    return(even_letters)
print(evenbetween(1, 2000))"""
"""def evenbetween(low, high):
    even_letters = []
    for num in range(low, high + 1):
        if (num % 2) != 0:
            even_letters.append(num)
    return(even_letters)
print(evenbetween(1, 2000))"""
"""def hailstone(n):
    num = n
    sequ = [num]
    while num != 1:
        if (num % 2) == 0:
            num /= 2
            sequ.append(num)
        else:
            num = (num * 3) + 1
            sequ.append(num)
    else:
        sequ.append(num)
        return(sequ)
print(hailstone(25))"""
"""def factorfinder (n):
    factors = []
    for num in range(1, n + 1):
        if (n % num) == 0:
            factors.append(num)
    return(factors)
print(factorfinder(12))"""
"""def smalbig(n1, n2, n3):
    if (n1 < n2 < n3): return([n1, n2, n3])
    if (n1 < n3 < n2): return([n1, n3, n2])
    if (n2 < n1 < n3): return([n2, n1, n3])
    if (n2 < n3 < n1): return([n2, n3, n1])
    if (n3 < n1 < n2): return([n3, n1, n2])
    if (n3 < n2 < n1): return([n3, n2, n1])
print(smalbig(3, 1, 2))"""
"""def bigsmal(n1, n2, n3):
    if (n1 > n2 > n3): return([n1, n2, n3])
    if (n1 > n3 > n2): return([n1, n3, n2])
    if (n2 > n1 > n3): return([n2, n1, n3])
    if (n2 > n3 > n1): return([n2, n3, n1])
    if (n3 > n1 > n2): return([n3, n1, n2])
    if (n3 > n2 > n1): return([n3, n2, n1])
print(bigsmal(3, 1, 2))"""
"""def blackjack(count):
    pos = [2, 3, 4, 5, 6]
    neg = [10, "j", "q", "k", "a"]
    score = 0
    for card in count:
        if (card in pos):
            score += 1
        elif (card in neg):
            score -= 1
    return(score)
print(blackjack([2, "j", "a", 6, 8, 9, 10, 3, 4, 2]))"""
"""def even_or_odd(numbers):
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if (num % 2) == 0:
            even_sum += num
        else:
            odd_sum += num
    if (even_sum > odd_sum):
        return("even")
    elif(even_sum < odd_sum):
        return("odd")
    else :
        print("tie")
print(even_or_odd([4, 2, 3, 3]))"""
"""def add_lists(fl, sl):
    output = []
    for ind in range(0, len(fl)):
        output.append(fl[ind] + sl[ind])
    return(output)"""
"""def largest_even(numbers):
    largest = 0
    for num in numbers:
        if (num % 2) == 0:
                if num > largest:
                    largest = num
    return(largest)
print(largest_even([3, 7, 2, 1, 7, 9, 10, 13]))
def largest_odd(numbers):
    largest = 0
    for num in numbers:
        if (num % 2) != 0:
                if num > largest:
                    largest = num
    return(largest)
print(largest_odd([3, 7, 2, 1, 7, 9, 10, 13]))"""
"""def progress_days(miles):
    progress = 0
    for ind in range(0, len(miles)):
        if ind != 0:
            if miles[ind] > miles[ind - 1]:
                progress += 1
    return progress
print(progress_days([10, 11, 12, 9, 10]))
def falter_days(miles):
    falter = 0
    for ind in range(0, len(miles)):
        if ind != 0:
            if miles[ind] < miles[ind - 1]:
                falter += 1
    return falter
print(falter_days([10, 11, 12, 9, 10]))"""
"""def like_calc(presses):
    status = "nothing"
    for pre in presses:
        if pre == "like":
            if status == "like":
                status = "nothing"
            else:
                status = "like"
        elif pre == "dislike":
            if status == "dislike":
                status = "nothing"
            else:
                status = "dislike"
    return status
print(like_calc(["like", "like", "dislike", "like"]))"""
"""def occurence_Checker(items, key):
    occ = []
    for ind in range(0, len(items)):
        if items[ind] == key:
            occ.append(ind)
    return occ
print(occurence_Checker([1, 5, 5, 2, 7], 5))"""
"""def multi_list (base, length):
    multi = []
    for num in range(1, length + 1):
        multi.append(base * num)
    return(multi)
print(multi_list(12, 10))"""
"""def match_first_letter(acro, words):
    if len(acro) == len(words):
        for ind in range(len(acro)):
            if acro[ind] != words[ind][0]:
                return False
        else:
            return True
    else:
        return False
print(match_first_letter("ngguoy", ["never", "gonna", "give", "up", "on"]))"""

"""grid = {"A" : [1, 2, 3], "B" : [1, 2, 3], "C" : [1, 2, 3]}
simplegrid = []
for key in grid:
    simplegrid.append(grid[key])
print(simplegrid)"""
"""def is_isogram (word):
    letters = {}
    for letter in word:
        for key in letters:
            if key == letter:
                return(False)
        else:
            letters[letter] = 0
    else:
        return(True)
print(is_isogram("Smash"))"""
"""def unique_number (numbers):
    occurences = {}
    for num in numbers:
        if num in occurences.keys():
            occurences[num] += 1
        else:
            occurences[num] = 1
    for key, val in occurences.items():
        if val==1:
            return key
print(unique_number([0, 1, 2, 3, 3, 0, 2]))"""
"""def unique_number (numbers):
    occurences = {}
    for num in numbers:
        if num in occurences.keys():
            occurences[num] += 1
        else:
            occurences[num] = 1
    output = []
    for key, val in occurences.items():
        if val==1:
            output.append(key)
    return(output)
print(unique_number([0, 1, 2, 3, 3, 0, 2, 4]))"""
"""def ID_to_name(IDs_Names):
    outputs = []
    for key, val in IDs_Names.items():
        outputs.append(val)
    return(outputs)
print(ID_to_name({90193 : "bob", 1840293 : "john"}))"""
"""def find_oldest (people):
    oldest_age = 0
    oldest_name = ""
    for name, age in people.items():
        if age > oldest_age:
            oldest_age = age
            oldest_name = name
    return(oldest_name)
print(find_oldest({"John" : 18, "Bob" : 60, "Lisa" : 20, "Gerret" : 64}))"""
"""def letter_count(word):
    let_nums = {}
    for letter in word:
        if letter in let_nums:
            let_nums[letter] += 1
        else:
            let_nums[letter] = 1
    return(let_nums)
print(letter_count("Hello"))"""
"""def min_course (courses):
    min_key = ""
    min_num = -1
    for key, num in courses.items():
        if (num < min_num) or (min_num == -1):
            min_num = num
            min_key = key
    return(min_key)
print(min_course({"art" : 90, "music" : 92, "drama" : 89}))"""
"""def find_youngest(people):
    youngest_age = -1
    youngest_name = ""
    for name, age in people.items():
        if (age < youngest_age) or (youngest_age == -1):
            youngest_age = age
            youngest_name = name
    return(youngest_name)
print(find_youngest({"John" : 22, "Bob" : 60, "Lisa" : 20, "Gerret" : 64}))"""
"""def get_cost(receipt):
    total = 0
    for product, cost in receipt.items():
        total += cost
    return(total)
print(get_cost({"John" : 22, "Bob" : 60, "Lisa" : 20, "Gerret" : 64}))"""
"""def print_menu(menu):
    for dish in menu:
        print(f"{dish} costs {menu[dish]}.")
print_menu({"burger" : 10, "fries" : 4, "soda" : 3})"""
"""def find_repeats(elements):
    output = {}
    for elem in elements:
        if (elem in output.keys()):
            output[elem] += 1
        else:
            output[elem] = 1
    return(output)
print(find_repeats([1, 3, 3, 3, 1, 2, 5, 5]))"""
"""def find_sales(products):
    total = 0
    for pro in products:
        total += products[pro]
    return(total)
print(find_sales({"burger" : 10, "fries" : 5, "soda" : 3}))"""
"""def salary_checker(employee_sal, target_sal):
    target_employees = []
    for emp in employee_sal:
        if employee_sal[emp] > target_sal:
            target_employees.append(emp)
    return(target_employees)
print(salary_checker({"John" : 180000, "Bob" : 60000, "Lisa" : 200000, "Gerret" : 64000}, 100000))"""
"""def donation_addition(doners):
    total = 0
    for doner in doners:
        total += doners[doner]
    return(total)
print(donation_addition({"John" : 18, "Bob" : 60, "Lisa" : 20, "Gerret" : 64}))"""
"""def fruit_calorie_counter(fruits):
    calories = {"Apple" : 95, "Banana" : 105, "Orange" : 62, "Grape" : 3, "Pear" : 102}
    total = 0
    for fruit in fruits:
        total += calories[fruit]
    return(total)
print(fruit_calorie_counter(["Apple", "Apple", "Orange", "Grape"]))"""
"""def majority_element(elements):
    occurences = {}
    for elem in elements:
        if elem in occurences.keys():
            occurences[elem] += 1
        else:
            occurences[elem] = 1
    majority = elements[0]
    for key in occurences:
        if (occurences[majority] < occurences[key]):
            majority = key
    return(majority)
print(majority_element([3,2,3]))"""
dic = {1 : 3, 2 : 3}
if 2 in dic.keys():
    print("n")