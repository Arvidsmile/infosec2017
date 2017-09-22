import sys

K1 = '184b4d16bbe3200c5a5f500cc09efa68cddd42cbda27c1e49fa7a0f2e2735007'
K2 = 'bd11fd28eabd0b87f2ff4595a50041bfb882bbf8ae058ea5d677c7da07d43786'
def readFile(name):
	file = open(name,'r')
	return file.read()

def Base10toBinary(char):
	array = format(ord(char), '08b')
	#number = bin(ord(char))
	return array

def Base16toBinary(char1):
	#number = ( bin(int(char1, 16))[2:] ).zfill(8)
	#number2 = ( bin(int(char2, 16))[2:] ).zfill(8)
	number = format((int(char1, 16)), '08b')
	#number2 = format((int(char2, 16)), '08b')
	#print int(char1, 16)
	#print number
	#print number2
	return [number]

def blockText(text):
	blockedText = []
	#Change text to binary and append to list
	for i in range(len(text)):
		blockedText.append(Base10toBinary(text[i]))
	#Create padding at the end of list so 
	#as to make length multiple of 8
	if len(text)%8 != 0:
		#blockedText.append(Base10toBinary(chr(128)))
		blockedText.append(format(128,'08b'))
		for i in range(len(text)%8-1):
			#blockedText.append(Base10toBinary(chr(0)))
			blockedText.append(format(0,'08b'))
	return blockedText

def feistel(blockedText, round):
	ciphertext = []
	#Determine key
	key = []
	if round < 8:
		for i in range(4):
			key = key + Base16toBinary(K1[round*4+i])
	else:
		for i in range(4):
			key = key + Base16toBinary(K1[round*4+i])
	print key
	#Encrypt
	for i in range(len(blockedText)/8):
		newLeft = []
		oldLeft = []
		newRight = []
		for j in range(4):
			#add latter 4 bytes (right side) to new left side
			newLeft = newLeft + [blockedText[i*8+(4+j)]]
			print newLeft
			#Collect old Left into a list 
			newRight = xor([blockedText[i*8+j]], key[j])
			oldLeft = oldLeft + [blockedText[i*8+j]]
		for k in range(4):
			newRight[k] = oldLeft[k]
	return ciphertext

def xor(byte, key):
	result = []
	for i in range(len(byte)):
		#change from string to bits
		if byte[i] == '0':
			bit1 = 0;
		else:
			bit1 = 1
		if key[i] == '0':
			bit2 = 0
		else:
			bit2 = 1
		#xor
		xorbit = bit1 ^ bit2
		print 'xorbit'
		print xorbit
		result = result + [xorbit]
	print 'result' 
	print result

def main():
	rounds = input("Num of rounds: ")
	encrypt = raw_input("1 == Encrypt, 0 == Decrypt : ")	
	text = readFile(sys.argv[1])
	print "Original text: " + text + "\n"
	blockedText = blockText(text);
	print blockedText
	for i in range(rounds):
		ciphertext = feistel(blockedText, i)

		

if __name__ == "__main__":
    main()
