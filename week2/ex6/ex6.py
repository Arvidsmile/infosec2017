#!/usr/bin/python
import sys

def readFile(name):
	file = open(name,'r')
	return file.read()

def toBinary(char):
	array = format(ord(char), '08b')
	return array

def blockText(text):
	blockedText = []
	j = 0;
	for i in range(len(text)/8+1):
		block = [0]*8
		for j in range(8):
			if i*8+j < len(text):
				block[j] = toBinary(text[i*8+j])
			else:
				block[j] = '00000000'
		blockedText.append(block)
	return blockedText

def feistel(blockedText):
	ciphertext = blockedText
	print len(blockedText[1])
	print len(blockedText[2])
	for i in range(len(blockedText)):
		for j in range(len(blockText[1])):
			break
	return ciphertext


def main():
	K1 = raw_input("Input sha256sum 1: ")
	K2 = raw_input("Input sha256sum 2: ")
	encrypt = input("1 == Encrypt, 0 == Decrypt : ")	
	text = readFile(sys.argv[1])
	print "Original text: " + text + "\n"
	blockedText = blockText(text);
	print blockedText
	ciphertext = feistel(blockedText)

		

if __name__ == "__main__":
    main()
