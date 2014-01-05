#!/usr/bin/python

import argparse
import json
import math
import os
import sys


def parseArgument():
    """
    Code for parsing arguments
    """
    parser = argparse.ArgumentParser(description='Parsing a file.')
    parser.add_argument('-f',required=True)
    args = vars(parser.parse_args())
    return args


def parseFile(filename):
	"""
	This would load the json file
	"""
	json_data = open(filename, "r")
	data = json.load(json_data)
	print(data)
	json_data.close()

### your functions here

def main():
    args = parseArgument()
    filename = args['f']
    print filename
    parseFile(filename)
	### your code here

main()
