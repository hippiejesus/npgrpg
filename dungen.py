#npgrpg tile generator - [Early development]
#note: in game area description = 240 char max]
#----- 16 rows of 15 chars                    ]-for verticle screen!
#----- 16 rows of 48 chars for horizontal = 768 chars
#To test: what looks best between 240-768 max chars
import random as rand
def col(c):
	return "\033[38;5;"+str(c)+"m"  
	
def genF():
	x=4
	y=30
	z=1
	q=12

	options = {(col(226)+"/"):x,(col(10)+","):y,(col(251)+"0"):z,(col(155)+"*"):q}
	op = []
	for i in options:
		for n in range(options[i]):
			op.append(i)
	line1 = "\033[37;40m++++++++++++++++++++++++++"

	def getLine():
		line = "\033[37;40m+"+"".join(rand.choice(op) for i in range(24))+"\033[37;40m+"
		return line



	field = line1 + "\n" + "".join(((getLine() + "\n") for i in range(14))) + line1 
	return(field)

def genT():
	x=30
	y=5
	z=15
	q=2

	options = {(col(231)+"~"):x,(col(14)+","):y,(col(195)+"-"):z,(col(117)+"*"):q}
	op = []
	for i in options:
		for n in range(options[i]):
			op.append(i)
	line1 = "\033[37;40m++++++++++++++++++++++++++"

	def getLine():
		line = "\033[37;40m+"+"".join(rand.choice(op) for i in range(24))+"\033[37;40m+"
		return line



	field = line1 + "\n" + "".join(((getLine() + "\n") for i in range(14))) + line1 
	return(field)

def genD():
	x=30
	y=5
	z=15
	q=2

	options = {(col(227)+"~"):x,(col(178)+"^"):y,(col(229)+"-"):z,(col(40)+"*"):q}
	op = []
	for i in options:
		for n in range(options[i]):
			op.append(i)
	line1 = "\033[37;40m++++++++++++++++++++++++++"

	def getLine():
		line = "\033[37;40m+"+"".join(rand.choice(op) for i in range(24))+"\033[37;40m+"
		return line



	field = line1 + "\n" + "".join(((getLine() + "\n") for i in range(14))) + line1 
	return(field)

def genG():
	x=30
	y=5
	z=15
	q=2

	options = {(col(10)+","):x,(col(46)+"."):y,(col(156)+"'"):z,(col(191)+","):q}
	op = []
	for i in options:
		for n in range(options[i]):
			op.append(i)
	line1 = "\033[37;40m++++++++++++++++++++++++++"

	def getLine():
		line = "\033[37;40m+"+"".join(rand.choice(op) for i in range(24))+"\033[37;40m+"
		return line



	field = line1 + "\n" + "".join(((getLine() + "\n") for i in range(14))) + line1 
	return(field)

def genA():
	x=1
	y=1
	z=1
	q=1

	options = {(col(26)+"~"):x,(col(19)+"~"):y,(col(105)+"~"):z,(col(51)+"~"):q}
	op = []
	for i in options:
		for n in range(options[i]):
			op.append(i)
	line1 = "\033[37;40m++++++++++++++++++++++++++"

	def getLine():
		line = "\033[37;40m+"+"".join(rand.choice(op) for i in range(24))+"\033[37;40m+"
		return line



	field = line1 + "\n" + "".join(((getLine() + "\n") for i in range(14))) + line1 
	return(field)

def testF():
	print(genF())
	
def testT():
	print(genT())

def testD():
	print(genD())

def testG():
	print(genG())
	
def testA():
	print(genA())
