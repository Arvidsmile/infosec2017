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
		m = (3 * pow(p1[0], 2) + a) * modinv(2 * p1[1], mod) % mod
	else:
		m = (p2[1] - p1[1]) * modinv((p2[0] - p1[0]), mod) % mod

	x3 = 0
	y3 = 0
	# x3 = (m^2 - x1 - x2) % mod
	x3 = (pow(m, 2) - p1[0] - p2[0]) % mod
	# y3 = (m(x1 - x3) - y1) % mod
	y3 = ( m * (p1[0] - x3) - p1[1]) % mod

	return (x3, y3)

# Book test-case:
p1 = (1, 4)
p2 = (3, 1)
mod = 5
a = 2

# (2, 0) = (1, 4) + (3, 1)
#print ellipticCurveAddition(p1, p2, a, mod)

# (? , ?) = (1, 4) * 2
#print ellipticCurveAddition(p1, p1, a, mod)

result = (2, 7)
for i in range(16):
	print result
	result = ellipticCurveAddition(result, result, 11, 167)

print result




