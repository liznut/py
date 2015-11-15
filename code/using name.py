if __name__ == '__main__':
	print 'This program is being run by itself'
	def printMax(a,b):
	if a>b :
		print a, 'is maxmium'
	else:
		print b, 'is maxmium'
printMax(3,4) # directly give literal values

x=5
y=7

printMax(x,y) #give variables as arguments
else:
	print 'I am being imported from another module'