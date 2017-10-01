from modinv import modinv
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

# m = int(raw_input("multiplier: "))
# a = int(raw_input("a: "))
# mod = int(raw_input("modulus: "))
# point = (int(raw_input("pointX: ")), int(raw_input("pointY: ")))

# On curve : y^2 = x^3 + ax + b % modulus
# given multiplier (scalar) and a point(Xp, Yp)
# to be multiplied by repeated addition
def ellipticCurveMult(multiplier, point, a, modulus):
	increment = point
	for i in range(multiplier - 1):
		print point
		point = ellipticCurveAddition(point, increment, a, modulus)
	return point

# Fast multiplication 

a = 11
point = (2, 7)
m = 15
mod = 167

print "15 * 2, 7) = " + str(ellipticCurveMult(m, point, a, mod))

# Find high bit points
# Given a multiplier and a point, compute all
# additions and return a list of the ones corresponding
# to the position with a high-bit in the multiplier
def findHighBitPoints():
	pass

# Given a list of all points which had a high bit
def recAdd(a, mod, list):
	print list
	if(len(list) == 2):
		return ellipticCurveAddition(list[0], list[1], a, mod)
	else:
		point = list[0]
		return ellipticCurveAddition(\
			recAdd(a, mod, list[1:]), point, a, mod)	

print "Recursive addition"
print recAdd(11, 167, [P1, P2, P3, P4])

