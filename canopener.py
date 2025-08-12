""" hate speach file cleaner this file defines the funtions that cleans/formats the data form the internet,
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
"""
import re
import csv
import search as se
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


def Findurlin(string):
    import re
    # findall() has been used
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]

def can_opener_pdf(file):
    from PyPDF2 import PdfReader

    reader = PdfReader(file)
    pgcont = len(reader.pages)
    pdfasstr = ""
    for i in range(0, pgcont):
        page = reader.pages[i]
        extracted_text = page.extract_text()
        pdfasstr = pdfasstr + extracted_text
    return pdfasstr


def can_opener_tsv(file):
    full_str = ''
    with open(file, "r") as tsvfile:
        row_count = sum(1 for line in tsvfile)

    list_of_points_before_relatin_maping = []
    linesers = 0

    pathtofile1 = file
    for line in open(pathtofile1, "r"):

        full_str = full_str + cleaner(line)
        linesers= linesers +1

    linesers = 0

    # open .tsv file
    with open(pathtofile1, "r") as f:

        # Read data line by line
            for line in f:
                full_str = full_str + line
                linesers = linesers + 1

    # print data line by line
    full_str= cleaner(full_str)
    #print(full_str)
    with open(pathtofile1, "r") as file:

        tsv_file = csv.reader(file, delimiter="\t")
        nameln = 0
        # printing data line by line
        for line in tsv_file:
            nameln = nameln + 1
            list_of_points_before_relatin_maping.append(se.string_to_datapoint_without_relations(name=nameln, data_as_string=cleaner(str(line))))
    #print(list_of_points_before_relatin_maping,'313')


    return (full_str,list_of_points_before_relatin_maping,nameln)


def clean(inp: str, extent: str):
    return can_opener_pdf(inp)


if __name__ == "__main__":
    print(
        clean(
            "/home/supercow/PycharmProjects/Seagull/browser/2024GameManual.pdf", "pdf"
        )
    )
