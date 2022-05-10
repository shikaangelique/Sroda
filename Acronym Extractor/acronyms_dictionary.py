import os.path
import os


# acronyms_dictionary = {}


class AcronymDatabase:
    def __init__(self):
        self.acronyms_database = 'acronyms_database.txt'
        self.acronyms_dictionary = {}
        self.acronyms = []
        self.acronyms_values = []
        if not os.path.isfile(self.acronyms_database):
            with open(self.acronyms_database, 'w') as main_database:
                pass
        else:
            with open(self.acronyms_database, 'r') as main_database:
                for line in main_database:
                    self.acronyms.append(line.split()[0])
                    self.acronyms_values.append(line.partition(' ')[2].strip("\n"))
                    self.acronyms_dictionary[line.split()[0]] = line.partition(' ')[2].strip("\n")
        # print(self.acronyms_dictionary)

    def check_acronyms_database(self, acronyms):
        output = {}
        for acronym in acronyms:
            if acronym in self.acronyms_dictionary:
                output[acronym] = self.acronyms_dictionary[acronym]
            # else:
            #     output[acronym] = ""
        return output

    def add_acronyms_internally(self):
        """after the list has been generated and the extractor.py
        has found the acr and full form, it adds to db.
        extractor.py checks db before it tries to find in text"""
        with open(self.acronyms_database, "a+") as main_database:
            pass

    def add_acronyms_externally(self, external_file):
        acronyms_keys = []
        acronyms_values = []
        with open(external_file, 'r') as not_main_dict:
            for line in not_main_dict:
                word = line.split()[0]
                if word not in self.acronyms:
                    acronyms_keys.append(word.strip("!\"#$%&'*+,./:;<=>?@[\]^_`{|}~!”\n\t"))
                    acronyms_values.append(line.partition(' ')[2].strip("!\"#$%&'*+,./:;<=>?@[\]^_`{|}~!”\n\t"))

        for key in range(len(acronyms_keys)):
            self.acronyms_dictionary[acronyms_keys[key]] = acronyms_values[key]

        database_format = "{:<} {}\n"
        with open(self.acronyms_database, 'a+') as im_tired_of_names:
            for key in self.acronyms_dictionary:
                im_tired_of_names.write(database_format.format(key, self.acronyms_dictionary[key]))


# print(acronyms_dictionary_values)
# print(acronyms_dictionary_keys)
#
# print(acronyms_dictionary)

if __name__ == '__main__':
    Adams = AcronymDatabase()
    Adams.add_acronyms_externally('adams_acronym_dictionary.txt')
