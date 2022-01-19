### Numerology ###
### Steps
# Create two dctionaries from the alphabet
#   One A - Z = 1 - 26
#   One A - Z = 1 - 9
# Get a name from user
# Condition the input and convert it in two corresponding dicts
# Sum all values from each dict
# Find digital root from each result
# Present infos for user

### Imports
from unicodedata import normalize
import string
import re

### Functions

def get_name():
    ''' Gets an input and checks if there are only letters'''

    done = False

    while not done:
        name = input('\nEnter your full name: ')
        if any(i.isdigit() for i in name):
            print("\nSorry that's not a valid input. Try again.")
        else:
            print('\nAlright! Thank You.')
            done = True
            return name

def condition_name(s):
    ''' Removes any accented characters and pucntuation in a string and makes it lowercase (s)
        returns a list '''
    no_accents = normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii').lower()
    return re.findall(r'[^!.? ]+', no_accents)

def name_num_9(l):

    dict9 = dict()
    val = 1
    for i in string.ascii_lowercase:
        dict9[i] = val
        if val == 9:
            val = 1
        else:
            val += 1

    new_dict = dict()
    for item in range(len(l)):
        for char in range(len(l[item])):
            name = l[item]

            if name in new_dict:
                new_dict[name].append(dict9[name[char]])
            else:
                new_dict[name] = [dict9[name[char]]]
    return new_dict

def name_num_26(l):
    ''' Creates a dict with strings from a list (l) as _keys
    and the corresponding number (1-26) as _value '''

    dict26 = {k:x for x,k in enumerate(string.ascii_lowercase, 1)}
    
    new_dict = dict()

    for item in range(len(l)):
        for char in range(len(l[item])):
            name = l[item]

            if name in new_dict:
                new_dict[name].append(dict26[name[char]])
            else:
                new_dict[name] = [dict26[name[char]]]
    
    return new_dict

def sum_key(d):
    ''' Sums the _values from a dictionary _key, an assign the result
    to the same _key in a new dict. The _values must be a list or tuple of numbers '''

    new_dict = dict()

    for key in d:
        new_dict[key] = sum(d[key])
    
    return new_dict

def all_to_one(d):
    ''' Sums all _values from a dictionary (d) '''

    total = 0

    for key in d:
        total += d[key]
    
    return total

def digital_root(n):
    ''' Finds the digital root of anumber (n) '''

    return (n - 1) % 9 + 1 if n else 0

def personality_num(d):
    ''' According to numerology is a number calculeted by the value of the consonants in the first name '''

    number = 0
    vowels = ['a','e','i','o','u']
    list_of_keys = list(d)
    counter = 0
    
    for char in list_of_keys[0]:
        if char not in vowels:
            number += d[list_of_keys[0]][counter]
        counter += 1
        
    return digital_root(number)

def soul_num(d):
    ''' According to numerology is a number calculeted by the value of the vowels in the full name '''
    number = 0 
    vowels = ['a','e','i','o','u']
    
    for key, value in d.items():
        counter = 0
        for char in key:
            if char in vowels:
                number += d[key][counter]
            counter += 1
    
    return digital_root(number)


### Execution
# Get input
user_name = get_name()
# Condition name
names_list = condition_name(user_name)
# Create dicitionaries with values for each letter of each name
name_dict_9 = name_num_9(names_list)
name_dict_26  = name_num_26(names_list)
# Sum the _values of each letter
name_dict_sum_9 = sum_key(name_dict_9)
name_dict_sum_26 = sum_key(name_dict_26)
# Sum all values into one
total9 = all_to_one(name_dict_sum_9)
total26 = all_to_one(name_dict_sum_26)
# Find the digital root of the numbers
dgrt9 = digital_root(total9)
dgrt26 = digital_root(total26)
# Find personality and soul nubers
p_num = personality_num(name_dict_9)
s_num = soul_num(name_dict_9)

# Present info to user
print('\nHere are the results:')
print(f'\nThe name: {user_name}')
print('\n\tValue of each letter 1 - 9:')
for pair in name_dict_9.items():
    print(f'\t{pair[0]}: {pair[1]}')
print(f'\n\tValue of each letter 1 - 26:')
for pair in name_dict_26.items():
    print(f'\t{pair[0]}: {pair[1]}')
print('\nTotal of each name:')
print(f'\n\t1 - 9:')
for pair in name_dict_sum_9.items():
    print(f'\t{pair[0]}: {pair[1]}')
print(f'\n\t1 - 26:')
for pair in name_dict_sum_26.items():
    print(f'\t{pair[0]}: {pair[1]}')
print('\nTotal of all names:')
print(f"\n\t{user_name} \n\tin 1 - 9: {total9}\n\tin 1 - 26: {total26}")
print(f'\tYour destiny number is: {dgrt26}\n\tYour personality number is: {p_num}\n\tYour soul number is: {s_num}')
print('\n\n Learn more with a google search "Name numerology (one of the numbers above) meaning"')
