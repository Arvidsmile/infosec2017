from timeit import default_timer as timer

# Function used for reference since pythons
# pow() is using some optimizations
def naiveEponentiation(base, exponent):
	for i in range(exponent-1):
		base *= exponent
	return base

def repeatedSquaresIter(base, exponent, modulus):
	# Reference: Stamp's Book, page 99

	#1. Find exponent in binary
	binStr = bin(exponent)[2::] #skip the '0b'-part

	#2. Initialize values
	exponent = 0
	output = 0

	#3. Loop through binStr from MSB to LSB
	for bit in binStr:
		output = pow(pow(base, exponent), 2)
		#4. Calculate new exponent
		exponent = (exponent * 2)

		if(bit == '1'):
			output *= base
			exponent += 1
		output = (output % modulus)

	return output

def repeatedSquaresRec(base, exponent, modulus):
	# base case
	if(exponent == 1):
		return base % modulus
	# recursive step
	else:
		returned = repeatedSquaresRec(base, exponent / 2, modulus)
		returned = returned * returned % modulus
		if(exponent % 2 != 0):
			returned = returned * base % modulus
	return returned % modulus 

base = int(raw_input("Base: "))
exp = int(raw_input("Exponent: "))
mod = int(raw_input("Modulus: "))

timeRec = timer()
print repeatedSquaresRec(base, exp, mod)
timeRec = (timer() - timeRec)

timeIter = timer()
print repeatedSquaresIter(base, exp, mod)
timeIter = (timer() - timeIter)

# timeNaive = timer()
# print naiveEponentiation(base, exp) % mod
# timeNaive = (timer() - timeNaive)

print "Recursive = " + str(timeRec)
print "Iterative = " + str(timeIter)
# print "Naive = " + str(timeNaive)


