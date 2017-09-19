#!/usr/bin/python

import sys

def readFile(name):
	file = open(name,'r')
	return file.read()
	
def substitute(text, o, d, key):
	print '-----------------------'
	print "(KEY LENGTH SHOULD BE SIZE OF ALPHABET)"
	print "Key length: " + str(len(key)) + "/n"
	if key == None or len(key) < 26:
		print "Error: Appropriate key not given."
		print "Text not converted.\n"
		print "-----------------------\n"
		return
	else:
		print "Key:"
		print "abcdefghijklmnopqrstuvwxyz"
		print "|"
		print "V"
		print key
	print "\n"
	if d == True:
		print "Decrypt"
	else:
		print "Encrypt"
	print "\n"
	if o == True:
		print "Keep non-letters, honor casing"
	else:
		print "Ignore non lower-case letters"
	print "-----------------------\n"
	text2 = ""
	for ch in text:
		if d == False: #If encrypting
			if o == False:
				if ord(ch) >= ord('a') and ord(ch) <= ord('z'): #If lowercase
					text2 += key[(ord(ch)-ord('a'))%len(key)]
				elif ord(ch) >= ord('A') or ord(ch) <= ord('Z'): #If upper-case
					text2 += key[(ord(ch)-ord('A'))%len(key)]
			else:
				#Keep non-letters and Honor casing
				if ord(ch) >= ord('a') and ord(ch) <= ord('z'): #If lowercase
					text2 += key[(ord(ch)-ord('a'))%len(key)]
				elif ord(ch) >= ord('A') or ord(ch) <= ord('Z'): #If upper-case
					text2 += key[(ord(ch)-ord('A'))%len(key)]
				else: #If non-letter symbol
					text2 += ch
		else: #If decrypting
			if o == False:
				if ord(ch) >= ord('a') or ord(ch) <= ord('z'): #If lowercase
					pos = 0 #Count position
					for l in key:
						if l == ch:
							text2 += chr(ord('a') + pos)
							break
						pos = pos+1
				elif ord(ch) >= ord('A') and ord(ch) <= ord('Z'): #If upper-case
					pos = 0 #Count position
					for l in key:
						if chr(ord(l) - (ord('a') - ord('A'))) == ch:
							text2 += chr(ord('a') + pos)
							break
						pos = pos+1;
			else:
				if ord(ch) >= ord('a') and ord(ch) <= ord('z'): #If lowercase
					pos = 0 #Count position
					for l in key:
						if l == ch:
							text2 += chr(ord('a') + pos)
							break
						pos = pos+1
				elif ord(ch) >= ord('A') and ord(ch) <= ord('Z'): #If upper-case
					pos = 0 #Count position
					for l in key:
						if chr(ord(l) - (ord('a') - ord('A'))) == ch:
							text2 += chr(ord('A') + pos)
							break
						pos = pos+1
				else: #If non-letter symbol
					text2 += ch
	print "Processed text:\n"
	print text2
				

def main():
	text = readFile(sys.argv[1])
	print "Original text" + text + "\n"
	if len(sys.argv) > 2 and sys.argv[2] == "-o":
		if len(sys.argv) > 3 and sys.argv[3] == "-d":
			converted = substitute(text, True, True, sys.argv[4])
		else:
			converted = substitute(text, True, False, sys.argv[3])
	elif len(sys.argv) > 2 and sys.argv[2] == "-d":
		converted = substitute(text, False, True, sys.argv[3])
	elif len(sys.argv) > 2:
		converted = substitute(text, False, False, sys.argv[2])
	else:
		converted = substitute(text, False, False, None)
				

if __name__ == "__main__":
    main()
