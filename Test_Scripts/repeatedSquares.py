def repeatedSquaresModulus(base, exponent, modulus):
	# Reference: Stamp's Book, page 99

	#1. Find exponent in binary
	binStr = str(bin(exponent)[2::]) #skip the '0b'-part

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

base = int(raw_input("Base: "))
exp = int(raw_input("Exponent: "))
mod = int(raw_input("Modulus: "))

print repeatedSquaresModulus(base, exp, mod)

