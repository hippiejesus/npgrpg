#-----------------------------------------------------------------------
#Imports****************************************************************
#-----------------------------------------------------------------------
import copy

import random

#-----------------------------------------------------------------------
#Globals****************************************************************
#-----------------------------------------------------------------------
BEINGLIST = []
ROOMLIST = []
GROUPLIST = []
ORGLIST = []
NATIONLIST = []

#-----------------------------------------------------------------------
#Classes****************************************************************
#-----------------------------------------------------------------------

#All 'living' things in the game are Beings, NPC or Player alike
class Being:
	#-------------------------------------------------------------------
	#Instance Variables
	#-------------------------------------------------------------------
    name = " "
    race = " "
    prof = " "

    currentRoom = [0,0]

    ST = 0
    IQ = 0
    LK = 0
    CON = 0
    DEX = 0
    CHA = 0
    
    currentHP = 0

    height = [0,0]
    weight = 0

    inventory = []
    weightPossible = 0
    weightCarried = 0

    level = 0
    type = "Commoner"
    
    affiliations = {'None':'Freelance'} #nation, organization, group
    
    isPlayer = False
    
    npc_attitudes = []
    npc_values = []
    npc_beliefs = []
    npc_behaviors = []
    
	#Initialize new Being
    def __init__(self,name,race):
        self.name = name
        self.race = race
        BEINGLIST.append(self)
	#Randomized stat selection process for PC
    def rollStats(self):
        STtemp = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
        IQtemp = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
        LKtemp = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
        CONtemp = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
        DEXtemp = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
        CHAtemp = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)

        print("Your stats roll in at:")
        print("")
        print("ST: ",STtemp)
        print("IQ: ",IQtemp)
        print("LK: ",LKtemp)
        print("CON: ",CONtemp)
        print("DEX: ",DEXtemp)
        print("CHA: ",CHAtemp)
        print("")
        print("Keep stats?")
        choice = raw_input("(y/n)")

        if choice == "y":
            self.ST = STtemp
            self.IQ = IQtemp
            self.LK = LKtemp
            self.CON = CONtemp
            self.DEX = DEXtemp
            self.CHA = CHAtemp
            self.currentHP = self.CON
            self.isPlayer = True
            print("Base attributes set!")
        elif choice == "n":
            self.rollStats()
	#Apply racial modifications to stats
    def applyRace(self):
        if self.race == "Dwarf":
            self.ST *= 2
            self.CON *= 2
            self.CHA *= (2/3)
        elif self.race == "Elf":
            self.IQ *= (3/2)
            self.DEX *= (3/2)
            self.CHA *= 2
            self.CON *= (2/3)
        elif self.race == "Fairy":
            self.ST *= (1/4)
            self.CON *= (1/4)
            self.LK *= (3/2)
            self.DEX *= (3/2)
            self.CHA *= 2
        elif self.race == "Hobbit":
            self.ST *= (1/2)
            self.CON *= 2
            self.DEX *= (3/2)
        elif self.race == "Leprechaun":
            self.ST *= (1/2)
            self.DEX *= (3/2)
            self.IQ *= (3/2)
            self.LK *= (3/2)
        elif self.race == "Dragon":
            self.ST *= 25
            self.IQ *= 5
            self.LK *= (1/2)
            self.CON *= 50
            self.DEX *= 3
            self.CHA *= -5
        elif self.race == "Goblin":
            self.ST *= (3/4)
            self.CON *= (3/4)
            self.DEX *= (3/2)
            self.CHA *= (-1/2)
        elif self.race == "Ogre":
            self.ST *= 2
            self.CON *= 2
            self.CHA *= (-3/2)
        elif self.race == "Orc":
            self.CHA *= -1
        elif self.race == "Troll":
            self.ST *= 3
            self.CON *= 3
            self.CHA *= -4

        self.weightPossible = self.ST * 100
        if self.isPlayer == True: print("racial modifiers applied.")
	#Generate height and weight, affected by race selection.
    def heightAndWeight(self):
        randomint = random.randint(3,18)
        baseHeight = 48
        baseWeight = 75
        while randomint >= 4:
            baseHeight += 2
            baseWeight += 15
            randomint -= 1

        if self.race == "Dwarf":
            baseHeight *= (2/3)
            baseWeight *= (7/8)
        elif self.race == "Elf":
            baseHeight *= (11/10)
        elif self.race == "Hobbit":
            baseHeight *= (1/2)
            baseWeight *= (1/2)
        elif self.race == "Fairy":
            baseHeight *= (1/10)
            baseWeight *= (1/200)
        elif self.race == "Leprechaun":
            baseHeight *= (1/3)
            baseWeight *= (1/4)
        elif self.race == "Dragon":
            baseHeight *= 10
            baseWeight *= 50
        elif self.race == "Goblin":
            baseHeight *= (3/4)
            baseWeight *= (3/4)
        elif self.race == "Ogre":
            baseHeight *= (3/2)
            baseWeight *= 2
        elif self.race == "Troll":
            baseHeight *= 2
            baseWeight *= 4

        self.height[0] = int(baseHeight / 12)
        self.height[1] = int(baseHeight % 12)
        self.weight = baseWeight
	#Fuction for displaying stats in a readable manner.
    def score(self):
        print("")
        print("Name: ",self.name)
        print("Kin: ",self.race)
        print("Type: ",self.type)
        print("Level: ",self.level)
        print("")
        print("Height: ",self.height)
        print("Weight: ",self.weight)
        print("Capacity: ",self.weightPossible)
        print("Carried: ",self.weightCarried)
        print("")
        print("ST: ",int(self.ST))
        print("IQ: ",int(self.IQ))
        print("LK: ",int(self.LK))
        print("CON: ",int(self.CON))
        print("DEX: ",int(self.DEX))
        print("CHA: ",int(self.CHA))
        print("")
        print("HP: ",int(self.currentHP))
        print("")
        print("Affiliations: ",self.affiliations)
	#Base generate function without the questioning, for creating NPCs.
    def generate(self):
        self.ST = random.randint(3,18) 
        self.IQ = random.randint(3,18)
        self.LK = random.randint(3,18)
        self.CON = random.randint(3,18)
        self.DEX = random.randint(3,18)
        self.CHA = random.randint(3,18)

        self.currentHP = self.CON

        self.applyRace()
        self.heightAndWeight()
	#Attack function, supplies options for attack and carries out calculations.
	def attack(self,target):
		attacks = ['swing','stab','trip','charge', 'shield bash', 'throw'
		           'disarm','grapple','parry','defense','ready', 'retreat']
		print(attacks)
		choice = raw_input("Choose a maneuver.")
		
		attacksEx = [  
		             ]
	
	#Move function, calls upon room generation if room does not exist.
    def move(self,direct):
        nextRoom = self.currentRoom
        ref = self.currentRoom[:]
        if self.isPlayer == True:
            print(getRoom(self.currentRoom).exits)
            print(direct in getRoom(self.currentRoom).exits)
        if((direct in getRoom(self.currentRoom).exits) == False):
            direction = " "
            if self.isPlayer == True: print("No exit.")
        else: direction = direct
        if(direction == "n"):
            nextRoom[1] += 1
        elif(direction == "s"):
            nextRoom[1] -= 1
        elif(direction == "e"):
            nextRoom[0] += 1
        elif(direction == "w"):
            nextRoom[0] -= 1
        if(direction != " "):
            if(getRoom(nextRoom) != False):
                self.currentRoom = nextRoom[:]
                if self.isPlayer == True: print("You enter the next room...")
            else:
                if self.isPlayer == True: print("Next: ",nextRoom," Current: ",ref)
                makeRoom(nextRoom[:],ref)
                self.currentRoom = nextRoom[:]
                if self.isPlayer == True: print("You enter the next room.")
    def takeTurn(self):
		#For now, all NPCs will wander aimlessly. 
		#Later, the action the NPC takes will depend on a number of factors.
        direction = ["n","s","e","w"]
        if('wander' in self.npc_behaviors):
			self.move(direction[random.randint(0,3)])

#Class handling random generation and parameter manipulation for rooms.
class Room:
	#-------------------------------------------------------------------
	#Instance Variables
	#-------------------------------------------------------------------
    name = " "
    coordinates = [0,0]
    inRoom = []

    exits = []
    description = " "
    features = {}
    items = []

    symbol = "|"
    environment = "nothing"
    hasCity = False
	
	#Initialize new Room.
    def __init__(self,name,coordinates,roomFrom):
        global ROOMLIST
        self.name = name
        self.coordinates = coordinates
        self.exits = []
        self.genExits()
        self.genEnvironment()
        addRoom(self)
        if(roomFrom != [0,0]):
		self.exitFrom(roomFrom[:])
	#**Append name to list of who is in the room. (currently unused)
    def enter(self,name):
        self.inRoom.append(name)
	#**Remove name from list of who is in the room. (currently unused)
    def exit(self,name):
        self.inRoom.pop(name)
	#Randomly generate exits.
    def genExits(self):
        rand = random.randint(1,15)
        if(rand == 1):
            self.exits.append("n")
        elif(rand == 2):
            self.exits.append("s")
        elif(rand == 3):
            self.exits.append("e")
        elif(rand == 4):
            self.exits.append("w")
        elif(rand == 5):
            self.exits.append("n")
            self.exits.append("s")
        elif(rand == 6):
            self.exits.append("e")
            self.exits.append("w")
        elif(rand == 7):
            self.exits.append("n")
            self.exits.append("w")
        elif(rand == 8):
            self.exits.append("s")
            self.exits.append("e")
        elif(rand == 9):
            self.exits.append("n")
            self.exits.append("e")
        elif(rand == 10):
            self.exits.append("s")
            self.exits.append("w")
        elif(rand == 11):
            self.exits.append("n")
            self.exits.append("e")
            self.exits.append("s")
        elif(rand == 12):
            self.exits.append("n")
            self.exits.append("w")
            self.exits.append("s")
        elif(rand == 13):
            self.exits.append("w")
            self.exits.append("n")
            self.exits.append("e")
        elif(rand == 14):
            self.exits.append("w")
            self.exits.append("s")
            self.exits.append("e")
        elif(rand == 15):
            self.exits.append("n")
            self.exits.append("s")
            self.exits.append("e")
            self.exits.append("w")
	#Determine the exit that will lead back to the previous room.
    def exitFrom(self,roomFrom):
		result = [(self.coordinates[0]-roomFrom[0]),(self.coordinates[1]-roomFrom[1])]
		print(self.coordinates)
		print(roomFrom)
		print(result)
		if(result[0] == -1): 
			self.exits.append("e")
		elif(result[0] == 1): 
			self.exits.append("w")
		elif(result[1] == -1): 
			self.exits.append("n")
		elif(result[1] == 1): 
			self.exits.append("s")
		#Remove duplicates in exit list	
		exitnew = list(dict.fromkeys(self.exits))
		self.exits = exitnew
    #*Randomly generate room features (in progress)
    def genFeatures(self):
		possibleFeatures = {"chair":"sit","button":"press","lever":"pull"}
    #Generate environment based off of adjacent rooms (shall be expanded upon)
    def genEnvironment(self):
		global ROOMLIST
		environmentList = []
		nearbyEnvironments = []
		
		northCoordinates = self.coordinates[:]
		northCoordinates[1] += 1
		
		southCoordinates = self.coordinates[:]
		southCoordinates[1] -= 1
		
		eastCoordinates = self.coordinates[:]
		eastCoordinates[0] += 1
		
		westCoordinates = self.coordinates[:]
		westCoordinates[0] -= 1
		
		if getRoom(northCoordinates) != False: nearbyEnvironments.append(getRoom(northCoordinates).environment)
		if getRoom(southCoordinates) != False: nearbyEnvironments.append(getRoom(southCoordinates).environment)
		if getRoom(eastCoordinates) != False: nearbyEnvironments.append(getRoom(eastCoordinates).environment)
		if getRoom(westCoordinates) != False: nearbyEnvironments.append(getRoom(westCoordinates).environment)
		
		numDesert = 0
		numAquatic = 0
		numForest = 0
		numGrassland = 0
		numTundra = 0
		
		for i in nearbyEnvironments:
				if i == "desert": numDesert += 1
				elif i == "aquatic": numAquatic += 1
				elif i == "forest": numForest += 1
				elif i == "grassland": numGrassland += 1
				elif i == "tundra": numTundra += 1
				
		survey = {"desert":numDesert,"aquatic":numAquatic,"forest":numForest,"grassland":numGrassland,"tundra":numTundra}
		inverted_survey = dict([[v,k] for k,v in survey.items()])
		
		if max(survey.values()) > 0:
			 
			top = inverted_survey.get(max(survey.values()))
			if top == "desert": 
			    if random.randint(0,10) > 3: self.environment = "desert"
			    else:
					if random.randint(0,10) > 4: self.environment = "tundra"
					else:
						if random.randint(0,10) > 5: self.environment = "grassland"
						else:
							if random.randint(0,10) > 6: self.environment = "forest"
							else:
								if random.randint(0,10) > 7: self.environment = "aquatic"
				
			if top == "tundra": 
			    if random.randint(0,10) > 3: self.environment = "tundra"
			    else:
					if random.randint(0,10) > 4: self.environment = "grassland"
					else:
						if random.randint(0,10) > 5: self.environment = "desert"
						else:
							if random.randint(0,10) > 6: self.environment = "forest"
							else:
								if random.randint(0,10) > 7: self.environment = "aquatic"
				
			if top == "grassland": 
			    if random.randint(0,10) > 3: self.environment = "grassland"
			    else:
					if random.randint(0,10) > 4: self.environment = "forest"
					else:
						if random.randint(0,10) > 5: self.environment = "aquatic"
						else:
							if random.randint(0,10) > 6: self.environment = "tundra"
							else:
								if random.randint(0,10) > 7: self.environment = "desert"
			if top == "forest": 
			    if random.randint(0,10) > 3: self.environment = "forest"
			    else:
					if random.randint(0,10) > 4: self.environment = "grassland"
					else:
						if random.randint(0,10) > 5: self.environment = "aquatic"
						else:
							if random.randint(0,10) > 6: self.environment = "desert"
							else:
								if random.randint(0,10) > 7: self.environment = "tundra"
								
			if top == "aquatic": 
			    if random.randint(0,10) > 3: self.environment = "aquatic"
			    else:
					if random.randint(0,10) > 4: self.environment = "grassland"
					else:
						if random.randint(0,10) > 5: self.environment = "forest"
						else:
							if random.randint(0,10) > 6: self.environment = "desert"
							else:
								if random.randint(0,10) > 7: self.environment = "tundra"
		else:
			surveylist = survey.keys()
			self.environment = surveylist[random.randint(0,4)]
		self.symbol = self.environment[:1]
	#**Check if name is in the room. (currently unused)
    def isInRoom(self,name):
        if(name in self.inRoom):
            return True
        else:
            return False

#Class handling random generation and parameter manipulation for groups.
#An organization is a group of groups
#A nation is a group of organizations (A group of groups of groups)
class Group:
	name = " "
	population = 0
	center = []
	members = []
	kind = 'group' #Can also be organization or nation
	ambitions = []
	
	def __init__(self,name):
		self.name = name
		self.center = []
		
	def addMember(self,member):
		self.members.append(member)
		if(member is Being):
			self.population += 1
			member.affiliations.append(self.kind,self.name)
			
		if(member is Group):
			self.population += member.population
			
		
		
	def dropMember(self,member):
		self.members.remove(member)
		if(member is Being):
			self.population -= 1
			member.affiliations.remove(self.name)
			
		if(member is Group):
			self.population -= member.population
		
#-----------------------------------------------------------------------
#Functions**************************************************************
#-----------------------------------------------------------------------

#Function to generate a room at the given coordinates, [x,y]
def makeRoom(coordinates,roomFrom):
    name = genName()
    room = copy.copy(Room(name,coordinates,roomFrom))
    

#Function to fetch a random letter, at index n, from a list containing the alphabet.
def getLetter(n):
    letters = ["a","b","c","d","e","f",
               "g","h","i","j","k","l",
               "m","n","o","p","q","r",
               "s","t","u","v","w","x",
               "y","z"]
    return letters[n]

#Function to fetch a reference to a particular Being from the BEINGLIST.
def getBeing(name):
    for i in BEINGLIST:
        if(i.name == name): return i

#Function to fetch a reference to a particular Room from the ROOMLIST.
def getRoom(coordinates):
    global ROOMLIST
    for i in ROOMLIST:
        if(i.coordinates == coordinates):
            return i
    return False

def getGroup(name):
	for group in GROUPLIST:
		if group.name == name: return group


#Function to add a Room to the ROOMLIST.
def addRoom(room):
    global ROOMLIST
    rooms = []
    for i in ROOMLIST:
        rooms.append(i)
    rooms.append(room)
    ROOMLIST = rooms

#Function to generate randomized names.
def genName():
    name = " "
    letterAmount = random.randint(2,9)
    while letterAmount >=1:
        letter = getLetter(random.randint(0,25))
        name += letter
        letterAmount -= 1

    return name

#Function to generate random Non-Player Characters
def genChar(group = "None", org = "None"):
	test = Being(genName(),"Human")
	test.generate()
	test.affiliations = test.affiliations.copy()
	test.npc_behaviors.append('wander')
	if(group != "None"):
		tgroup = getGroup(group)
		tgroup.addMember(test)
		if 'None' in test.affiliations:
			del test.affiliations['None']
		test.affiliations.update({tgroup.kind:tgroup.name})
		test.currentRoom = tgroup.center
	else: test.currentRoom = [0,1]

def genGroup(organization = "None"):
	test = Group(genName())
	GROUPLIST.append(test)
	roomint = random.randint(0,len(ROOMLIST)-1)
	pop = random.randint(1,15)
	test.center = ROOMLIST[roomint].coordinates[:]
		
	while pop >= 1:
		if organization != "None": orgname = organization
		else: orgname = "None"
		genChar(group = test.name, org = orgname)
		pop -= 1
		

#def genOrganization():
#	test = Group(genName())
#	GROUPLIST.append(test)
	
	


#Function to print map.
def printMap():
	xlist = []
	ylist = []
	for i in ROOMLIST:
		xlist.append(i.coordinates[0])
		ylist.append(i.coordinates[1])
	hx = max(xlist)
	lx = min(xlist)
	hy = max(ylist)
	ly = min(ylist)
	rows = hy + abs(ly) + 1
	columns = hx + abs(lx) + 1
	while rows > 0:
		tx = lx
		c = columns
		line = ""
		while c > 0:
			if getRoom([tx,hy]) != False:
				if [tx,hy] == [0,0]:
					line += "#"
				else: line += getRoom([tx,hy]).symbol
			else: line += "-"
			tx += 1
			c -= 1
		print(line)
		hy -= 1
		rows -= 1

#-----------------------------------------------------------------------
#START OF PROGRAM*******************************************************
#-----------------------------------------------------------------------
nameChoice = raw_input("Name: ")
raceChoice = raw_input("Race: ") 
player = Being(nameChoice,raceChoice)
player.rollStats()
player.applyRace()
player.heightAndWeight()
player.score()

print(ROOMLIST)
makeRoom([0,1],[0,0])
print(ROOMLIST)
player.currentRoom = [0,1]

#----------------------------------------------------------------------`	-
#MAIN LOOP**************************************************************
#-----------------------------------------------------------------------
quit = 0
while quit == 0:
    print("Biome: ",getRoom(player.currentRoom).environment)
    print("Exits: ",getRoom(player.currentRoom).exits)
    for i in BEINGLIST:
			if player.currentRoom == i.currentRoom:
				print(i.name+" is here.")
    
    choice = raw_input("...")

    if choice == "quit": quit = 1

	#Movement input.
    if choice == "n": player.move("n")
    if choice == "s": player.move("s")
    if choice == "e": player.move("e")
    if choice == "w": player.move("w")

    if choice == "map": printMap()

    if choice == "evaluate" or choice == "eval":
		cnum = 0
		cdic = {}
		for being in BEINGLIST:
			if being.currentRoom == player.currentRoom:
				cdic.update({cnum:being.name})
				cnum += 1
		print(cdic)
		dec = raw_input("Which being?")
		if(int(dec) in cdic.keys()):
			call = cdic[int(dec)]
			getBeing(call).score()

    if choice == "where":
        print(getRoom(player.currentRoom).coordinates)

    if choice == "score":
        player.score()

    #hidden commands.
    if choice == "#GROUPLIST" or choice == "#GL": print(GROUPLIST)
    if choice == "#ROOMLIST" or choice == "#RL": print(ROOMLIST)
    if choice == "#BEINGLIST" or choice == "#BL": print(BEINGLIST)
    if choice == "#CHARGEN" or choice == "#CG": genChar()
    if choice == "#GROUPGEN" or choice == "#GG": genGroup()
    if choice == "#EXIT" or choice == "#E":
		ex = raw_input("direction?")
		getRoom(player.currentRoom).exits.append(ex)
    if choice == "#ROOMGEN" or choice == "#RG":
		x = raw_input(player.currentRoom)
		y = raw_input(x)
		makeRoom([int(x),int(y)],player.currentRoom)
		addRoom(getRoom([int(x),int(y)]))
		print("Room added.")
		
    for b in BEINGLIST:
		if b.isPlayer == False:
			b.takeTurn()
