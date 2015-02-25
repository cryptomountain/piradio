#!/usr/bin/env python
#
# ir.conf Generator
# 
# $Id: genir.py v 1.00 2015/02/24 joe Exp $
# 
# Author : Joe Culbreth
# Site   : http://www.javatron.org
#
# This program will generate ir.conf ( lircs conf file for pylirc init funtion) file from a lircd.conf file
# 
# License: GNU V3, See https://www.gnu.org/copyleft/gpl.html
#
# Disclaimer: Software is provided as is and absolutly no warranties are implied or given.
#	     The authors shall not be liable for any loss or damage however caused.
#
import os
import sys
import string
import traceback
from string import Template

infile = "audiotron_remote_lirc.conf"
remote = "*"
prog = "radio"

block = Template("""begin
  remote = $r
  button = $b
  prog = $p
  config = $c
end""")

irfile = open(infile,"r")
line = ""
output = ""
while(line != "begin codes"):
	line = irfile.readline().strip()
while(line != "end codes"):
	line = irfile.readline().strip()
	begin = line.find("KEY_")
	if(begin < 0):
		begin = line.find("BTN_")
		if (begin < 0):
			continue
	end = line.find(" ",begin+4)
	button = line[begin:end]
	config = line[begin+4:end].lower()
	output += block.substitute( r=remote,b=button,p=prog,c=config) + "\n"
irfile.close()

print output
outfile = open("ir.conf","w")
outfile.write(output)
outfile.close()


