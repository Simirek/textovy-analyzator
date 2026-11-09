registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password"
}

user_name = input("enter a user name:")
password = input("enter a password:")

if user_name in registered_users and registered_users[user_name] ==password:
    print("Hi, welcome to the app!")
    print("You can start to analyze the texts.")
else:
    print("You are not registered. Closing app.")
    exit()

texts = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

print(f"We have {len(texts)} texts to analyze.")

choice = int(input(f"Enter a number between 1 and {len(texts)}: "))

print("------------------------------")
if 1 <= choice <= len(texts):
    selected_text = texts[choice - 1]  

words = selected_text.split()
num_words = len(words)
print(f"There are {num_words} words in the selected text.")

count = 0

for word in words:
    if word[0].isupper():
        count += 1

print(f"There are {count} titlecase words.")

count = 0

for word in words:
    if word.isupper():
        count +=1

print(f"There are {count} uppercase words.")

count = 0

for word in words:
    if word.islower():
        count +=1 

print(f"There are {count} lowercase words.")

num_count = 0
total_sum = 0

for word in words:
    if word.isdigit():
        total_sum = total_sum + int(word)
        num_count += 1

print(f"There are {num_count} numeric strings.")
print(f"The sum of all numbers is {total_sum}.")

lengths = {}

for word in words:
    word_length = len(word)

    if word_length in lengths:
        lengths[word_length] += 1
    else:
        lengths[word_length] = 1

print("------------------------------")
print(f"{'LEN':>3} | {'OCCURRENCES':>15} | {'NR.':>3}")
print("------------------------------")

for length, count in lengths.items():
    stars = "*" * count
    print(f"{length:>3} | {stars:<15} | {count:>3}")

