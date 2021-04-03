
sinexizw = 1
while sinexizw:
	isitru = input("Gimme the HEX: ")
	asdecode = bytes.fromhex(isitru)
	print(str(asdecode)) #kati na kanw na fyneii to b''
	sinexizw = input('1 continue, 0 quit: ')
	if int(sinexizw) == 1:
		sinexizw = int(sinexizw)
		
	elif int(sinexizw) == 0:
		sinexizw = int(sinexizw)
	else:
		sinexizw = input('1 continue, 0 quit: ')
		if int(sinexizw) == 1:
			sinexizw = int(sinexizw)
		elif int(sinexizw) == 0:
			sinexizw = int(sinexizw)
		
		
	
	
	
	
