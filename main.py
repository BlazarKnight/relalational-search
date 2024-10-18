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

from userpath.cli import append


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
        dictofm=dict(self.matrix)
        return tuple(dictofm.keys())

    def __hash__(self):
        return hash(self.unique_name)

@dataclass
class mater_dict:

    matrix:list

    def words(self):

        return [x[0] for x in self.matrix]


    def word_ocerenses(self,look_word):
        send=()
        k=[x[0] for x in self.matrix]
        for tupl in self.matrix:

            if look_word in tupl:
                send = (tupl[1], True, look_word)
            elif look_word not in k:


                send =(look_word,False)
        return send


@dataclass
class byzdis_disubution_map:
    map:list
    def map_qurry(self):
        return self.map
    def unique_name_lookup(self,unique_name):
        send=None
        k=[x[0] for x in self.map]
        for tupl in k:

            if unique_name in tupl:
                send = (float(tupl[1]), True, unique_name)



        return send


@dataclass
class NullIterable:
    def __init__(self):
        pass

    def __iter__(self):
        return iter([])  # returns an empty iterator

@dataclass
class searchdict:
    mastdict: list
    def keywords(self):
        out=[x[0] for x in self.mastdict]
        return out


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

def list_of_data_points_to_dict(point_list:list):
    number_of_docs=len(point_list)
    listofwordlists = [pnt.words() for pnt in point_list]

    wordlist = []
    wordli=[]
    for wordsk in listofwordlists:

        wordli += wordsk[0:len(wordsk)]
    wordlist+=wordli




    words = sorted(set(wordlist))



    mast_dict_as_list =[]
    for word in words:
        wordocer=0
        for point in point_list:
            if point.word_ocerenses(word)[1]:
                wordocer += point.word_ocerenses(word)[0]
        toadd= (word,wordocer/number_of_docs)
        mast_dict_as_list.append(toadd)
        #[x[0] for x in mast_dict_as_list ]
    return mater_dict(matrix=mast_dict_as_list)







def function_for_map(point1:datapoint,dict):
    relation_fromword=0
    p1_word_list = list(point1.words())
    distubutinsumaslist=[]

    finall_map= []
    for word in p1_word_list:



        if not dict.word_ocerenses(word)[1]:
            print('wtf',"166",dict.word_ocerenses(word))

        else:

            ocrents_in_doc=int(point1.word_ocerenses(word)[0])
            averge_occents_in_data=dict.word_ocerenses(word)[0]
            relation_fromword += (ocrents_in_doc - averge_occents_in_data)+1
            distubutinsumaslist.append(relation_fromword)


        
        finall_map.append([point1.unique_name,sum(distubutinsumaslist)])
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


def list_of_poins_to_map(listofpoints,mat_dict):
    relatiin_mapp_full = byzdis_disubution_map(map=[])


    for pointstk in listofpoints:


        if type(function_for_map(pointstk, mat_dict)) != NullIterable:
            names_in_map=[x[0] for x in relatiin_mapp_full.map_qurry()]


            if pointstk.unique_name not in names_in_map:
                    relatiin_mapp_full.map.append(function_for_map(pointstk, mat_dict))

    return relatiin_mapp_full



def searchalgo(search_terms:str,compleat_data_as_points_list:list,master_ditionary:mater_dict,byzdisrubution_map:byzdis_disubution_map,*term_filtering_stranth:int):
    list_of_datapoint_with_term=[]
    unsorted_list_of_datapoint_names_with_term=[]
    if term_filtering_stranth!=int:
        use_term_fitering=False
    for term in search_terms.split():
        if term in master_ditionary.words():
            if  not use_term_fitering:
                list_of_datapoint_with_term += [x for x in compleat_data_as_points_list if term in x.words()]

            elif master_ditionary.word_ocerenses(term)[0]<term_filtering_stranth:
                list_of_datapoint_with_term += [x for x in compleat_data_as_points_list if term in x.words()]
            pass

    master_ditionary_from_points_with_terms = list_of_data_points_to_dict(list_of_datapoint_with_term)
    map_of_points_with_terms=list_of_poins_to_map(list_of_datapoint_with_term,master_ditionary_from_points_with_terms)
    for name_dis_number_pair in map_of_points_with_terms.map:
        lookup_name=name_dis_number_pair[0][0]

        local_before_filter=byzdisrubution_map.unique_name_lookup(lookup_name)[0]

        print(local_before_filter,name_dis_number_pair[0][1])
        change_in_local=local_before_filter-name_dis_number_pair[0][1]
        unsorted_list_of_datapoint_names_with_term.append([name_dis_number_pair[0][0],change_in_local])
        print(name_dis_number_pair[0][0],change_in_local)
    print(unsorted_list_of_datapoint_names_with_term)
    unsorted_list_of_datapoint_names_with_term.sort()

    return [name[0] for name in unsorted_list_of_datapoint_names_with_term]
        #else:
            #return "pleas put a space betwwen each word and number sequence or try different search terms"

def main():

    relatiin_mapp_full= byzdis_disubution_map(map=[])
    relatiin_mapp_full.map = []
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
    #print("267",mat_dict)
    bizdismap=list_of_poins_to_map(list_of_points_before_relatin_maping, mat_dict)

    print( bizdismap,"240")

    dictfromdp= list_of_data_points_to_dict(list_of_points_before_relatin_maping)

    print(searchalgo('romeo',list_of_points_before_relatin_maping,mat_dict,bizdismap))

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


