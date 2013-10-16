#! /usr/local/bin/python
import fileinput
import re

DATA_DIR = "/home/localbox/src/csf-data"

f = open(DATA_DIR+'/github-names.txt', 'a')

p = re.compile('[\s]*https://github.com/([\w]*)/([\w]*)')

for line in fileinput.input():
	m = p.match(line)
#	f.write(line)
	if (m != None):
		sender = m.group(1)
		repo = m.group(2)
		f.write(sender+" "+repo+"\n")

f.close()
