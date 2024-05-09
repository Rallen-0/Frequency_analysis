'''

These functions use the 'rand.choices()' function from the 'random' python library to choose among a list based on a set of numbers,
or 'weights' which we already have, The 'k' value is the length of string we want to generate.
'''
import random as rand
import pandas as pd

'''
importing pandas and rand for specific functions, for pandas, to easily import the csv fileand the random to import the rand.choices
this allows for the easy random choice in a list, we already have the weights, based on their distribuations.
'''
def str_filter(DirtyString):
    chars_to_remove = [';',':', '"', '-', '^', '\'',
                       ',','!','(',')','.','?',
                       '¡','¿',':','©','­']
    span_chars_remove = str.maketrans({'ñ':'n','ú':'u','í':'i',
                                       'ó':'o','«':'','»': '',
                                       'á':'a','é':'e','ã':'a'
                                       , 'â':'a'})
    CleanString = DirtyString.translate({ord(x): '' for x in chars_to_remove})
    CleanString_1 = CleanString.translate(span_chars_remove)
    CleanString = CleanString_1.lower()
    return CleanString


csv_file_path = input('enter .csv file name')  

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Create dictionaries from the DataFrame columns
# this is RE-combining the dictionary from the .csv file.
dict_eng = dict(zip(df['Character'], df['Distribution_english']))
dict_spa = dict(zip(df['Character'], df['Distribution_spanish']))


def random_eng(length):
    random_string = rand.choices(list(dict_eng.keys()),
                                 weights = list(dict_eng.values()),
                                 k = length)
    return ''.join(random_string)

def random_spa(length):
    random_string = rand.choices(list(dict_spa.keys()),
                                 weights = list(dict_spa.values()),
                                 k = length)
    return ''.join(random_string)

'''
These inputs are user controlled to say:
how long the string will be;
Which language will it be;
prints resulting psudo-language based on actual language distributions.
'''

input_length = int(input("Enter the desired length of the random string: "))
lang = str_filter(input("language to make psudo-lang (English or Spanish): "))
if lang == "english":
    random_string = random_eng(input_length)
    print("Random String of English:",'\n', random_string)
elif lang == "spanish":
    random_string = random_spa(input_length)
    print("Random String of Spanish:",'\n', random_string)
else:
    print("Error: Not a valid input language.")
