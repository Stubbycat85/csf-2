#! /usr/local/bin/python
import fileinput
import re

# Normalize github URLs (remove the subscription from the end)

DATA_DIR = "/home/localbox/src/csf-data"

f = open(DATA_DIR+'/github-ssh-remotes.txt', 'a')

p = re.compile('[\s]*https://github.com/([\w]*)/([\w]*)(/subscription)*')

for line in fileinput.input():
	m = p.match(line)
#	f.write(line)
	if (m != None):
		username = m.group(1)
		repo = m.group(2)
		f.write("git@github.com:"+username+"/"+repo+"\n")

f.close()
