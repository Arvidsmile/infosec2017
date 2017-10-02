def checkIfPresent(c, factors): 
#Determine if number is already present
	if len(factors) != 0:
		for i in range(len(factors)):
			if c == factors[i]:
				return factors
	factors.append(c)
	return factors
    
def prime_factors(n): 
#Determine prime factors
	number = n
	i = 2
	factors = []
	while i*i <=n:
		if n%i:
			i+=1
		else:
			n //= i
			factors = checkIfPresent(i,factors)
	if n > 1:
		if n != number:
			factors = checkIfPresent(n,factors)
	return factors

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

def generators(pf, p):
	#Determine generators
	gener = []
	for g in range(2,p):
		flag = 0
		for x in pf:
			if repeatedSquaresRec(g, (p-1)/x, p) == 1:
				flag = 1
				break
		if flag == 0:
			gener.append(g)
	return gener

def main():
	prime = input("Prime: ")
	factors = []
	factors = prime_factors(prime-1)
	print factors
	gener = generators(factors,prime)
	print gener #<-- remove [-1] to show all generators

if __name__ == "__main__":
    main()
