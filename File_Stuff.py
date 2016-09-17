

## Open file for reading and do some thing for each line

with open(inputfile, 'Ur') as f:
	for line in f:
	  ## Line is a string


## Open file for writing and writing to it

output = open(outputfile, 'w+')
output.write("some_string\n")

## Open File as csv and do some thing

import csv

with open(inputfile, 'Ur') as f:
	parserreader = csv.reader(f)
	next(parserreader, None)
	for row in parserreader:
	  ## row is the current row. row[0] is 1st cell, row[1] is 2nd cell etc...
