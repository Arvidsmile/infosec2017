import math
import numpy

#### MANAGE FILES ####

#1. Read the file and store as one string
file1 = open("testtext", 'r').read() 
cipherText = open("ciphertext", 'r').read()

#1.1	Remove all '\n's from text
file1 = file1.replace('\n', '')
cipherText = cipherText.replace('\n', '')

# Global Variable
stdSumTable = []
globalvecs = []

# Calculate standard deviation(s) sum for frequency count(s)
# Takes a list of frequency count list(s), calculates the
# std-deviation of each list and then returns the sum of
# all the std-deviations
def standardDeviationSum(vectors):
	stdevSum = 0
	for i in range(len(vectors)):
		stdev = math.sqrt( sum(numpy.multiply(vectors[i], vectors[i]))/26 - numpy.power(sum(vectors[i])/26, 2))
		stdevSum += stdev
	return stdevSum

# Returns a list consisting of 'size' number of
# lists with frequency counts
def makeFreqVects(size):
	# Initialize a list of 'size' lists
	vectors = [([0] * 26) for i in range(size)]
	for i in range(len(cipherText)):
		vectors[i%size][ord(cipherText[i]) % ord('a')] += 1
	globalvecs.append(vectors)
	return vectors


def main():
	### MAIN PART ###
	#1. Loop through all possible key-lengths
	highestStDev = 0
	highestStDevIndex = 0
	for i in range(5,16): # <-- from 5 to 15
		stdSumTable.append(standardDeviationSum(makeFreqVects(i)))
		print "Sum of " + str(i) + " std. devs: " + str(stdSumTable[i-5]) + ","
		if stdSumTable[i-5] > highestStDev: #determine key length with highest StDev
			highestStDev = stdSumTable[i-5]
			highestStDevIndex = i

	keyList = []
	frequencies = []
	#for frequency vectors of the length with highest StDev
	for i in range(len(globalvecs[highestStDevIndex-5])):
		#Make a tuple with the letter index corresponding to the frequency
		frequencies.append([globalvecs[highestStDevIndex-5][i],range(0,26)])
		#Bubble sort letters, highest frequency first
		for j in range(len(globalvecs[highestStDevIndex-5][i])):
			for k in range(len(globalvecs[highestStDevIndex-5][i])-1-j):
				if frequencies[i][0][k] < frequencies[i][0][k+1]:
					a = frequencies[i][0][k]
					frequencies[i][0][k] = frequencies[i][0][k+1]
					frequencies[i][0][k+1] = a
					b = frequencies[i][1][k]
					frequencies[i][1][k] = frequencies[i][1][k+1]
					frequencies[i][1][k+1] = b
	for i in range(len(frequencies)):
		poss = []
		#Try for 3rd most common letters in English
		poss.append(chr(ord('a') + (frequencies[i][1][0]-(ord('e')-ord('a')))%26))
		poss.append(chr(ord('a') + (frequencies[i][1][0]-(ord('t')-ord('a')))%26))
		poss.append(chr(ord('a') + (frequencies[i][1][0]-(ord('a')-ord('a')))%26))
		poss.append(chr(ord('a') + (frequencies[i][1][0]-(ord('a')-ord('o')))%26))
		poss.append(chr(ord('a') + (frequencies[i][1][0]-(ord('a')-ord('i')))%26))
		keyList.append(poss)
	print "\n"
	print "Most possible letters: (ranging from most to 3rd most)"
	print "Key index: 0    1    2    3    4    5    6    7    8    9    10   11"
	print "1st:     " + str([i[0] for i in keyList])
	print "2nd:     " + str([i[1] for i in keyList])
	print "3rd:     " + str([i[2] for i in keyList])
	print "4th:     " + str([i[3] for i in keyList])
	print "5th:     " + str([i[4] for i in keyList])

	print "\n"
	#Decript text using key that assumes all highest
	# frequency letters were originally an 'e'
	text = ""
	for i in range(len(cipherText)):
		text += chr( ( (ord(cipherText[i]) - ord('a')) - (ord(keyList[i%len(keyList)][0]) - ord('a')))%26 + ord('a'))
	print "Original text:"
	print cipherText
	print "\n"
	print "Decrypted text:"
	print text
	

if __name__ == "__main__":
    main()
