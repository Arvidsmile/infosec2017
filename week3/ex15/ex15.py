from modinv import modinv

# Global used to track amount of addition-operations
numAdditions = 0

# Stamp's algorithm for adding two points
# P3(x3, y3) = P1(x1, y1) + P(x2, y2)
# -- Adding two points on an elliptic curve:

# Arguments: Two tuples p1 and p2 to be added
# Returns: One tuple p3 containing
# the new (x, y)-coordinates
def isEqual(p1, p2):
	if(p1[0] == p2[0] and p1[1] == p2[1]):
		return True
	return False

# Assuming a curve y^2 = x^3 + ax + b (% mod)
# p1 is the Pi with smallest Xi, p1[0] < p2[0]
def ellipticCurveAddition(p1, p2, a, mod):
	#0. Check the smallest Xi
	if (p1[0] > p2[0]):
		p1, p2 = p2, p1 # tuple swap (of tuples)

	#1. Calculate 'm'
	m = 0
	if(isEqual(p1, p2)):
		m = (3 * pow(p1[0], 2) + a) * \
			modinv(2 * p1[1], mod) % mod
	else:
		m = (p2[1] - p1[1]) * \
			modinv((p2[0] - p1[0]), mod) % mod

	x3 = 0
	y3 = 0
	# x3 = (m^2 - x1 - x2) % mod
	x3 = (pow(m, 2) - p1[0] - p2[0]) % mod
	# y3 = (m(x1 - x3) - y1) % mod
	y3 = ( m * (p1[0] - x3) - p1[1]) % mod

	return (x3, y3)

# "Naive multiplier"
def ellipticCurveMult(multiplier, point, a, modulus):
	increment = point
	for i in range(multiplier - 1):
		point = ellipticCurveAddition(point, increment, a, modulus)
	return point

# Find high bit points
# Given a multiplier and a point, compute all
# additions and return a list of the ones corresponding
# to the position with a high-bit in the multiplier
def findHighBitPoints(point, a, modulus, multiplier):
	global numAdditions
	binM = bin(multiplier)[2:]
	sumList = [0] * len(binM)
	sumList[0] = point
	orderedOutput = []

	# Starting with the least significant bit
	binM = list(reversed(binM))
	
	for i in range(1, len(binM)):
		prev = sumList[i-1]
		sumList[i] = ellipticCurveAddition(prev, prev, a, modulus)
		numAdditions += 1 #<-- track the amount of additions

	for i in range(len(binM)):
		if(binM[i] == '1'):
			orderedOutput.append(sumList[i])

	return orderedOutput

# Given a list of all points which had a high bit
# and recursively add them together like in hidden
# slide 51 from week 3
def recECCAdd(a, mod, list):
	global numAdditions
	if(len(list) == 2):
		numAdditions += 1 #<-- track the amount of additions
		return ellipticCurveAddition(list[0], list[1], a, mod)
	else:
		point = list[0]
		numAdditions += 1 #<-- track the amount of additions
		return ellipticCurveAddition(\
			recECCAdd(a, mod, list[1:]), point, a, mod)	

# Fast multiplication using the bits of the multiplier
# Returns the point as a tuple
def fastECCMultiplier(point, a, modulus, multiplier):
	return recECCAdd(a, modulus, \
		findHighBitPoints(point, a, modulus, multiplier))

#### Answers to questions ####

# Public Key
a = 3
b = 5
mod = 157
MyPoint = (4, 9)

# Private key
m = 24

# MyPoint_m = (19, 135)
MyPoint_m = fastECCMultiplier(MyPoint, a, mod, m)

# Point sent from TA
TAPoint = (79, 12) # = n * (4, 9)

SharedSecret = fastECCMultiplier(TAPoint, a, mod, m)
print SharedSecret