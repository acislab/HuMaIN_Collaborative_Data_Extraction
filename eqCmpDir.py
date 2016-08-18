#!/usr/bin/python
##########################################################################################
# Developer: Icaro Alzuru         Project: HuMaIN (http://humain.acis.ula.ve)
# Description: 
#   It compares the files in two folders, returning the percentage of words in file 1 
# which are also present in file 2.
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

import sys, os, subprocess
import time

def die_with_usage():
    """ HELP MENU """
    print ''
    print 'Usage:'
    print '   python eqCmpDir.py <gold_folder> <result_folder> <output_file>'
    print ''
    print 'It assumes extension .txt for the files of folders <gold_folder> and <result_folder>'    
    print 'Example:'
    print '   python eqCmpDir.py /root/label-data/ent/gold/ocr /root/Data/entResult cmp_ent.txt'
    print ''
    sys.exit(0)

def cmpS( s1, s2 ):
	wS1 = s1.split()
	wS2 = s2.split()
	n = 0
	d = 0
	for w in wS1:
		if (w in wS2):
			d = d + 1
		n = n + 1
	return d, n

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

							d, n = cmpS ( gold_content, result_content )
							f.write( baseFilename + " " + str(d) + " " + str(n) + "\n" )
					except IOError:
						f.write( baseFilename + " Not Found\n")

	f.close()

