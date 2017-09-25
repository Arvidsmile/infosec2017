import sys
import hashlib

def readFile(name):
	file = open(name,'r')
	return file.read()

def sha256 ( input ) :
	return (hashlib.sha256(str(input)\
		.encode('utf -8 ')).hexdigest())

def processText(text):
	blockedText = []
	#Change text to binary and append to list
	for i in range(len(text)):
		blockedText.append(ord(text[i]))
	#Create padding at the end of list so 
	#as to make length multiple of 8
	if len(text)%8 != 0:
		#Create marker (byte 128)
		blockedText.append(128)
		for i in range(8 - (len(text)%8+1)):
			#pad rest of block with byte 0
			blockedText.append(0)
	return blockedText

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

def feistel(blockedText, round, totalRounds, encryptMode, K1):
	ciphertext = []
	#Determine key
	key = []
	if encryptMode == True:
		#Read key forwards if encrypting
		for i in range(0,4):
			hexa = K1[(round*8)+(i*2)] + K1[(round*8)+(i*2)+1]
			key.append(int(hexa,16))
	else:
		#Read key backwards in steps of 4 if decrypting 
		for i in range(0,4):
			hexa = K1[(totalRounds -1 - round)*8+(i*2)] + \
				K1[(totalRounds -1 - round)*8+(i*2)+1]
			key.append(int(hexa,16))
	#Encrypt
	for i in range(len(blockedText)/8):
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
			#New Right side
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

def main():
	key = raw_input("Key: ")
	K1 = sha256(key) + sha256(sha256(key))
	rounds = input("Num of rounds: ")
	encrypt = raw_input("1 == Encrypt, 0 == Decrypt : ")
	if encrypt == '1':
		encryptMode = True
		text = readFile(sys.argv[1])
		blockedText = processText(text);
		print 'Original text: '
		print text
	else:
		encryptMode = False
		blockedText = bytes_from_file(sys.argv[1])
	for i in range(rounds):
		blockedText = feistel(blockedText, i, rounds, encryptMode, K1)
	#Change from int to String character
	finalText = intToChar(blockedText) 
	print 'Final Text: '
	print finalText

if __name__ == "__main__":
    main()
