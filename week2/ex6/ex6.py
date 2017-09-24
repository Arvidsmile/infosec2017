import sys
import hashlib

K1 = ''
K2 = ''

def readFile(name):
	file = open(name,'r')
	return file.read()

def sha256 ( input ) :
	return (hashlib.sha256(str(input)\
		.encode('utf -8 ')).hexdigest())

def blockText(text):
	blockedText = []
	#Change text to binary and append to list
	for i in range(len(text)):
		# blockedText.append(Base10toBinary(ord(text[i])))
		blockedText.append(ord(text[i]))
	#Create padding at the end of list so 
	#as to make length multiple of 8
	if len(text)%8 != 0:
		#Create marker (byte 128)
		#blockedText.append(Base10toBinary(128))
		blockedText.append(128)
		for i in range(8 - (len(text)%8+1)):
			#pad rest of block with byte 0
			# blockedText.append(Base10toBinary(0))
			blockedText.append(0)
	return blockedText

def feistel(blockedText, round, encryptMode):
	ciphertext = []
	#Determine key
	key = []
	if round < 8:
		for i in range(4):
			key.append(int(K1[round*4+i],16))
	else:
		for i in range(4):
			key.append(int(K2[round*4+i],16))
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
				xorValue =  blockedText[i*8+(4+j)] ^ key[j]
				ciphertext.append(xorValue)
		for j in range(4):
			if encryptMode == True:
				#if encrypting
				#xor left side with key and add to new right side
				xorValue = blockedText[i*8+(j)] ^ key[j]
				ciphertext.append(xorValue)
			else:
				#if decrypting
				#add first 4 bytes (left side) to new right side
				ciphertext.append(blockedText[i*8+j])		
	return ciphertext

def from_bytes (data, big_endian = False):
    if isinstance(data, str):
        data = bytearray(data)
    if big_endian:
        data = reversed(data)
    num = 0
    for offset, byte in enumerate(data):
        num += byte << (offset * 8)
    return num

def intToChar(blockedText):
	text = ''
	print 'Blocked Text'
	print blockedText
	for i in range(len(blockedText)):
		text = text + (chr(blockedText[i]))
	return text

def bytes_from_file(filename):
	array = []
	with open(filename, mode = 'rb') as inputFile:
		byte = inputFile.read(1)
		while byte:
			current = from_bytes(byte)
			array.append(current)
			byte = inputFile.read(1)
		inputFile.close()
	return array

def main():
	key = raw_input("Key: ")
	print key
	K1 = sha256(key)
	print K1
	K2 = sha256(K1)
	print K2
	rounds = input("Num of rounds: ")
	encrypt = raw_input("1 == Encrypt, 0 == Decrypt : ")
	if encrypt == '1':
		encryptMode = True
		text = readFile(sys.argv[1])
		print text
		blockedText = blockText(text);
	else:
		encryptMode = False
		blockedText = bytes_from_file(sys.argv[1])
		print blockedText
	
	for i in range(rounds):
		blockedText = feistel(blockedText, i, encryptMode)
	#Change from binary to String character
	# finalText = binaryArrayToString(blockedText)
	finalText = intToChar(blockedText) 
	print 'Final Text: '
	print finalText

if __name__ == "__main__":
    main()
