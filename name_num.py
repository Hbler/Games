# Creates two dictionaries from user name input:
# 1. Names as _keys and and letter numbers (1..26) as _values (in a list)
# 2. Names as _keys and and letter numbers (1..9) as _values (in a list)
#   This values (1..9) represent the western/modern numerology_alphabet

# -------
# imports
# -------

from unicodedata import normalize # for accents removal

# -------------------------------------------
# ask for full name, test it, remove accents,
# and make a list with all names as strings.
# -------------------------------------------

def name_check():
    '''Checks is there are numbers in the input.
    Breaks after three tries that contain numbers.'''

    t = 3
    while t > 0:
        name = raw_input('Enter your full name:\n - ')
        if any(i.isdigit() for i in name):
            t -= 1
            print 'You have %d tries.' % t
        elif t == 0:
            print 'No more tries!'
            break
        else:
            return name

def split_string(s):
    '''Creates a list of strings from a string (s) input.'''

    n_list = s.split(' ')
    return n_list

def remv_accent(s):
    '''Removes any accented character in the string (s)'''

    return normalize('NFKD', s.decode('utf-8')).encode('ascii', 'ignore')

full_name = name_check()

full_name_no_accents = remv_accent(full_name)

names_ls = split_string(full_name_no_accents.lower())

# -----------------------------------------
# create letter - number dictionaries
# -----------------------------------------

alphabet = 'abcdefghijklmnopqrstuvwxyz'

num_dict26 = {k:i for i,k in enumerate(alphabet, 1)}
# dictionary with letters as _keys and numbers from 1..26 as _values

def numerology_alphabet(s):
    '''Creates a dictionary with the string letters as _keys
    and numbers from 1..9 as _values'''

    x = 1
    n9_dict = dict()
    for i in s:
        n9_dict[i] = x
        if x == 9:
            x = 1
        else:
            x += 1
    return n9_dict

num_dict9 = numerology_alphabet(alphabet)
# dictionary with letters as _keys and numbers from 1..9 as _values

# -----------------------------------
# convert names list in numeric lists
# -----------------------------------

def name_to_num_26(l):
    '''Creates a dictionary with strings from a list (l) as _keys
    and a list of numbers (1..26) representing each letter as _values
    for each string.'''

    n_dict = dict()

    for i in range(len(l)):
        for char in range(len(l[i])):
            name = l[i]

            if name in n_dict:
                n_dict[name].append(num_dict26[name[char]])
            else:
                n_dict[name] = [num_dict26[name[char]]]

    return n_dict

def name_to_num_9(l):
    '''Creates a dictionary with strings from a list (l) as _keys
    and a list of numbers (1..9) representing each letter as _values
    for each string.'''

    n_dict = dict()

    for i in range(len(l)):
        for char in range(len(l[i])):
            name = l[i]

            if name in n_dict:
                n_dict[name].append(num_dict9[name[char]])
            else:
                n_dict[name] = [num_dict9[name[char]]]

    return n_dict

name_dict26 = name_to_num_26(names_ls)

name_dict9 = name_to_num_9(names_ls)

# -------------------
# derivatives numbers
# -------------------

def sum_dictionary_keys(d):
    '''Sums a _value of a dictionary (d), and assingn the result to the same
    _key in a new dictionary. The _value must be a list or tuple with numbers.'''

    sum_k = dict()

    for k in d:
        sum_k[k] = sum(d[k])

    return sum_k

sdk26 = sum_dictionary_keys(name_dict26)

sdk9 = sum_dictionary_keys(name_dict9)

def keys_to_one(d):
    '''Sums the _values of the _keys in a dictionary (d) in variable (n).'''

    n = 0

    for k in d:
        n += d[k]

    return n

kto26 = keys_to_one(sdk26)

kto9 = keys_to_one(sdk9)

def digital_root(n):
    '''Find the digital root of a number (n).'''

    dig_rt = n - (9 * ((n - 1) / 9))
    return dig_rt

dr26 = digital_root(kto26)

dr9 = digital_root(kto9)

# ----------------
# printing results
# ----------------

print
print full_name_no_accents
print
print names_ls
print

# number ranging from 1..26
print name_dict26
print
print sdk26
print
print kto26
print
print dr26
print

# number ranging from 1..9
print name_dict9
print
print sdk9
print
print kto9
print
print dr9
