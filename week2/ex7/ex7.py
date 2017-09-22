import random

# Generate superincreasing knapsack with 'size' number of values
# Returns a tuple containing the superincreasing knapsack 
# and its current total
def genSuperIncKnapsack(size):
	# initialize array with 0's
	knapsack = [0] * size
	new = 0
	
	# Generate value for knapsack[0]
	knapsack[0] = random.randint(1, 10)
	currentTotal = knapsack[0]
	for i in range(1, size):
		while(new <= currentTotal):	# Every new element is max 5
									# increments away from total
			new = random.randint(currentTotal, currentTotal + 5)
		currentTotal += new
		knapsack[i] = new

	return (knapsack, currentTotal)

# Reference: https://stackoverflow.com/questions/39678984/
# efficient-check-if-two-numbers-are-co-primes-relatively-primes
def greatestCommonDiv(x, y):
	while(y != 0):
		x, y = y, x % y
	return x

def isRelativePrime(x, y):
	return greatestCommonDiv(x, y) == 1

# Takes the current total value (sum of elements) of the superincreasing
# knapsack and finds two numbers that are relatively prime
# that can be used to create the general knapsack, returns
# Returns a tuple of (m, n)
def genMultipliers(currentTotal):
	n = currentTotal + 1 # <-- n must be larger than total sum
	m_n_found = False
	while(m_n_found == False): 	# Start looking for m's at
								# around 1/1000's of n
		for m in range(int(n - n * 0.999), n): 
			if(isRelativePrime(m, n) and (m != 1)):	 	
				multipliers = (m, n)
				m_n_found = True
				break
		# No relative prime found for n (uncertain if this is 
		# mathematically sound...)
		n += 1 # Increment n by 1 and try again..
	return multipliers

# Takes a superincreasingknapsack, multiplier m and modulus n and create
# a general knapsack
def genGeneralKnapsack(superKnapsack, multiplier, modulus):
	length = len(superKnapsack)
	generalKnapsack = [0] * length
	for i in range(length):
		generalKnapsack[i] = (superKnapsack[i] * multiplier) % modulus
	return generalKnapsack

# Find multiplicative inverse of conversion factor m^(-1) % n
# Reference: https://en.wikibooks.org/wiki/
# Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b / a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        print "no modular inverse"
    else:
        return x % m

#############################################################3

### Decryption Code ###

# Takes a private key (superincreasing knapsack) and
# the value to decrypt
def solveSuperKnapsack(superKnap, value):
	binaryMsg = [0] * len(superKnap)
	total = 0
	# Iterate backwards
	for i in range(len(superKnap) - 1, -1, -1):
		test = total + superKnap[i]
		if (test > value):
			continue
		elif(test < value):
			binaryMsg[i] = 1
			total += superKnap[i]
		else:
			binaryMsg[i] = 1
			break
	return binaryMsg

# Take a list of 1's and 0's, split it into blocks of 8 bits,
# convert those lists of size 8 into an integer value and finally
# convert that integer value into a char-type, add this char
# type to the output string
def binaryArrayToString(binaryArray):
	output = ""
	# move 8 steps at a time to grab a character from binaryArray
	for i in range(0, len(binaryArray), 8):
		byte = (binaryArray[i:i+8])
		asciiChr = 0
		for bit in byte:
			asciiChr = (asciiChr << 1) | bit
		print str(asciiChr) + " gives: " + chr(asciiChr)
		output += chr(asciiChr)

	return output

###########################################################

# Everything is ready, lets make a public and private key:
#. Public key, superKnapsack is a tuple (see line 3-5)
superKnapsack = genSuperIncKnapsack(int(raw_input("Size of knapsack: ")))
m_n = genMultipliers(superKnapsack[1])

print "~~~~~~~~~ Public Key: ~~~~~~~~~"
print "multiplier(m) = " + str(m_n[0]) + " modulo(n) = " + str(m_n[1])
print "m and n are relative prime: " + str(isRelativePrime(m_n[0], m_n[1]))
generalKnapsack = genGeneralKnapsack(superKnapsack[0], m_n[0], m_n[1])
print "General Knapsack: "
print generalKnapsack
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "~~~~~~~~~ Private Key: ~~~~~~~"
print superKnapsack[0]
multInv = modinv(m_n[0], m_n[1])
print "Multiplicative inverse : m^-1 mod n = " + str(multInv)
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~"

# --------------------------------------------
# Hardcoded values that are related to the key sent to Teacher Assistant
myPublicKey = [104, 208, 728, 1144, 2704, 
5304, 10608, 21320, 42640, 85280, 
65631, 26333, 52562, 104812, 78, 156]

myMultiplier = 104,
myModulo = 104929

myPrivateKey = [1, 2, 7, 11, 26, 51, 102, 205, 410, 
			820, 1640, 3280, 6559, 13115, 26233, 52466]
myMultInv = 15134
# --------------------------------------------

print "\n---------- 	DECRYPTION	--------------\n"
### Time to decrypt message from TA ###
#1. Read file
file = open("encrypted", 'r')

#2. Decrypt block by block until end of file
plainText = ""
for line in file:
	# Decrypted values appear as hex, so we convert to decimal
	val = (int(line, 16) * myMultInv) % myModulo 
	solution = solveSuperKnapsack(myPrivateKey, val)
	# (Due to my own misunderstanding of the exercise this
	# reversed(...) call is necessary for decryption to work properly)
	plainText += binaryArrayToString(list(reversed(solution)))

#3. Display the decrypted text
print plainText

# Output:
# The Bosnian War was an international armed conflict that took
#  place in Bosnia and Herzegovina between 1992 and 1995. 
#  Following a number of violent incidents in early 1992, 
#  the war is commonly viewed as having started on 6 April 1992. 
#  The war ended on 14 December 1995. The main belligerents were 
#  the forces of the Republic of Bosnia and Herzegovina and those 
#  of the self-proclaimed Bosnian Serb and Bosnian Croat entities 
#  within Bosnia and Herzegovina, Republika Srpska and Herzeg-Bosnia, 
#  which were led and supplied by Serbia and Croatia, respectively.