# coding=utf-8
# the above line is necessary to tell python what kind of encoding we're working with
# see: http://www.python.org/dev/peps/pep-0263/

from pinyin import *

def write_file(file_name, dic):
	new_file = open(file_name, 'w')
	
	new_file.write("var CH_DIC = function() {")
	new_file.write("\n\n")
	new_file.write("\tthis._table = {")
	new_file.write("\n\n")
	
	for item in dic:
		try:
			new_file.write("\t\t")
			new_file.write("\"" + item["hanzi"] + "\":")
			new_file.write(" \"" + item["pinyin"] + "|" + item["def"] + "\",")
			new_file.write('\n')
		except:
			print "Something went wrong"
	
	new_file.write("\n")
	new_file.write("\t}")
	new_file.write("\n\n")
	new_file.write("}")
	
	new_file.close()
	
def read_file(file_name):
	
	# EXAMPLE INPUT LINE:   㐖 㐖 [Ye4] /see
	# TRADITIONAL_HANZI SIMPLIFIED_HANZI [PINYIN] /TRANSLATION
	
	# Put each dictionary item into the array
	items = []

	f = open(file_name, "r")
	lines = f.readlines()
	
	for line in lines:
		l = line
		
		#These are info lines at the beginning of the file
		#NOTE: Might be useful to store version #, date, etc for dictionary reference
		if l.startswith(("#", "#!")):
			continue
		else:
			#partition out definition text, replace slshes with semicolons, normalize quotations, get rid of any \n
			defi = l.partition('/')[2].replace('/','; ').replace("\"", "'").strip()
			#Get trad and simpl hanzis then split and take only the simplified
			han = l.partition('[')[0].split(' ', 1)[1].strip(" ")
			#Take the content in between the two brackets
			pin = l.partition('[')[2].partition(']')[0]
			
			pin = convert(pin);			
			
			items.append({"hanzi":han, "pinyin":pin, "def":defi})
	
	write_file("CH_DIC.js", items)
		
read_file("cedict_ts.u8")