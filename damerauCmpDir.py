#!/usr/bin/python
##########################################################################################
# Developer: Icaro Alzuru         Project: HuMaIN (http://humain.acis.ula.ve)
# Description: 
#   It compares the files in two folders, returning the normalized Damerau-Levenshtein 
# distance for each common file. The Damerau-Levenshtein used is the developed by 
# Geoffrey Fairchild and available at https://github.com/gfairchild/pyxDamerauLevenshtein
##########################################################################################
# Copyright 2016    Advanced Computing and Information Systems (ACIS) Lab - UF
#                   (https://www.acis.ufl.edu/)
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##########################################################################################

import sys, os, subprocess, time
from pyxdameraulevenshtein import normalized_damerau_levenshtein_distance

def die_with_usage():
    """ HELP MENU """
    print ''
    print 'Usage:'
    print '   python damerauCmpDir.py <gold_folder> <result_folder> <output_file>'
    print ''
    print 'It assumes extension .txt for the files of folders <gold_folder> and <result_folder>'    
    print 'Example:'
    print '   python damerauCmpDir.py /root/label-data/ent/gold/ocr /root/Data/entResult cmp_ent.txt'
    print ''
    sys.exit(0)

if __name__ == '__main__':
    """ MAIN """
    # help menu
    if len(sys.argv) != 4:
        die_with_usage()

    # get params
    gold_folder = sys.argv[1]
    result_folder = sys.argv[2]
    filename = sys.argv[3]
    
    # sanity check
    if not os.path.isdir(gold_folder):
        print '\nERROR: source folder', gold_folder, 'does not exist.\n'
        die_with_usage()
        
    if not os.path.isdir(result_folder):
        print '\nERROR: source folder', result_folder, 'does not exist.\n'
        die_with_usage()
        
    f = open(filename,'w') 

    for root, dirs, files in os.walk(gold_folder):
        for file in files:
            if file.endswith(".txt"):
                baseFilename = file[:-4]
                gold_filename = gold_folder + "/" + file 
                result_filename = result_folder +"/" + file
                #result_filename = result_folder + "/" + baseFilename +"/" + file
                
                with open(gold_filename, 'r') as gfile:
                    gold_content = gfile.read()
                    try:
                        with open(result_filename, 'r') as rfile:
                            result_content = rfile.read()
        
                            a = normalized_damerau_levenshtein_distance(gold_content, result_content)
                            f.write( baseFilename + " " + str(a) + "\n")
                    except IOError:
                        f.write( baseFilename + " 2.0\n")

    f.close()

