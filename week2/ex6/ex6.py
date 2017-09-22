import sys

K1 = '184b4d16bbe3200c5a5f500cc09efa68cddd42cbda27c1e49fa7a0f2e2735007'
K2 = 'bd11fd28eabd0b87f2ff4595a50041bfb882bbf8ae058ea5d677c7da07d43786'
def readFile(name):
	file = open(name,'r')
	return file.read()

def Base10toBinary(char):
	#array = format(ord(char), '08b')
	number = bin(ord(char))
	return number

def Base16toBinary(char1, char2):
	number = ( bin(int(char1, 16))[2:] ).zfill(8)
	number2 = ( bin(int(char2, 16))[2:] ).zfill(8)
	print number
	print number2
	return [number, number2]

def blockText(text):
	blockedText = []
	#Change text to binary and append to list
	for i in range(len(text)):
		blockedText.append(Base10toBinary(text[i]))
	#Create padding at the end of list so 
	#as to make length multiple of 8
	if len(text)%8 != 0:
		blockedText.append(Base10toBinary(chr(128)))
		for i in range(len(text)%8-1):
			blockedText.append(Base10toBinary(chr(0)))
	return blockedText

def feistel(blockedText, round):
	ciphertext = []
	#Determine key
	if round < 8:
		key = Base16toBinary(K1[round*2], K1[round*2+1])
	else:
		key = Base16toBinary(K2[round*2], K2[round*2+1])
	#Encrypt
	for i in range(len(blockedText)/8):
		newLeft = []
		oldLeft = []
		newRight = []
		for j in range(4):
			#add latter 4 bytes (right side) to new left side
			newLeft = newLeft + [blockedText[i*8+(4+j)]]
			#Collect old Left into a list 
			oldLeft = oldLeft + [blockedText[i*8+j]]
		for k in range(4):
			newRight[k] = oldLeft[k]
	return ciphertext


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
