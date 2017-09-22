import sys
import hashlib

K1 = 'c73b13d07b16bf503b19aa9055b9951b5e899116383ef115982b8b7a6c54f0f4'
K2 = '5d3e6edec3a7e8594a3ede60242f8ae98de5993b23dcbe6896df3f76c1eef132'

def readFile(name):
	file = open(name,'r')
	return file.read()

def sha256 ( input ) :
	input = ' '. join ( input )
	return list ( hashlib . sha256 ( str ( input ) . encode ('utf -8 ') ) . hexdigest () )

def Base10toBinary(integer):
	array = format(integer, '08b')
	li = []
	for i in range(len(array)):
		#change from string to bits
		if array[i] == '0':
			bit1 = 0;
		else:
			bit1 = 1
		li.append(bit1)
	return li

def Base16toBinary(char1):
	array = format((int(char1, 16)), '08b')
	li = []
	for i in range(len(array)):
		#change from string to bits
		if array[i] == '0':
			bit1 = 0;
		else:
			bit1 = 1
		li.append(bit1)
	return li


def blockText(text):
	blockedText = []
	#Change text to binary and append to list
	for i in range(len(text)):
		blockedText.append(Base10toBinary(ord(text[i])))
	#Create padding at the end of list so 
	#as to make length multiple of 8
	if len(text)%8 != 0:
		#Create marker (byte 128)
		blockedText.append(Base10toBinary(128))
		for i in range(8 - (len(text)%8+1)):
			#pad rest of block with byte 0
			blockedText.append(Base10toBinary(0))
	return blockedText

def feistel(blockedText, round, encryptMode):
	ciphertext = []
	#Determine key
	key = []
	if round < 8:
		for i in range(4):
			key.append(Base16toBinary(K1[round*4+i]))
	else:
		for i in range(4):
			key.append(Base16toBinary(K2[round*4+i]))
	#Encrypt
	for i in range(len(blockedText)/8):
		newLeft = []
		newRight = []
		newBlock = []
		for j in range(4):
			#New Left-side
			if encryptMode == True:
				#if encrypting
				#add latter 4 bytes (right side) to new left side
				ciphertext.append(blockedText[i*8+(4+j)])
			else:
				#if decrypting
				#xor right side with key and add to new left side
				xorValue = xor(blockedText[i*8+(4+j)], key[j])
				ciphertext.append(xorValue)
		for j in range(4):
			if encryptMode == True:
				#if encrypting
				#xor left side with key and add to new right side
				xorValue = xor(blockedText[i*8+j], key[j])
				ciphertext.append(xorValue)
			else:
				#if decrypting
				#add first 4 bytes (left side) to new right side
				ciphertext.append(blockedText[i*8+j])		
	return ciphertext

def xor(byte, key):
	result = []
	for i in range(len(byte)):
		#xor
		xorbit = byte[i] ^ key[i]
		result.append(xorbit)
	return result

def binaryArrayToString(blockedText):
	binaryArray = sum(blockedText,[])
	output = ""
	# move 8 steps at a time to grab a character from binaryArray
	for i in range(0, len(binaryArray), 8):
		byte = (binaryArray[i:i+8])
		asciiChr = 0
		for bit in byte:
			asciiChr = (asciiChr << 1) | bit
		output += chr(asciiChr)
	return output

def main():
	# key = raw_input("Key: ")
	# print key
	# K1 = sha256(key)
	# print K1
	# K2 = sha256(K1)
	rounds = input("Num of rounds: ")
	encrypt = raw_input("1 == Encrypt, 0 == Decrypt : ")
	if encrypt == 1:
		encryptMode = True
	else:
		encryptMode = False
	text = readFile(sys.argv[1])
	print 'Original Text: '
	print text
	blockedText = blockText(text);
	for i in range(rounds):
		blockedText = feistel(blockedText, i, encryptMode)
	#Change from binary to String character
	finalText = binaryArrayToString(blockedText)
	print 'Final Text: '
	print finalText

if __name__ == "__main__":
    main()
