# 1. Find the encrypted text
cipherText = "qyfwigyninbywiolmyuvionchzilguncihmy\
wolcnsnbcmwiolmycmuvionmywolchachzilguncihchnbcmwi\
hnyrnqynbchezilyrugjfyuvionbiqnijlypyhnnbyohuonbil\
ctyxlyuxchaizchzilguncihiluvionbiqnijlypyhnnbyohuo\
nbilctyxgixczcwuncihizchzilguncihguhsyhwlsjncihgyn\
bixmyrcmnmigyuflyuxsnbiomuhxmsyulmifxchcncuffsqyff\
ziwomihmcgjfygynbixmniyhwlsjnchzilguncihziffiqchan\
bcmqyffomywbuluwnylcmncwpufoymcxyhnczschachzilgunc\
ihguechacnxczzcwofnnigixczschzilguncihohhinczcyxfu\
nylchnbcmwiolmyqyffchnlixowyjylmihufyhwlsjncihuhxq\
yffmnoxsnijcwmfceyvozzylipylzfiqyrjficnmuhxmwlimmm\
cnymwlcjnchacbijysioffyhdisnbcmwiolmyuvionchzilgun\
cihmywolcns"

def solveSubCipher(cipher, key):
	alpha = "abcdefghijklmnopqrstuvwxyz"
	output = ""

	for letter in cipherText:
		letter_idx = ord(letter) % ord('a')
		output += alpha[(letter_idx - key) % 26]
	return output

def findKeyFromAlphaShift(cipher):
	print "-----------------" # <-- helps reading output
	for i in range(26):
		print str(i) + " -- " + solveSubCipher(cipher, i)
	print "-----------------"

findKeyFromAlphaShift(cipherText)
# Key found to be 20!

# 2. Find the smallest postive substitution cipher shift value
# to return the original text 

plainText = "welcometothecourseaboutinformationsecurity\
thiscourseisaboutsecuringinformationinthiscontextwethin\
kforexampleabouthowtopreventtheunauthorizedreadingofinf\
ormationorabouthowtopreventtheunauthorizedmodificationo\
finformationmanyencryptionmethodsexistsomealreadythousa\
ndsyearsoldinitiallywellfocusonsimplemethodstoencryptin\
formationfollowingthiswellusecharacteristicvaluesidenti\
fyinginformationmakingitdifficulttomodifyinformationunn\
otifiedlaterinthiscoursewellintroducepersonalencryption\
andwellstudytopicslikebufferoverflowexploitsandscrosssi\
tescriptingihopeyoullenjoythiscourseaboutinformationsecurity"

def encrypt(cipher, key):
	alpha = "abcdefghijklmnopqrstuvwxyz"
	output = ""

	for letter in cipherText:
		letter_idx = ord(letter) % ord('a')
		output += alpha[(letter_idx + key) % 26]
	return output

def findSmallestPositiveShift():
	shift = 0
	while (encrypt(cipherText, shift) != plainText):
		shift += 1
	return shift

print "Smallest positive shift = " + str(findSmallestPositiveShift())