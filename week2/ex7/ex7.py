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

# Takes the current total value of the superincreasing
# knapsack and finds two numbers that are relatively prime
# that can be used to create the general knapsack, returns
# Returns a tuple of (m, n)
def genMultipliers(currentTotal):
	n = currentTotal + 1
	m_n_found = False
	while(m_n_found == False):
		for m in range(int(n - n * 0.999), n): 
			if(isRelativePrime(m, n) and (m != 1)):	 	
				multipliers = (m, n)
				m_n_found = True
				break
		# No relative prime found for n (uncertain if this is 
		# mathematically sound)
		n += 1
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



print "TEST"
print genGeneralKnapsack([2, 3, 7, 14, 30, 57, 120, 251], 41, 491)
print modinv(41, 491)