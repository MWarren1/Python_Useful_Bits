## using arguments with a script

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
