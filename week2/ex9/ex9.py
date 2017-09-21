# Globals and "hard-coded" values
# key = "2017"
key = [50, 48, 49, 55]

S = [0] * 256
K = [0] * 256

i = 0 # <-- we will reuse these later and
j = 0 # need to keep track of them across the small program

# index for keystreamByte, also globally used
t = 0

# Initialize lookup table using key
# of size N, Reference: Stamp's book page 56
def initRC4(key, N):
	global S, K, i, j
	for i in range(256):
		S[i] = i
		K[i] = key[i % N]

	j = 0
	for i in range(256):
		j = (j + S[i] + K[i]) % 256
		S[i], S[j] = S[j], S[i] 
	i = j = 0

# We are only working with globals here
# Reference: Stamp's book page 56
def genKeyStreamByte():
	global i, j, S, t
	i = (i + 1) % 256
	j = (j + S[i]) % 256
	S[i], S[j] = S[j], S[i]
	t = (S[i] + S[j]) % 256
	return S[t]

# ~~~~~ Work starts here: ~~~~~

# 1. Initialize the lookup-table using key
initRC4(key, 4)

# 2. Ignore the first 256 keyStreamByte calls
for i in range(256):
	keyStreamByte = genKeyStreamByte()

# 3. Load file 
cipherText = open("rc4.enc", 'r').read()

# 4. Perform Decryption
plainText = ""
for char in cipherText:
	keyStreamByte = genKeyStreamByte()
	plainText += chr(ord(char) ^ keyStreamByte)

# 5. Display output
print plainText

# Achieved output:

# But I don't want to go among mad people,' said Alice. 'Oh, you can't help
# that,' said the cat. 'We're all mad here.'  

# This quote is from `Alice in Wonderland' by Lewis Carroll

