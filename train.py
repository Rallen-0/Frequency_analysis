import csv
import matplotlib.pyplot as plt

'''
str_filter has an input of a string , the process filters, takes out all
letter types that aren't part of the ascii dataset, have any diacritics
or punctuation or uppercase letters,

the input IS a string and the output is a 'cleaned' string, the filter is specified to spanish text.
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

'''
clean_output_txt() applies the str_filter() function and creates
 a new file of said clean data.
'''

def clean_output_txt(file_dirty,file_clean):
    with open(file_dirty, 'r+', encoding='utf-8') as infile_eng:
        dirty_string = infile_eng.read()

    cleanstring = str_filter(dirty_string)

    with open(file_clean, "w+", encoding='utf-8') as Outfile_eng:
        Outfile_eng.write(cleanstring)

    return file_clean   


'''
dict_Find_lang(), this function takes in the input of 2 files, analyzes the length of the text,
 the count o each letter and divides one number by another. this resulting number is zipped together
 in a python dict and wrote to an outut csv file.
'''

def dict_find_lang(input_file1, input_file2, output_csv):
    
    alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    
    ################ lang 1 work #####
    
    lang1 = input("Input file 1 language (english or spanish): ")
    lang1 = lang1.lower()
    input_file1 = clean_output_txt(input(f"Input file 1 (.txt) name: "),
                                         f"{lang1}_training_AIW.txt")
    with open(input_file1) as file1:
        text1 = file1.read()
    character_count1 = len(text1) 
    
    print(f"No. of characters in {input_file1}: ", character_count1)
                                   
    #print('Count of each letter in total for file 1:')
    file_list1 = list(text1)
    word_count_list1 = []

    for i in range(97, 123):
        word_count_list1.append(file_list1.count(chr(i)))
        word_count_list1[i - 97] += 1
    word_count_list1.append(file_list1.count(chr(32)))

    word_count_dist1 = []
    for i in range(0, len(word_count_list1)):
        if character_count1 != 0:
            word_count_dist1.append(float(word_count_list1[i] / character_count1))
                                   
    ################# lang 2 work #####
                                   
    lang2 = input("Input file 2 language (english or spanish): ")
    lang2 = lang2.lower()
    input_file2 = clean_output_txt(input(f"Input file 2 (.txt) name: "),
                                         f"{lang2}_training_AIW.txt")  
    with open(input_file2) as file2:
        text2 = file2.read()
    character_count2 = len(text2)
    print(f"No. of characters in {input_file2}: ", character_count2)

    #print('Count of each letter in total for file 2:')
    file_list2 = list(text2)
    word_count_list2 = []

    for i in range(97, 123):
        word_count_list2.append(file_list2.count(chr(i)))
        word_count_list2[i - 97] += 1
    word_count_list2.append(file_list2.count(chr(32)))

    word_count_dist2 = []
    for i in range(0, len(word_count_list2)):
        if character_count2 != 0:
            word_count_dist2.append(float(word_count_list2[i] / character_count2))

    #####################                              
                                   

    data = {'Character': alpha_list, 'Distribution1': word_count_dist1, 'Distribution2': word_count_dist2}


    # Write to CSV file
    with open(output_csv, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Character', f'Distribution_{lang1}', f'Distribution_{lang2}'])
        for i in range(len(alpha_list)):
            writer.writerow([alpha_list[i], word_count_dist1[i], word_count_dist2[i]])
    print('output.csv has been created')
    plt.bar(list(alpha_list), word_count_dist1, color='b')
    
    # code to create plots, edited out as not to create duplicate plots.
    '''
        # Create subplots first
    fig, (ax_1, ax_2) = plt.subplots(1, 2, figsize=(15, 6))
    fig1 = ax_1.bar(alpha_list, word_count_dist1,
                    color='black', alpha=0.6)
    ax_1.set_title('English language distribution')
    ax_1.set_ylabel('letter odds', fontsize=13)
    # second plot
    fig2 = ax_2.bar(alpha_list, word_count_dist2,
                    color='r', alpha=0.6)
    ax_2.set_title('Spanish language distribution')
    ax_2.set_ylabel('letter odds', fontsize=13)
    legend_labels = ['English', 'Spanish']
    ax_2.legend([fig1, fig2], legend_labels)
    fig.savefig('plot.png', bbox_inches='tight')

    # Show the plot
    plt.show()
    '''
    
    
dict_find_lang('input1.txt', 'input2.txt', 'output.csv')


