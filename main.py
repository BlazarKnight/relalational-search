import itertools
from dataclasses import dataclass
from collections import defaultdict
import timeit



@dataclass
class datapoint:
    unique_name: str
    matrix: list
    relation_map: dict
    def name_qury(self):
        return self.unique_name
    def dict_matrix_qury(self):
        return self.matrix
    def relation_map_qury(self):
        return self.relation_map
    def word_ocerenses(self,look_word):
        send = ()
        for tupl in self.matrix:

            if look_word in tupl:
                send += (tupl[1], True, look_word)
        if len(send)>0:
            return send
        else:
            return(0,False)
    def words(self):
        words=[]
        for tupl in self.matrix:
            words.append(tupl[0])
        return words

@dataclass
class mater_dict:

    matrix:list

    def words(self):
        words = []
        for tupl in self.matrix:
            words.append(tupl[0])
        return words


    def word_ocerenses(self,look_word):
        send=()
        for tupl in self.matrix:

            if look_word in tupl:
                send += (tupl[1], True, look_word)
        return send



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
        lineclean = lineclean.lower()
        clean = clean + lineclean
    return clean


def string_to_dict(fullstring):
    # fullstring must have all words and terms of data set in it!!!!
    data_list_split = fullstring.split()  # Split the string into a list of words

    # Count the occurrences of each word in data_list_split using a defaultdict
    word_counts = defaultdict(int)
    for word in data_list_split:
        word_counts[word] += 1

    data_list_singal = set(data_list_split)  # Remove duplicates using a set
    sorted_data_list = sorted(data_list_singal)  # Sort the list of unique words

    matrix = [(word, word_counts[word]) for word in sorted_data_list]
    return mater_dict(matrix=matrix)

def function_for_map(point1:datapoint,point2:datapoint,dict):
    relation_fromword=0
    p1_word_list=[]
    p1_word_list += point1.words()

    for word in p1_word_list:

        if not dict.word_ocerenses(word)[1]:
            print('wtf',dict.word_ocerenses(word))

        if len(remove_duplicates(point1.words()+point2.words()))>0 and point2.word_ocerenses(word)[1]  :
            print('.')
            combind_ocrents=(point2.word_ocerenses(word)[0]+point1.word_ocerenses(word)[0])
            total_occents_in_data=dict.word_ocerenses(word)[0]
            relation_fromword += (combind_ocrents / total_occents_in_data)+1


        elif point2.word_ocerenses(word)[1] and dict.word_ocerenses(word)[1]:
            print('what the hell',bools)
            break
    try:
        print(relation_fromword)

        return relation_fromword
    except(TypeError):
        return relations








def string_in_dataset_to_matrix(string_in_data):
    data_list_split = string_in_data.split()  # Split the string into a list of words

    # Count the occurrences of each word in data_list_split using a defaultdict
    word_counts = defaultdict(int)
    for word in data_list_split:
        word_counts[word] += 1

    data_list_singal = set(data_list_split)  # Remove duplicates using a set
    sorted_data_list = sorted(data_list_singal)  # Sort the list of unique words

    matrix = [(word, word_counts[word]) for word in sorted_data_list]
    return matrix  # Return the matrix of word and occurrence pairs



def string_to_datapoint_without_relations(name:str,data_as_string:str):
    point=datapoint(unique_name=name,matrix=string_in_dataset_to_matrix(data_as_string),relation_map=None)

    return point

def main():
    import re
    start = timeit.default_timer()
    chunk_size=500
    openfile = open('input.txt', "r")
    clean = ''
    count=0
    full_str=''
    list_of_points_before_relatin_maping=[]
    for line in openfile:
        count += 1
        # for symbol in ["\n",':','.',"'",'&','-']:
        lineclean = re.sub(r'[^\w\s]', '', line)
        lineclean = lineclean.replace("\n", " ")
        lineclean = lineclean.lower()
        clean = clean + lineclean
        full_str= full_str + lineclean
        if count % chunk_size==0:
            point=string_to_datapoint_without_relations(f'lines{count-chunk_size}-{count}',clean)
            list_of_points_before_relatin_maping.append(point)
            clean =''

    mat_dict= string_to_dict(full_str)
    print(mat_dict)

    full_points_list=[]
    for pointstk in list_of_points_before_relatin_maping:
        relation_map_as_list = []
        for pon in list_of_points_before_relatin_maping:

            if pointstk != pon and len(set( pon.matrix + pointstk.matrix))<len(pon.matrix+pointstk.matrix):
                relation_map_as_list += [[pon.name_qury(),function_for_map(pointstk,pon,mat_dict)]]


                bo=True
            else:
                bo=False
            if bo and pointstk.relation_map != dict(relation_map_as_list) :
                pointstk.relation_map=dict(relation_map_as_list)
                full_points_list.append(pointstk)

    print(full_points_list)





    pass


if __name__ == '__main__':
    main()


