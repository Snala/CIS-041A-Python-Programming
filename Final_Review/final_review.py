import re

'''
Question 1:
'''


def square_it(n):
    return n*n


the_numbers = (11, 92, 68, 4, 5, 9)

the_result = map(square_it, the_numbers)

print(*the_result, sep='\n')


'''
Question 2:
'''

find_the_numbers = "De Anza College, 21250 Stevens Creek Blvd., Cupertino, 95014"

found = re.findall(r'\d+', find_the_numbers)

print(found)

'''
Question 3:
'''

data = 'Diane\'s birthday is April 25, Kristin\'s birthday is June 1, Wayne\'s birthday is September 27 '
dictionary_data = dict()
data = data.split(',')
for i in data:
    pre_dictionary = i.split('\'s birthday is ')
    dictionary_data[pre_dictionary[0].strip()] = pre_dictionary[1].strip()
print(dictionary_data)
