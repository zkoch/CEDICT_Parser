# coding=utf-8
# char codes ref from: http://www.math.nus.edu.sg/aslaksen/read.shtml

TONES = { "1a":"&#257;", "2a":"&#225;", "3a":"&#462;", "4a":"&#224;", 
		  "1e":"&#275;", "2e":"&#233;", "3e":"&#283;", "4e":"&#232;", 
		  "1i":"&#299;", "2i":"&#237;", "3i":"&#464;", "4i":"&#236;",
		  "1o":"&#333;", "2o":"&#243;", "3o":"&#466;", "4o":"&#242",
		  "1u":"&#363;", "2u":"&#250;", "3u":"&#468;", "4u":"&#249;",
		  "1v":"&#470;", "2v":"&#472;", "3v":"&#474;", "4v":"&#476;" }
		  # using v for the umlauded u

def convert(s):
	word_list = []
	ret_string = ""
	tmp = ""
	# split the string by spaces
	words = s.split(" ")
	
	# "zhong1 guo2" -> [ ['1', 'zhong'], ['2', 'guo'] ]
	for word in words:
		word_list.append([word[len(word)-1], word[0:len(word)-1]])
		
	# do the searchy stuff
	for word in word_list:
		tone = word[0]
		pinyin = word[1].lower()
		
		if tone == "5" or pinyin == "":
			break
		
		if pinyin.find("a") > -1:
			tmp = pinyin.replace("a", TONES[tone+"a"])
			
		elif pinyin.find("e") > -1:
			tmp = pinyin.replace("e", TONES[tone+"e"])
			
		elif pinyin.find("ou") > -1:
			tmp = pinyin.replace("o", TONES[tone+"o"]+"u")
			
		elif pinyin.find("io") > -1:
			tmp = pinyin.replace("io", "i"+TONES[tone+"o"])
		
		elif pinyin.find("iu") > -1:
			tmp = pinyin.replace("iu", "i"+TONES[tone+"u"])
			
		elif pinyin.find("ui") > -1:
			tmp = pinyin.replace("ui", "u"+TONES[tone+"i"])
			
		elif pinyin.find("uo") > -1:
			tmp = pinyin.replace("uo", "u"+TONES[tone+"o"])
			
		elif pinyin.find("i") > -1:
			tmp = pinyin.replace("i", TONES[tone+"i"])
		
		elif pinyin.find("o") > -1:
			tmp = pinyin.replace("o", TONES[tone+"o"])
			
		elif pinyin.find("u:") > -1:
			tmp = pinyin.replace("u:", TONES[tone+"v"])
			
		elif pinyin.find("u") > -1:
			tmp = pinyin.replace("u", TONES[tone + "u"])
			
		else:
			tmp = pinyin
		
		ret_string += tmp + " "

	return ret_string