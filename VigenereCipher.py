import argparse

alph = list(map(chr, range(97, 123)))

def encrypt(message, key):
	message = message.lower()
	key = key.lower()
	cipherText = ''
	nonCount = 0
	for i in range(len(message)):
		if message[i] not in alph:
			nonCount += 1
			cipherText += message[i]
		else:
			cipherText += alph[(alph.index(key[(i - nonCount) % len(key)]) + alph.index(message[i]) ) % 26]
	return cipherText

def decrypt(cipherText, key):
	cipherText = cipherText.lower()
	key = key.lower()
	message = ''
	nonCount = 0
	for i in range(len(cipherText)):
		if cipherText[i] not in alph:
			nonCount += 1
			message += cipherText[i]
		else:
			message += alph[(alph.index(cipherText[i]) - alph.index(key[(i - nonCount) % len(key)])) % 26]
	return message
			
def main():
	
	if args.encrypt_flag == None and args.message == None and args.key == None:
		sel = input('Encrypt(1) or decrypt(2):')
		if sel == '1':
			message = input('Enter text to be encrypted:')
			key = input('Enter key:')
			print('Encrypted message:\n' +  encrypt(message, key))
		elif sel == '2':
			message = input('Enter text to be decrypted:')
			key = input('Enter key:')
			print('Decrypted message:\n' +  decrypt(message, key))

	elif args.encrypt_flag == True and args.message != None and args.key != None:
		message = args.message
		key = args.key
		print('Encrypted message:\n' +  encrypt(message, key))

	elif args.encrypt_flag == False and args.message != None and args.key != None:
		message = args.message
		key = args.key
		print('Decrypted message:\n' +  encrypt(message, key))

	else:
		parser.print_help()
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group()
	group.add_argument('-d', action = 'store_false', dest = 'encrypt_flag', default = None, help = 'decrypt message')
	group.add_argument('-e', action='store_true', dest = 'encrypt_flag', help = 'encrypt message')
	parser.add_argument('-m', '--message', help = 'message to be encrypted or decrypted')
	parser.add_argument('-k', '--key', help = 'key used for encryption or decryption')
	args = parser.parse_args()
	main()
			
			
			
			
