giapame = 1
sumstring = ''
utf8list = []

while giapame:
	choose = input('Αριθμό ή λίστα; 1 : Αριθμός, 2 = Λίστα')
	choose = int(choose)
	
	if choose == 1:
		dwse = input('Δώσε αριθμό ')
		dwse = int(dwse)
		dekaej = hex(dwse)
		mystring = dekaej [2]+ dekaej [3]	
		sumstring = sumstring + mystring
		print (sumstring)
		synexeia = input ('Continue? 1 : YES 0 : NO')
		synexeia = int(synexeia)
	
		if synexeia == 1:
			pass
		elif synexeia ==0:
			print (sumstring)
		
			convert = input("Wish to convert to ASCII? 1: Yes 0: No ")
			convert = int(convert)
			while True:
				if convert == 1:
					asdecode = bytes.fromhex(sumstring)
					print(str(asdecode))
					quit()
				elif convert == 0:
					quit()
				else:
					convert = input("Wish to convert to ASCII? 1: Yes 2: No ")
					convert = int(convert)
			
		
		else:
			synexeia = input ('Continue? 1 : YES 0 : NO')
			synexeia = int(synexeia) #ValueError: invalid literal for int() with base 10: 'd' EXCEPT TO ERROR 
			
	elif choose == 2:
		choose = input('Αριθμό ή λίστα; 1 : Αριθμός, 2 = Λίστα')
		# na to grafei se csv kai meta na pairnei ton kathe arithmo 
		#meta while sth lista na kanei to convert kai na to apothikevei sto sumstring opws panw 
		
		
	
		
	
		
	
