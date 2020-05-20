def read1():
    encrypt = ''
    with open(filename1, 'r', encoding='utf-8') as f:
        encrypt = encrypt.join(f)
    return encrypt

def encryption(encrypt, key):
    encrypted = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in encrypt.lower():
        if letter in alphabet:
            position = alphabet.find(letter)
            newPosition = (position + key) % len(alphabet)
            encrypted += alphabet[newPosition] 
        else:
            encrypted += letter
    return encrypted

def write1(encrypted):
	with open(filename2, 'w', encoding='utf-8') as f:
		f.write(encrypted)

def read2():
	encrypt = ''
	with open(filename2, 'r', encoding='utf-8') as f:
		encrypt = encrypt.join(f)
	return encrypt

def decryption(encrypt, key):
	encrypteed = ""
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	for letter in encrypt.lower():
		if letter in alphabet:
			position = alphabet.index(letter)
			newPosition = (position - key) % len(alphabet)
			encrypteed += alphabet[newPosition]
		else:
			encrypteed += letter
	return encrypteed

def write2(encrypteed):
    with open(filename3, 'w', encoding='utf8') as f:
        f.write(encrypteed)


filename1 = input('What file to encrypt?: ')
filename2 = input('Where to arrange encrypted text?: ')
filename3 = input('Where to arrange decrypted text?: ')
key = int(input('Key(1-25): ')) 

encrypt =  read1()
encrypt = encryption(encrypt, key)
write1(encrypt)

encrypt = read2()
encrypt = decryption(encrypt, key)
write2(encrypt)
print("Done")
