from os import system, name

class Converter():
	def __init__(self):
		self.clear()
		self.binary_total = ''
		self.decimal_to_binary_answer=''
		self.binary_to_decimal_answer=0
		self.use_existing = False
		self.choice = 'y'
		run = True

		self.count = 0

		while run == True:
			conversion_type=input("\n[1] Decimal to Binary\n[2] Binary to Decimal\n[3] Hex Conversions\n\nChoice: ")
			if conversion_type == '1':
				self.clear()
				self.decimal_to_binary()
			elif conversion_type == '2':
				self.clear()
				self.binary_to_decimal()
			elif conversion_type == '3':
				self.clear()
				self.hex_to_binary()
			
			x = input("\n\nRun another conversion?   y/n: ")
			if x != 'y':
				run = False
			self.clear()
			


	def clear(self):
		if name == 'nt':
			_=system('cls')
		else:
			_=system('clear')


	def decimal_to_binary(self):
		key = {'0':128,'1':64,'2':32,'3':16,'4':8,'5':4,'6':2,'7':1}
		self.choice = 'y'
		while self.choice == 'y':
			octet = input("\nEnter an IP Octet in Decimal form:   ")
			total = int(octet)
			binary = ''
			self.count = 0
			while len(binary) != 8:
				x = key[str(self.count)]
				if total - x >= 0:
					binary += '1'
					total -= x
				else:
					binary += '0'
				self.count += 1
			self.decimal_to_binary_answer=binary
			print("\nAnswer:  ",binary)
			self.choice = input("\nRun Decimal conversion again?   y/n:  ")
			self.clear()


	def binary_to_decimal(self):
		self.choice = 'y'
		while self.choice == 'y':
			if self.use_existing == True:
				octet = list(self.binary_total)
			else:	
				octet = list(input("\nInput a Binary number:   "))
			total = 0
			for i in range(len(octet)):
				num = octet.pop()
				if num == '1':
					total = total + pow(2, i)
			self.binary_to_decimal_answer=total
			print("\nAnswer:  ",total)
			self.choice = input("\nRun Binary conversion again?   y/n:  ")
			self.use_existing = False
			self.clear()


	def hex_to_binary(self):
		hex_key = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
		nibble_key = {'0':8,'1':4,'2':2,'3':1}
		binary_set=[]
		self.choice = 'y'
		while self.choice == 'y':
			hex = input("\nEnter a hex value:   ")
			for i in hex:
				self.count = 0
				binary = ''
				total = hex_key[i]
				while len(binary) != 4:
					x = nibble_key[str(self.count)]
					if total - x >= 0:
						binary += '1'
						total -= x
					else:
						binary += '0'
					self.count += 1
				self.binary_total += binary
				binary_set.append(binary)
			print("\n\nNibbles:  ",binary_set)
			print("Answer:  ",self.binary_total)
			self.choice = input("\n\nRun HEX conversion again?   y/n:  ")

		to_decimal = input("\nConvert Binary output to Decimal?   y/n:  ")

		if to_decimal == 'y':
			self.use_existing = True
			self.binary_to_decimal()
		self.clear()


Converter()