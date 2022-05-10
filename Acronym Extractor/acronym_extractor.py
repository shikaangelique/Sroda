import os.path
import os
import string
from acronyms_dictionary import AcronymDatabase

acronyms = []


# if not os.path.isfile('my_document.txt'):
#     with open('my_document.txt', 'w') as my_file:
#         pass

# file = 'my_document.txt'


def extract_acronyms(file):
    global acronyms
    with open(file, 'r') as base_text_file:
        for line in base_text_file:
            for word in line.split():
                word = word.strip("!\"#$%&'()*+,./:;<=>?@[\]^_`{|}~!”")
                if len(word) > 1 and word[0].isupper() and word[-1].isupper():
                    if word not in acronyms:
                        acronyms.append(word)
    acronyms = sorted(acronyms)
    # print(acronyms)


def output_generated_acronyms_list():
    global acronyms
    longest_word = ""
    for word in acronyms:
        if len(word) > len(longest_word):
            longest_word = word

    line_format = "{:<} \n"
    available_acronym_format = "{:<} {} \n"

    database_check = get_full_forms_from_database(acronyms)
    main_text_check = get_full_forms_from_text(acronyms, file)

    with open('acronym_dictionary.txt', 'w') as generated_file:
        for word in acronyms:
            if word in database_check:
                generated_file.write(available_acronym_format.format(word, database_check[word]))
            else:
                generated_file.write(available_acronym_format.format(word, main_text_check[word]))
                # generated_file.write(line_format.format(word))

    update_database('acronym_dictionary.txt')

def get_full_forms_from_database(any_acronyms_list):
    database = AcronymDatabase()
    return database.check_acronyms_database(any_acronyms_list)


def find_full_form(acronym, file):
    with open(file, "r") as base_text_file:
        read_text = base_text_file.read()
        # read_text.replace("-", " ")
        # read_text = read_text.translate(str.maketrans('', '', string.punctuation))
        clean_text = ""
        comprehensive_word_list = []
        for word in read_text.split(" "):
            word = word.strip("!\"#$%&'*+,./:;<=>?@[\]^_`{|}~!”\n\t")
            word = word.replace("-", " ")
            clean_text = clean_text + word + " "
        for word in clean_text.split(" "):
            comprehensive_word_list.append(word)

    acronym_form = "(" + acronym + ")"
    full_form = ""

    a_listable = []
    acronym_index = comprehensive_word_list.index(acronym_form)
    error_offset_count = 0
    for words in range(len(acronym)):
        acronym_index = acronym_index - 1
        character = comprehensive_word_list[acronym_index]
        full_form = comprehensive_word_list[acronym_index] + " " + full_form
        a_listable.append(comprehensive_word_list[acronym_index])
        if character == "for" or character == "and" or character == "of" or character == "or":
            error_offset_count = error_offset_count + 1
    # print(a_listable)
    # print(error_offset_count)
    while error_offset_count > 0:
        for words in range(error_offset_count):
            acronym_index = acronym_index - 1
            character = comprehensive_word_list[acronym_index]
            full_form = comprehensive_word_list[acronym_index] + " " + full_form
            a_listable.append(comprehensive_word_list[acronym_index])
            error_offset_count = 0
            if character == "for" or character == "and" or character == "of" or character == "or":
                error_offset_count = error_offset_count + 1

    return full_form


def get_full_forms_from_text(any_acroynyms_list, file):
    """ Check db to see if it’s already there. If there, pull out full form from DB.
     If not, look for “(ACR)” and pull out the next len(ACR) words to the left
     of the “(ACR)” if the first letter of each word is the respective letter
     in the ACR, eurêka! """
    output = {}
    with open(file, "r") as base_text_file:
        read_file = base_text_file.read()
    for acronym in any_acroynyms_list:
        acronym_form = "(" + acronym + ")"
        if acronym_form in read_file:
            found_full_form = find_full_form(acronym, file)
            output[acronym] = found_full_form
        else:
            output[acronym] = ""
    return output


def update_database(file):
    database = AcronymDatabase()
    database.add_acronyms_externally(file)



if __name__ == '__main__':
    # file = 'my_document.txt'
    file = 'my_document.txt'
    extract_acronyms(file)
    output_generated_acronyms_list()
    # print(get_full_forms_from_database(acronyms))
    # print(acronyms)
    # print(get_full_forms_from_text(acronyms, file))
    # print(get_full_forms_from_text(acronyms, file))


