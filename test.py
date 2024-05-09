'''
The 2 dictionaries 'dict_spa' and 'dict_eng' are generated from the code above just 'trained' on a large dataset,
code can be combined later, this is for testing purposes.
'''
import math
import pandas as pd

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

csv_file_path = input('enter \'.csv\' file name: ') 
# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Create dictionaries from the DataFrame columns
dict_eng = dict(zip(df['Character'], df['Distribution_english']))
dict_spa = dict(zip(df['Character'], df['Distribution_spanish']))


input_word = str_filter(input('Enter text to analyzse language : '))
input_word = list(input_word.lower())                   # Takes input text and converts to list.



# func for find prob of each language

dict_list_eng_word = []                                 # Initialises empty lists to be filled later
dict_list_spa_word = []


for i in range(0,len(input_word)):                      # the following 2 'for' loops take the 'values' for a given letter list  and adds it to seperate list
    for k, v in dict_eng.items():
        if k == input_word[i]:
            dict_list_eng_word.append(round(v,4))

            
for i in range(0,len(input_word)):
    for k, v in dict_spa.items() :
        if k == input_word[i]:
            dict_list_spa_word.append(round(v,4))

            


prob_word_spa = math.prod(dict_list_spa_word)         # Find the product of the given letter list's values.
prob_word_eng = math.prod(dict_list_eng_word)

Total_prob = prob_word_spa + prob_word_eng            # "Normalises" the values by finding the total prob and dividing each list prob by it
Normal_spa_wordprob = prob_word_spa / Total_prob      # Normalisation can let us see a value between 0 and 1 (or mutliplied to find a %)
Normal_eng_wordprob = prob_word_eng / Total_prob

# Set confidence, this can be set to be stricter ( a higher value ) or more leinient ( lower value) 
confidence = 0.7

# Determine the language and confidence level by seeing which values are higher and above the confidence level, if neither is reached, string is 'Not confident enough'
if Normal_spa_wordprob > confidence and Normal_spa_wordprob > Normal_eng_wordprob:
    prob_lang = 'Spanish'
    confidence = Normal_spa_wordprob
    confidence *= 100
elif Normal_eng_wordprob > confidence and Normal_eng_wordprob > Normal_spa_wordprob:
    prob_lang = 'English'
    confidence = Normal_eng_wordprob
    confidence *= 100
else:
    prob_lang = 'Not confident enough to determine.'
    confidence = max(Normal_spa_wordprob, Normal_eng_wordprob)
    confidence *= 100

print(f'Detected Language: {prob_lang}')
print(f'Confidence: {confidence:.2f} %')
