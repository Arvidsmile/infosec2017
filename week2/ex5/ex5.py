
# Define globals
plainText = "informationsecurity"
key = "vlaksjdhfgqodzmxncb"

# Function vernam takes two strings "..." as arguments
# and returns the string representation 
# of encrypted/decrypted text
def vernam(plain_or_cipher, key):
	#0. Make sure lengths match
	if (len(plain_or_cipher) != len(key)):
		print "Key and text are not of same length!"
		return

	#1. Convert text and key to ASCII representation
	textASCII = [ord(c) for c in plain_or_cipher]
	keyASCII = [ord(c) for c in key]

	#2. Perform XOR operation (vernam cipher)
	output = ""
	for idx in range(len(textASCII)):
		# Perform XOR, then convert to char-type 
		# and add to output string
		output += (chr(textASCII[idx] ^ keyASCII[idx]))

	return output

# Takes a string "..." and prints out either an array of
# ascii-values or the argument (in string format)
def displayText(text):
	# Non displayable ascii characters have values below 32

	# REFERENCE: https://www.juniper.net/documentation/en_US/idp5.1/
	# topics/reference/general/intrusion-detection-prevention-custom-
	# attack-object-extended-ascii.html

	for chr in text:
		if (ord(chr) < 32):
			print [ord(c) for c in text] #<-- convert to array
			return						# of ascii and print
			
	# else, display normally
	print text

# Perform encryption and decryption using 'key'
cipherText = vernam(plainText, key)
originalText = vernam(cipherText, key)

# Display the results
displayText(originalText)
displayText(cipherText)