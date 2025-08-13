''' hate speach analizis computes relationships and trend in data ,
    Copyright (C) 2024 Kai Broadbent 'BlazarKnight'

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to appblazarknight@gmail.com
'''
import canopener as can
import pickle
#from collections.abc import range_iterator
from os import close
import itertools as it
#import formater.format as form
from dataclasses import dataclass
from collections import defaultdict
import csv

import re
#bob test gitnore

@dataclass
class datapoint:
    unique_name: str
    matrix: dict

    def name_qury(self):
        return self.unique_name

    def dict_matrix_qury(self):
        return self.matrix

    def word_ocerenses(self, look_word):
        if look_word in self.matrix:
            return (self.matrix[look_word], True)
        else:
            return (look_word, False)

    def words(self):
        dictofm = dict(self.matrix)
        return tuple(dictofm.keys())

    def __hash__(self):
        return hash(self.unique_name)


@dataclass
class mater_dict:

    matrix: list


    def lisget(self, index, default=None):
        sem= self.matrix
        try:
            return sem[index]
        except IndexError:
            return default

    def words(self):

        return [x[0] for x in self.matrix]

    def word_ocerenses(self, look_word):
        send = ()
        k = [x[0] for x in self.matrix]
        #send= self.matrix[self.matrix.index(look_word,float)]

        for tupl in self.matrix:

            if look_word in tupl:
                send = (tupl[1], True, look_word, tupl)
            elif look_word not in k:

                send = (look_word, False)
        return send




    def fastlookup(self,look_world):

        ''' foats= [x[1] for x in self.matrix]
        placeholder = float(i for i in foats
                            )

        look_tup=(look_world, )'''
        lis=[i for i, x in enumerate(self.matrix) if x[0] == look_world]
        #print([i for i, x in enumerate(self.matrix) if x[0] == look_world])
        for i in lis:
            return (self.matrix[i])

        return  [i for i, x in enumerate(self.matrix) if x[0] == look_world]

    def topwords(self,topwhat: int,sortpat:int,*retpat:int):

        print(retpat)
        print(sortpat)
        sortedlist = sorted(self.matrix, key=lambda x: x[sortpat])
        if retpat==():
            return sortedlist[0:topwhat - 1]
        if retpat != () and int(retpat[0]) <= len(sortedlist[0])-1:
            return [i[retpat[0]] for i in sortedlist[0:topwhat - 1]]

        print(retpat)# <= len(sortedlist[0])-1)
        return sortedlist[0:topwhat-1]


@dataclass
class byzdis_disubution_map:
    map: list

    def map_qurry(self):
        return self.map

    def unique_name_lookup(self, unique_name):
        send = None
        k = [x[0] for x in self.map]
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
        out = [x[0] for x in self.mastdict]
        return out


def remove_duplicates(lst):
    # seen = []
    # return [x for i, x in enumerate(lst) if x not in seen or not seen.append(x)]
    from collections import OrderedDict

    # my_list = [1, 2, 3, 2, 4, 3, 5]
    unique_items = list(OrderedDict.fromkeys(lst))
    return unique_items


def file_to_clean_str(file):
    import re
    openfile = open(file, "r")
    clean = ''
    for line in openfile:
        # for symbol in ["\n",':','.',"'",'&','-']:
        lineclean = re.sub(r'[^\w\s]', '', line)
        lineclean = lineclean.replace("\n", " ")
        lineclean = lineclean.lower()
        clean = clean + lineclean
    return clean
def cleaner(lin):
    lineclean = re.sub(r'[^\w\s]', '', lin)
    lineclean = lineclean.replace("\n", " ")
    lineclean = lineclean.lower()

    return lineclean

def string_to_dict(fullstring, numofdoc):
    # fullstring must have all words and terms of data set in it!!!!
    data_list_split = fullstring.split()  # Split the string into a list of words
    wordcounttot=len(data_list_split)# conts the numer of words in the dataset
    # Count the occurrences of each word in data_list_split using a defaultdict
    word_counts = defaultdict(int)
    for word in data_list_split:
        word_counts[word] += 1

    data_list_singal = set(data_list_split)  # Remove duplicates using a set
    sorted_data_list = sorted(data_list_singal)  # Sort the list of unique words

    matrix = [(word, float(word_counts[word]) / numofdoc, float( float(word_counts[word]) / wordcounttot)/ numofdoc,word_counts[word] ) for word in sorted_data_list]
    return mater_dict(matrix=matrix)


def list_of_data_points_to_dict(point_list: list):
    number_of_docs = len(point_list)
    listofwordlists = [pnt.words() for pnt in point_list]

    wordlist = []
    wordli = []
    for wordsk in listofwordlists:
        wordli += wordsk[0:len(wordsk)]
    wordlist += wordli

    words = sorted(set(wordlist))

    mast_dict_as_list = []
    for word in words:
        wordocer = 0
        for point in point_list:
            if point.word_ocerenses(word)[1]:
                wordocer += point.word_ocerenses(word)[0]
        toadd = (word, wordocer / number_of_docs)
        mast_dict_as_list.append(toadd)
        # [x[0] for x in mast_dict_as_list ]
    return mater_dict(matrix=mast_dict_as_list)


def function_for_map(point1: datapoint, dict):
    relation_fromword = 0
    p1_word_list = list(point1.words())
    distubutinsumaslist = []

    finall_map = []
    for word in p1_word_list:

        if not dict.word_ocerenses(word)[1]:
            print('wtf', "166", dict.word_ocerenses(word))

        else:

            ocrents_in_doc = int(point1.word_ocerenses(word)[0])
            averge_occents_in_data = dict.word_ocerenses(word)[0]
            relation_fromword += (ocrents_in_doc - averge_occents_in_data) + 1
            distubutinsumaslist.append(relation_fromword)

        finall_map.append([point1.unique_name, sum(distubutinsumaslist)])
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


def string_to_datapoint_without_relations(name: str, data_as_string: str):
    point = datapoint(unique_name=name, matrix=string_in_dataset_to_matrix(data_as_string))

    return point


def list_of_poins_to_map(listofpoints, mat_dict):
    relatiin_mapp_full = byzdis_disubution_map(map=[])

    for pointstk in listofpoints:

        if type(function_for_map(pointstk, mat_dict)) != NullIterable:
            names_in_map = [x[0] for x in relatiin_mapp_full.map_qurry()]

            if pointstk.unique_name not in names_in_map:
                relatiin_mapp_full.map.append(function_for_map(pointstk, mat_dict))

    return relatiin_mapp_full


def searchalgo(search_terms: str, compleat_data_as_points_list: list, master_ditionary: mater_dict,
               byzdisrubution_map: byzdis_disubution_map, *term_filtering_stranth: int):
    list_of_datapoint_with_term = []
    unsorted_list_of_datapoint_names_with_term = []
    if term_filtering_stranth != int:
        use_term_fitering = False
    for term in search_terms.split():
        if term in master_ditionary.words():
            if not use_term_fitering:
                list_of_datapoint_with_term += [x for x in compleat_data_as_points_list if term in x.words()]

            elif master_ditionary.word_ocerenses(term)[0] < term_filtering_stranth:
                list_of_datapoint_with_term += [x for x in compleat_data_as_points_list if term in x.words()]
            pass

    master_ditionary_from_points_with_terms = list_of_data_points_to_dict(list_of_datapoint_with_term)
    map_of_points_with_terms = list_of_poins_to_map(list_of_datapoint_with_term,
                                                    master_ditionary_from_points_with_terms)
    for name_dis_number_pair in map_of_points_with_terms.map:
        lookup_name = name_dis_number_pair[0][0]

        local_before_filter = byzdisrubution_map.unique_name_lookup(lookup_name)[0]

        change_in_local = local_before_filter - name_dis_number_pair[0][1]
        unsorted_list_of_datapoint_names_with_term.append([name_dis_number_pair[0][0], change_in_local])

    unsorted_list_of_datapoint_names_with_term.sort()

    return [name[0] for name in unsorted_list_of_datapoint_names_with_term]
    # else:
    # return "pleas put a space betwwen each word and number sequence or try different search terms"


def main():
    relatiin_mapp_full = byzdis_disubution_map(map=[])
    relatiin_mapp_full.map = []
    terbo=1000
    pathtofile= '/home/the-game/Downloads/ghc_train.tsv'
    openfile = open(pathtofile, "r")
    clean = ''
    count = 0
    full_str = ''
    list_of_point = []
    lenchecker = 0
    with open(pathtofile, "r") as tsvfile:
        row_count = sum(1 for line in tsvfile)
    number_of_docs = row_count #row_count
    list_of_points_before_relatin_maping = []
    linesers = 0

    for line in open(pathtofile, "r"):

        full_str = full_str + cleaner(line)
        linesers= linesers +1

    linesers = 0

    # open .tsv file
    with open(pathtofile, "r") as f:

        # Read data line by line
            for line in f:
                full_str = full_str + line
                linesers = linesers + 1

    # print data line by line
    full_str= can.can_opener_tsv(pathtofile)[0]
    #print(full_str)
    with open(pathtofile, "r") as file:

        tsv_file = csv.reader(file, delimiter="\t")
        nameln = 0
        # printing data line by line
        for line in tsv_file:
            nameln = nameln + 1
            list_of_points_before_relatin_maping.append(string_to_datapoint_without_relations(name=nameln, data_as_string=cleaner(str(line))))
    #print(list_of_points_before_relatin_maping,'313')

    print(nameln)

    mat_dict = string_to_dict(full_str, number_of_docs)
    #print("267",mat_dict)
    termlist = 'trump', 'zog'
    for i in termlist:
        if i in mat_dict.words():
            print(mat_dict.fastlookup(i),"351")
        else:
            print(i,"is not in the data set ")
    print(mat_dict.topwords(500,1,0))
    print(mat_dict.topwords(500, 2, 0))
    print(mat_dict.topwords(500, 3, 0))
    print(mat_dict.topwords(500000, 1, 0)==mat_dict.topwords(500, 3, 0))
   #
    # print(.index(x))
    #print([termlist[m] for m in range(0,3)])
    #print( mat_dict.words().index([termlist[m] for m in range(0,3)]))
    #termsindata= [  in mat_dict.words()    ]




    #bizdismap = list_of_poins_to_map(list_of_points_before_relatin_maping, mat_dict)

    #print(bizdismap, "240")

    #dictfromdp = list_of_data_points_to_dict(list_of_points_before_relatin_maping)

   # print(searchalgo('trump', list_of_points_before_relatin_maping, mat_dict, bizdismap),"326")

    #with open("points.pickle", "wb") as file:
        #pickle.dump(list_of_points_before_relatin_maping, file)
    #with open("dict.pickle", "wb") as file:
        #pickle.dump(mat_dict, file)
    #with open("relationmap.pickle", "wb") as file:
        #pickle.dump(relatiin_mapp_full, file)
    print("done")

    pass


if __name__ == '__main__':
    main()


