#!/usr/bin/env python3

# Giovanni Foletto - Reimplementing Spell in order to get comprehension in
# a JSON compatible object.

import os
import json
import numpy as np
import urllib.parse
import string
from tqdm import tqdm

STRING = string.ascii_uppercase

class LogReader:
    def __init__(self, inlog) -> None:
        """
        inlog: give the JSON deserialized log object (it should be a dict())
        """
        assert type(inlog) == type(dict())

        self.inlog    = inlog
        self.keys     = set()
        self.element  = dict()

        self.unwrap(self.inlog)
    
    def unwrap(self, log, key="", context="") -> None:
        if type(log) == type(dict()):
            for k in log.keys():
                self.keys.add(k)
                if context == "":
                    self.unwrap(log[k], key=k, context=k)
                else:
                    self.unwrap(log[k], key=k, context=context+"."+k)
        elif type(log) == type(list()):
            for el in log:
                self.unwrap(el, key=key, context=context)
        # Technicly, "Records" field should not exists anymore
        else:
            if key == "assumeRolePolicyDocument":
                log = urllib.parse.unquote(log).replace("\n", "").replace(" ", "")
            
            self.element[context] = log

class LCSSputoContent:
    def __init__(self, originalLog="", templateName="", templateID=1, keyName="") -> None:
        self.originalLog    = originalLog   # contains the started seq1 log
        self.templateName   = templateName  # contains the template readable name
        self.templateID     = templateID    # contains the template id
        self.keyName        = keyName       # contains the key respect of the template is made
        self.counter        = 1             # how many log are of this type
    
    def __str__(self) -> str:
        return f"LCSSputoContent<originalLog={self.originalLog}, \
            templateName={self.templateName}, templateID={self.templateID}, \
            keyName={self.keyName}, counter={self.counter}>"

class LCSSputoLogFile:
    def __init__(self, originalLog="", templateName="", templateID=1, content="") -> None:
        self.originalLog    = originalLog   # contains the started seq1 log
        self.templateName   = templateName  # contains the template readable name
        self.templateID     = templateID    # contains the template id
        self.content        = content       # contains the list of different contents
    
    def __str__(self) -> str:
        return " ".join([a.templateName for a in self.content])

class SputuLogParser:
    def __init__(
            self, 
            indir="./", 
            outdir="./result/",
            filename=None
            # log_format=None, 
            # tau=0.5, 
            # rex=[], 
            # keep_para=True
        ) -> None:

        assert indir is not None and indir != ""
        assert filename is not None
        
        self.path      = indir
        self.savePath  = outdir
        self.filename  = filename
            
        self.content_templ = dict()
        self.log_templ     = dict()
        #self.JSON_PARSE= 
        # self.tau       = tau
        # self.logformat = log_format
        # self.df_log    = None
        # self.rex       = rex
        # self.keep_para = keep_para
        
        if not os.path.exists(self.savePath): 
            os.makedirs(self.savePath)

        self.file      = open(self.filename, "r")

    def LCS(self, seq1, seq2):
        # inizializzo matrice con linee seq2 e colonne seq1
        lengths = [[0 for j in range(len(seq2) + 1)] for i in range(len(seq1) + 1)]

        for i in range(len(seq1)):
            for j in range(len(seq2)):
                if seq1[i] == seq2[j]:
                    lengths[i + 1][j + 1] = lengths[i][j] + 1
                else:
                    lengths[i + 1][j + 1] = max(lengths[i + 1][j], lengths[i][j + 1])

        # read the substring out from the matrix
        result = []
        lenOfSeq1, lenOfSeq2 = len(seq1), len(seq2)
        while lenOfSeq1 != 0 and lenOfSeq2 != 0:
            if lengths[lenOfSeq1][lenOfSeq2] == lengths[lenOfSeq1 - 1][lenOfSeq2]:
                lenOfSeq1 -= 1
            elif lengths[lenOfSeq1][lenOfSeq2] == lengths[lenOfSeq1][lenOfSeq2 - 1]:
                lenOfSeq2 -= 1
            else:
                assert seq1[lenOfSeq1 - 1] == seq2[lenOfSeq2 - 1]
                result.insert(0, seq1[lenOfSeq1 - 1])
                lenOfSeq1 -= 1
                lenOfSeq2 -= 1
        return result
    
    def create_vocabulary(self, filter="Records", until=10):
        # main method to build the vocabulary of logs
        json_file = json.loads(self.file.read())

        array_log_1 = np.array(json_file[filter][:until])
        array_log_2 = np.array(json_file[filter][:until])

        for log_1 in tqdm(array_log_1):
            # save the temp array of LCS for every new array and
            # initialize parser class for log_1
            parser_1 = LogReader(log_1)
            this_log_content = []
            # TODO: warning if a keys class is not campionated
        
            for selected_key in parser_1.element.keys():
                longest = []    # the array with most common chars        
                max_len = 0     # the max len of the match

                for log_2 in array_log_2:
                    parser_2 = LogReader(log_2)
                    # check if the key exists on both classes
                    if parser_2.element.get(selected_key) is None:
                        continue                
                    seq1 = parser_1.element[selected_key]
                    seq2 = parser_2.element[selected_key]

                    if seq1 is None:
                        seq1 = "None"
                    if seq2 is None:
                        seq2 = "None"

# not work
                    # if type(seq1) == type(bool):
                    #     seq1 = "True" if seq1 else "False"

                    # if type(seq1) == type(bool):
                    #     seq2 = "True" if seq2 else "False"

                    lcs_res = self.LCS(seq1, seq2)

                    if len(lcs_res) >= max_len:
                        max_len = len(lcs_res)
                        longest = lcs_res
            
                find = False
                # check if the key class already exists
                if self.content_templ.get(selected_key) is not None:
                    # check if there is already the content researched
                    for lsc in self.content_templ[selected_key]:
                        if np.array_equal(longest, lsc.templateID):
                            lsc.counter += 1
                            find = True
                else:
                    self.content_templ[selected_key] = []      

                assign_new_id = len(self.content_templ[selected_key]) +1

                if not find:
                    lcs_new = LCSSputoContent(
                                keyName=selected_key, 
                                originalLog=log_1,
                                templateID=longest,
                                templateName=f"{selected_key}-{assign_new_id}"
                            )
                    self.content_templ[selected_key].append(lcs_new)
                    this_log_content.append(lcs_new)
            
            # search if there is a log build up like this or not
            template_name = "T"+str(len(self.log_templ)+1)
            if len(self.log_templ) == 0:
                self.log_templ[template_name] = LCSSputoLogFile(
                    content=this_log_content,
                    templateName=template_name
                )
                continue
                # print(self.log_templ[template_name])
            
            find = False
            for lt in self.log_templ:
                if np.array_equal(lt, this_log_content):
                    find = True
            
            if not find:
                self.log_templ[template_name] = LCSSputoLogFile(
                        content=this_log_content,
                        templateName=template_name
                    )
        
        print("Printing vocabulary: ")
        voc = 0
        for k in self.content_templ:
            #print(self.content_templ[k])
            for l in self.content_templ[k]:
                print(l.templateName)
                voc += 1
        
        print(f"\n Found #{voc} for the given files")
                
        print("Printing LogTypes: ")
        voc = 0
        for k in self.log_templ:
            #print(self.content_templ[k])
            print(k)
            voc += 1
        
        print(f"\n Found #{voc} for the given files")

    def parse(self, inlog):
        parser_1 = LogReader(inlog) 
        #print([i for i in parser_1.element.keys()])
        #print([i for i in parser_1.keys])
        
        l1_templ = []
        for key_1 in parser_1.element.keys():
            longest = []    # the array with most common chars        
            class_type = -1 # the class type of the common chars
            max_len = 0     # the max len of the match
            if self.content_templ.get(key_1) is None:
                print("[***Warning***], the vocabulary has not all the requested key-classes")
                continue

            for templ in range(len(self.content_templ[key_1])):
                # compare with keys of the current log and the keys of the template on the 
                # vocabulary found.
                seq1 = parser_1.element[key_1]
                seq2 = "".join(self.content_templ[key_1][templ].templateID)
                #print(f"{key_1} -> {parser_1.element[key_1]}")

                if seq1 is None:
                    seq1 = "None"
                if seq2 is None:
                    seq2 = "None"

                find_lcs = self.LCS(seq1, seq2)
                if len(find_lcs) >= max_len:
                    longest = find_lcs
                    class_type = templ
                    max_len = len(find_lcs)

            l1_templ.append(self.content_templ[key_1][class_type])
            
            #print(f"LOG INPUT: {key_1} \t CLASSIFICATION => {self.content_templ[key_1][class_type].templateName}, with content {"".join(longest)}")
        
        for el in self.log_templ:
            if np.array_equal(self.log_templ[el].content, l1_templ):
                print(el)


if __name__ == "__main__":

    indir       = "./"
    filename    = "../test.json"
    outdir      = "./result/", 
    #log_format  = None, 
    # tau=0.5, 
    # rex=[], 
    # keep_para=True
    spell = SputuLogParser(indir=indir, outdir=indir, filename=filename)
    spell.create_vocabulary(until=100)

    print("\n ==== Testing ==== \n")
    with open("../input.json", "r") as fj:
        j_obj = json.loads(fj.read())
        for rec in j_obj: #["Records"]:
            spell.parse(rec)