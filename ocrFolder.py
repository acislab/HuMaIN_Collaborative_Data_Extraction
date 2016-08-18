#!/usr/bin/python
##########################################################################################
# Developer: Icaro Alzuru         Project: HuMaIN (http://humain.acis.ula.ve)
# Description: 
#   Program which executes the img2txt (OCR) script to each jpg file available at the
# input folder. 
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

def die_with_usage():
	""" HELP MENU """
	print ''
	print 'usage:'
	print '   python ocrFolder.py <src_folder> <dst_folder> <logs_folder>'
	print ''
	print 'example:'
	print '   python ocrFolder.py /home/user/data /home/user/results /home/user/logs'
	print ''
	sys.exit(0)


if __name__ == '__main__':
	""" MAIN """
	# help menu
	if len(sys.argv) != 4:
		die_with_usage()

	# get params
	src_folder = sys.argv[1]
	dst_folder = sys.argv[2]
	logs_folder = sys.argv[3]
    
	# sanity check
	if not os.path.isdir(src_folder):
		print '\nERROR: source folder', src_folder, 'does not exist.\n'
		die_with_usage()
        
	for root, dirs, files in os.walk(src_folder):
		for file in files:
			if file.endswith(".jpg"):
				baseFilename = file[:-4]
				start_time = time.time()
				command = "python img2txt.py " + src_folder + "/" + file + " " + dst_folder + "/" + baseFilename + " | cat > " + logs_folder + "/" + baseFilename + ".log"	
				os.system(command)
				print("\n--- %s: %s seconds ---" % (baseFilename, time.time() - start_time))


