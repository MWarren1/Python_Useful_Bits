##### using arguments with a script

import argparse

## CLI switches
parser = argparse.ArgumentParser(prog='<scriptname>', description='description')
parser.add_argument('--input', required=True, help='description')
parser.add_argument('--output', help='description(optional)')

args = parser.parse_args()
input = args.input
output = args.output

## tests if optional argument was used
if output is None:
  output = "default option"


#########################################################

##### get a list of files from a folder

import os.path
from os import walk

folder = "C:\temp\ ## needs to end with a \

## find all files in folder and make a list
(_, _, filenames) = walk(folder).next()

## loop through all the files to do some thing
totalfiles = (len(filenames) - 1)
currentfilenum = 0
while currentfilenum <= totalfiles:
		currentfile = folder + filenames[currentfilenum]
		## do some thing with that filename
	
