from dataclasses import dataclass
@dataclass
class datapoint
    unique_name: str
    dict_matrix: list
    relation_map: dict


def remove_duplicates(lst):
    #seen = []
    #return [x for i, x in enumerate(lst) if x not in seen or not seen.append(x)]
    from collections import OrderedDict

    #my_list = [1, 2, 3, 2, 4, 3, 5]
    unique_items = list(OrderedDict.fromkeys(lst))
    return  unique_items

def file_to_clean_str(file):
    import re
    openfile = open(file,"r")
    clean = ''
    for line in openfile:
            #for symbol in ["\n",':','.',"'",'&','-']:
        lineclean =  re.sub(r'[^\w\s]', '', line)
        lineclean = lineclean.replace("\n"," ")
        clean = clean + lineclean
    return clean


def string_to_dict(fullstring):
    # fullstring must have all words and terms of data set in it!!!!

    split_string = fullstring.split()
    single_list= remove_duplicates(split_string)
    sorted_list= sorted(single_list)
    return sorted_list

def string_in_dataset_to_matrix(string_in_data,datadict):
    data_list_split= string_in_data.split()
    data_list_singal= remove_duplicates(data_list_split)


def main():
    pass
if __name__ == '__main__':
    string_to_dict(file_to_clean_str('input.txt'))
    print(file_to_clean_str('input.txt'))
    #print(file_to_dict('input.txt', 'bitdit'))
    #print(seter())

