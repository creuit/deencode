def rot13(s):
	result = ""
	
	#Loop over characters
	for v in s:
		#Convert to number with ord.
		c = ord(v)
		
		# Shift number back or forward.
		if c  >= ord('a') and c <= ord('z'):
			if c > ord('m'):
				c -= 13
			else:
				c += 13
		elif c >= ord('A') and c <= ord('Z'):
			if c > ord('M'):
				c -= 13
			else:
				c += 13
				
		# Append to result.
		result += chr(c)

	# Return transformation.
	return result



def main():
	#Choose encode or decode
	ed = input('Press 1 = encode, 2 = decode')
	ed = int(ed)
	while ed > 0:
		# Encode: PERITTO AS TO AFISV OMVS
		if ed == 1:
			word = input('Encode: ')
			print(rot13(rot13(word)))
			ed = input('Press 1 = Encode, 2 = Decode')
			ed = int(ed)
		# Decode:	
		elif ed == 2:
			word = input('Decode: ')
			print(rot13(word))
			ed = input('Press 1 = Encode, 2 = Decode') # vgazei error otan den einai int FIXIT
			ed = int(ed)
		else:
			quit()
	else:
		quit()
	
main()

	
			
	
