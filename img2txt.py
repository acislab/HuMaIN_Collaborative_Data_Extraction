#!/usr/bin/python
##########################################################################################
# Developer: Icaro Alzuru         Project: HuMaIN (http://humain.acis.ula.ve)
# Description: 
#   Script which executes the OCRopy OCR process (Binarization, Segmentation, and 
# Recognition). Please configure dirOcropy variable to indicate the OCRopus path.
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

dirOcropy = "/root/ocropy"

start_time = time.time()
############################# Validations #################################################
# Verification of the number of parameters and help
if len(sys.argv) != 3:
	print("Error: Invalid number of parameters")
	print("Use: python img2txt.py <source_file> <dest_folder>\n")
	sys.exit()

filename = sys.argv[1]
dstFolder = sys.argv[2]

# The existence of the source file is verified
if ( not os.path.isfile(filename)):
	print("Error: File %s was not found" % (filename))
	sys.exit()

# The existence of the destination folder is verified or created
if ( not os.path.isdir( dstFolder )):
	subprocess.call(["mkdir -p " + dstFolder], shell=True)
	if ( not os.path.isdir( dstFolder )):
		print("Error: Destination folder %s could not be created" % (dstFolder))
		sys.exit()

# The existence of the ocropy folder is verified
if ( not os.path.isdir(dirOcropy)):
	print("Error: Ocropy folder %s was not found" % (dirOcropy))
	sys.exit()
##########################################################################################

### Binarization
c = dirOcropy + "/ocropus-nlbin -n " + filename + " -o " + dstFolder
r = subprocess.call([c], shell=True)
if r != 0:
	print("Error: Binarization process failed")
	sys.exit()
	
### Segmentation
c = dirOcropy + "/ocropus-gpageseg -n " + dstFolder + "/0001.bin.png"
r = subprocess.call([c], shell=True)
if r != 0:
	print("Error: Segmentation process failed")
	sys.exit()

### Character Recognition
c = dirOcropy + "/ocropus-rpred -n -m en-default.pyrnn.gz " + dstFolder + "/0001/*.png"
r = subprocess.call([c], shell=True)
if r != 0:
	print("Error: Character recognition process failed")
	sys.exit()

### All text
name1 = filename.split("/")[-1]
name = name1.split(".")[0]
c = "cat " + dstFolder + "/0001/??????.txt > " + dstFolder + "/" + name + ".txt" 
r = subprocess.call([c], shell=True)

### Web page generation
#c = dirOcropy + "/ocropus-hocr " + dstFolder + "/0001/??????.bin.png"
#print(c)
#r = subprocess.call([c], shell=True)
#if r != 0:
#	print("Error:")
#	sys.exit()

print("\n--- %s seconds ---" % (time.time() - start_time))

