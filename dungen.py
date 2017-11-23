#npgrpg tile generator - [Early development]
#note: in game area description = 240 char max]
#----- 16 rows of 15 chars                    ]-for verticle screen!
#----- 16 rows of 48 chars for horizontal = 768 chars
#To test: what looks best between 240-768 max chars
import os
import random as rand

x=4
y=30
z=1
q=12

options = {"\033[33;40m/":x,"\033[1;32;40m,":y,"\033[1;30;40m0":z,"\033[32;40m*":q}
op = []
for i in options:
    for n in range(options[i]):
        op.append(i)

line1 = "\033[37;40m++++++++++++++++++++++++++"

def getLine():
    line = "\033[37;40m+"+"".join(rand.choice(op) for i in range(24))+"\033[37;40m+"
    return line
field = line1 + "\n" + "".join(((getLine() + "\n") for i in range(14))) + line1 


while True:
    inp = input("...")
    os.system('clear')
    field = line1 + "\n" + "".join(((getLine() + "\n") for i in range(14))) + line1 
    print(field)