import sys
#sha256sum for 'Feistel'
#K1 = '184b4d16bbe3200c5a5f500cc09efa68cddd42cbda27c1e49fa7a0f2e2735007'
#K2 = 'bd11fd28eabd0b87f2ff4595a50041bfb882bbf8ae058ea5d677c7da07d43786'
#sha256sum for 'The Feistel Cipher'
K1 = '9b3fab6d542dafc4dec9ed03243b63ff672ba11c955a7feb9c3893093ad83ae9'
K2 = 'a4cb34202540541b95fd86ad5fbe2b9c85388adadab4d476741f48058af91be5'
def readFile(name):
	file = open(name,'r')
	return file.read()

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
	#number = bin(ord(char))
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
	print 'key'
	print key
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
		#change from string to bits
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
	rounds = input("Num of rounds: ")
	encrypt = raw_input("1 == Encrypt, 0 == Decrypt : ")
	if encrypt == 1:
		encryptMode = True
	else:
		encryptMode = False
	text = readFile(sys.argv[1])
	print "Original text: " + text + "\n"
	blockedText = blockText(text);
	print blockedText
	for i in range(rounds):
		blockedText = feistel(blockedText, i, encryptMode)
		print 'encrypted blockedText'
		print blockedText
	print 'processed text'
	finalText = binaryArrayToString(blockedText)
	print finalText

	#reverse
	#for i in range(rounds):
	#	blockedText = feistel(blockedText, i, encryptMode == False)
	#	print 'encrypted blockedText'
	#	print blockedText
	#print 'processed text'
	#finalText = binaryArrayToString(blockedText)
	#print finalText



if __name__ == "__main__":
    main()
