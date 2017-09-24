import numpy as np
import matplotlib.pyplot as pplot

def solve_ceasar(cipherText, key):
	alpha = "abcdefghijklmnopqrstuvwxyz"
	output = ""

	for letter in cipherText:
		letter_idx = ord(letter) % ord('a')
		# Apparently raw_input() treats everything as a 
		# string by default, hence the type cast below
		output += alpha[(letter_idx - int(key)) % 26]

	return output

def findKeyFromAlphaShift(cipherText):
	print "-----------------"
	for i in range(26):
		print str(i) + " -- " + solve_ceasar(cipherText, i)
	print "-----------------"

def solve_ceasar_capital(cipherText, key):
	alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	output = ""

	for letter in cipherText:
		letter_idx = ord(letter) % ord('A')
		# Apparently raw_input() treats everything as a 
		# string by default, hence the type cast below
		output += alpha[(letter_idx - int(key)) % 26]

	return output

def exercise11_hist():
	text = "GBSXUCGSZQGKGSQPKQKGLSKASPCGBGBKGUKGCEUKUZKGGBSQEICACGKGCEUERWKLKUPKQQGCIICUAEUVSHQKGCEUPCGBCGQOEVSHUNSUGKUZCGQSNLSHEHIEEDCUOGEPKHZGBSNKCUGSUKUASERLSKASCUGBSLKACRCACUZSSZEUSBEXHKRGSHWKLKUSQSKCHQTXKZHEUQBKZAENNSUASZFENFCUOCUEKBXGBSWKLKUSQSKNFKQQKZEHGEGBSXUCGSZQGKGSQKUZBCQAEIISKOXSZSICVSHSZGEGBSQSAHSGKHMERQGKGSKREHNKIHSLIMGEKHSASUGKNSHCAKUNSQQKOSPBCISGBCQHSLIMQGKGSZGBKGCGQSSNSZXQSISQQGEAEUGCUXSGBSSJCQGCUOZCLIENKGCAUSOEGCKGCEUQCGAEUGKCUSZUEGBHSKGEHBCUGERPKHEHKHNSZKGGKAD"
	alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	freq = []

	for i in range(len(text)):
		freq.append(ord(text[i]) % ord('A'))

	pplot.hist(freq, 26)
	pplot.xticks(np.arange(26), alpha)
	pplot.show()

exercise11_hist()






