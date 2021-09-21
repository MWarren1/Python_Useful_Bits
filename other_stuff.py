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
	
#########################################################

##### time how long script takes to run

import time
## start of the script
start_time = time.time()

## end of the script
end_time = time.time()
print(end_time - start_time)



### Just some functions that might be useful in the future

#########################################################

## FUNCTION - input is an ip address in an array and Returns the next ip address in an array
def next_ip(currentip):
	# start with last oct
	currentip[3] = currentip[3]+1
	if currentip[3] == 256:
		currentip[3] = 0
		currentip[2] = currentip[2]+1
		if currentip[2] == 256:
			currentip[2] = 0
			currentip[1] = currentip[1]+1
			if currentip[1] == 256:
				currentip[1] = 0
				currentip[0] = currentip[0]+1
	return currentip[0],currentip[1],currentip[2],currentip[3],
	
##########################################################################	
	
## FUNCTION - check ip addresses are correct format
def ipcheck(input):
	ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', input )
	if len(ip) != 0:	
		ip = str(ip)
		ip = ip[2:-2]
		error = 0
	else:
		error = 1
				
	return ip,error;
	
##########################################################################
	
## FUNCTION - SNMP get request - borrowed this function
## NEEDS PYSNMP
def snmp_get(ip,oid,community):
 
  from pysnmp.entity.rfc3413.oneliner import cmdgen

  cmdGen = cmdgen.CommandGenerator()
 
  errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
    cmdgen.CommunityData(community),
    cmdgen.UdpTransportTarget((ip, 161),timeout=1,retries=0),
    oid
  )
 
  # Check for errors and print out results
  if errorIndication:
    print(errorIndication)
  else:
    if errorStatus:
      print('%s at %s' % (
        errorStatus.prettyPrint(),
        errorIndex and varBinds[int(errorIndex)-1] or '?'
       )
     )
    else:
      for name, val in varBinds:
        #print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
        return val	
        
  ##########################################################################
