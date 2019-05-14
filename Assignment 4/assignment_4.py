import csv


class MorseCode:
    def __init__(self, value, key):
        self.value = value
        self.key = key

    def __eq__(self, right_character):
        return self.value == right_character.value

    def __lt__(self, right_character):
        return self.value < right_character.value


if __name__ == '__main__':
    # The sentence that we will be interpreting
    sentence = 'THE QUICK BROWN POODLE JUMPED OVER THE LAZY FOX 123 TIMES'

    with open('MorseCode.csv', 'r') as csv_file:
        csv_output = csv.reader(csv_file, delimiter=',')
        list_of_characters = []
        for row in csv_output:
            key = row[0]
            value = row[1]
            bob = MorseCode(key, value)
            list_of_characters.append(bob)

    # First we sort the list
    list_of_characters.sort()
    # Let's print them each out.
    [print(item.value) for item in list_of_characters]

    # Print out the sentence
    for character in sentence:
        character = character.upper()
        try:
            index = list_of_characters.index(MorseCode(character, ''))
            print(list_of_characters[index].key, end='')
        except ValueError:
            print(' ', end='')
