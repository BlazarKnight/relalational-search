'''
    relalational-search
    A search algorithm that aims to search beyond the keywords.
    Copyright (C) 2024 Kai Broadbent

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>. '''

import pickle
import itertools
from dataclasses import dataclass
from collections import defaultdict
import timeit
import re
from collections import Counter

@dataclass
class datapoint:
    unique_name: str
    matrix: dict


    def name_qury(self):
        return self.unique_name
    def dict_matrix_qury(self):
        return self.matrix

    def word_ocerenses(self,look_word):
        if look_word in self.matrix:
            return (self.matrix[look_word],True)
        else:
            return(look_word,False)
    def words(self):
        return list(self.matrix)

    def __hash__(self):
        return hash(self.unique_name)

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


@dataclass
class byzdis_disubution_map:
    map:set
    def map_qurry(self):
        return self.map



@dataclass
class NullIterable:
    def __init__(self):
        pass

    def __iter__(self):
        return iter([])  # returns an empty iterator





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


def string_to_dict(fullstring,numofdoc):
    # fullstring must have all words and terms of data set in it!!!!
    data_list_split = fullstring.split()  # Split the string into a list of words

    # Count the occurrences of each word in data_list_split using a defaultdict
    word_counts = defaultdict(int)
    for word in data_list_split:
        word_counts[word] += 1

    data_list_singal = set(data_list_split)  # Remove duplicates using a set
    sorted_data_list = sorted(data_list_singal)  # Sort the list of unique words

    matrix = [(word, float(word_counts[word])/numofdoc) for word in sorted_data_list]
    return mater_dict(matrix=matrix)

def function_for_map(point1:datapoint,dict):
    relation_fromword=0
    p1_word_list=[]
    distubutinsumaslist=[]
    p1_word_list += point1.words()
    finall_map= set()
    for word in p1_word_list:



        if not dict.word_ocerenses(word)[1]:
            print('wtf',dict.word_ocerenses(word))

        else:

            ocrents_in_doc=int(point1.word_ocerenses(word)[0])
            averge_occents_in_data=dict.word_ocerenses(word)[0]
            relation_fromword += (ocrents_in_doc - averge_occents_in_data)+1
            distubutinsumaslist.append(relation_fromword)


        print(finall_map.union(set({point1.unique_name,sum(distubutinsumaslist)})))
        finall_map=finall_map.union(set([(frozenset((point1.unique_name,sum(distubutinsumaslist))))]))
        return finall_map
    else:
        return NullIterable()








def string_in_dataset_to_matrix(string_in_data):
    data_list_split = string_in_data.split()  # Split the string into a list of words

    # Count the occurrences of each word in data_list_split using a defaultdict
    word_counts = defaultdict(int)
    for word in data_list_split:
        word_counts[word] += 1

    data_list_singal = set(data_list_split)  # Remove duplicates using a set
    sorted_data_list = sorted(data_list_singal)  # Sort the list of unique words

    matrix = [(word, word_counts[word]) for word in sorted_data_list]
    return dict(matrix)  # Return the matrix of word and occurrence pairs



def string_to_datapoint_without_relations(name:str,data_as_string:str):
    point=datapoint(unique_name=name,matrix=string_in_dataset_to_matrix(data_as_string))

    return point

def main():

    relatiin_mapp_full= byzdis_disubution_map(map={})
    relatiin_mapp_full.map = {""}
    chunk_size=2000
    openfile = open('input.txt', "r")
    clean = ''
    count=0
    full_str=''
    list_of_point_names=[]
    lenchecker=0
    number_of_docs=0
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
            list_of_point_names.append(point.unique_name)
            number_of_docs+=1
            clean =''

    mat_dict= string_to_dict(full_str,number_of_docs)



    full_points_list=[]
    for pointstk in list_of_points_before_relatin_maping :


        if type(function_for_map(pointstk,mat_dict)) != NullIterable:

            bob=relatiin_mapp_full.map_qurry()
            print(bob,"bob")
            if function_for_map(pointstk,mat_dict) not in relatiin_mapp_full.map_qurry():

                if (relatiin_mapp_full.map_qurry().update(function_for_map(pointstk,mat_dict)))==None:
                    pass


                elif len(relatiin_mapp_full.map_qurry().update(function_for_map(pointstk,mat_dict)))!= len(relatiin_mapp_full.map):
                    relatiin_mapp_full.map.update({function_for_map(pon1,mat_dict)})



    print(list_of_points_before_relatin_maping,relatiin_mapp_full)
    with open("points.pickle", "wb") as file:
        pickle.dump(list_of_points_before_relatin_maping, file)
    with open("dict.pickle", "wb") as file:
        pickle.dump(mat_dict, file)
    with open("relationmap.pickle","wb") as file:
        pickle.dump(relatiin_mapp_full, file)
    print("done")




    pass


if __name__ == '__main__':
    main()


