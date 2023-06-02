from itertools import permutations

characters = ['a', 'e', 'i', 'o', 'u']
all_strings = list(permutations(characters))

for string in all_strings:
    print(''.join(string))
