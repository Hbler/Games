# Creates two dictionaries from user name input:
# 1. Names as _keys and and letter numbers (1..26) as _values (in a list)
# 2. Names as _keys and and letter numbers (1..9) as _values (in a list)
#   This values (1..9) represent the western/modern numerology_alphabet

# ---------------------------------------------------------------------
# ask for full name, test it, and make a list with all names as strings
# ---------------------------------------------------------------------

def name_check():
    '''Checks is there are numbers in the input.
    Breaks after three tries that contain numbers.'''

    t = 3
    while t > 0:
        full_name = raw_input('Enter your full name:\n - ')
        if any(i.isdigit() for i in full_name):
            t -= 1
            print 'You have %d tries.' % t
        elif t == 0:
            print 'No more tries!'
            break
        else:
            return full_name

def split_string(s):
    '''Creates a list of strings from a string (s) input.'''

    n_list = s.split(' ')
    return n_list

names_ls = split_string(name_check().lower())

# -----------------------------------------
# create letter - number value dictionaries
# -----------------------------------------

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# dictionary with letters as _keys and numbers from 1..26 as _values
num_dict_26 = {k:i for i,k in enumerate(alphabet, 1)}

def numerology_alphabet(string):
    '''Creates a dictionary with the string letters as _keys
    and numbers from 1..9 as _values'''

    x = 1
    n9_dict = dict()
    for i in string:
        n9_dict[i] = x
        if x == 9:
            x = 1
        else:
            x += 1
    return n9_dict

# dictionary with letters as _keys and numbers from 1..9 as _values
num_dict_9 = numerology_alphabet(alphabet)

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
                n_dict[name].append(num_dict_26[name[char]])
            else:
                n_dict[name] = [num_dict_26[name[char]]]

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
                n_dict[name].append(num_dict_9[name[char]])
            else:
                n_dict[name] = [num_dict_9[name[char]]]

    return n_dict




print name_to_num_26(names_ls)

print name_to_num_9(names_ls)
