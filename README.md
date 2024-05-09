**Project #1:
Language recogniser for english and spanish.



Ensure all nesscessary libraries are installed:
Pandas,Pillow


The project is split into three python scripts:

train.py:
#INPUTS#
Input the language of the first .txt file

Input the .txt file name:
english_training_AIW.txt  or  spanish_training_AIW.txt 
(these will be in the file)

Input the language of the second .txt file

Input the .txt file name:
english_training_AIW.txt  or  spanish_training_AIW.txt 
(these will be in the file)

#OUTPUTS#
the output will be a .csv file containing the python dictionary of the english and spanish data, the name can be configured in the code but will default as 'output.csv'


test.py:

#INPUTS#

the previously generated .csv file, 'output.csv'

Text of your choice, which the code will analyze and determine which language (English or Spanish) it is closer to.

#OUTPUTS#

The detected language (English or Spanish)
and its confidence. (a percentage %)

Generate.py:

#INPUTS#

the previously generated .csv file, 'output.csv'

Length of desired psudo-lang string

language of said psudo-lang string (English or Spanish)

#OUTPUTS#

Random string of either English or Spanish.
**
