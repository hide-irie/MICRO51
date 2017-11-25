import zipfile
import os, errno
import shutil
import csv
import itertools
import json
import binascii
import codecs
import sqlite3
import datetime
import sys
import collections
from getpass import getpass
import argparse
from collections import OrderedDict
from collections import defaultdict
from sets import Set

programdict   = defaultdict(list)
sessiontitles = defaultdict()
programnames = defaultdict()
papernames = defaultdict()

sessionnames  = Set([])
paralleltracks = {'1','2','3','4','5','6','7'}
singletracks   = {'8'}

def parsecsvprogram(name):
	reader = csv.reader(open(name, 'rU'), delimiter=",")
	header = reader.next()
	for row in reader:
		sessionnames.add(row[0])
		programdict[row[0]].append(row[4]+"|"+row[5])
		sessiontitles[row[0]] = row[1]

	for x in paralleltracks:
		programnames[x] = (sessiontitles[x+"-A"],sessiontitles[x+"-B"])
		papernames[x]   = itertools.izip_longest(programdict[x+"-A"],programdict[x+"-B"])
	

	th = "<td style=\"background-color: light blue;\" class=\"tdb\"><strong><em>%s</em></strong></td>"
	for x in sorted(paralleltracks):
		print("####"+x+"####")
		print("<tr>")
		print(th % (x+"-A "+sessiontitles[x+"-A"]))
		print(th % (x+"-B "+sessiontitles[x+"-B"]))
		print("</tr>")

		# Iterate over all the papers
		for p in papernames[x]:
			print("<tr>")
			print("<td>&nbsp;</td>")

			# Session A paper
			if p[0] is not None:
				fields = p[0].split("|")
				print("<td>")
				print("<strong>")		
				print(fields[0])
				print("</strong><br>")
				print(fields[1])
				print("</td>")
			else:
				print("<td>")
				print("<strong>")		
				print("")
				print("</strong><br>")
				print("")
				print("</td>")

			# Session B Paper
			if p[1] is not None:
				fields = p[1].split("|")
				print("<td>")
				print("<strong>")		
				print(fields[0])
				print("</strong><br>")
				print(fields[1])
				print("</td>")
			else:
				print("<td>")
				print("<strong>")		
				print("")
				print("</strong><br>")
				print("")
				print("</td>")
			# Terminate one paper row
			print("</tr>")
	return


parser = argparse.ArgumentParser(description='Parser for FIRRTL simulation of DFGs')

parser.add_argument('--outputfile', '-o', dest='outputfilename', default=None, help='Output directory')

parser.add_argument("--inputfile", '-i', dest='inputfilename', default=None, help='Directory of zip files from ftp://ftp.fec.gov/FEC/electronic/')


args = parser.parse_args()

# Overwrite defaults
if args.outputfilename is not None:
	outputfilename = args.outputfilename

if args.inputfilename is not None:
	inputfilename = args.inputfilename

if __name__ == '__main__':
	 parsecsvprogram(inputfilename)
