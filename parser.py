#npgrpg Parser: [Ready for testing]
#-use: import parser
#----- actionList = parser.parse(commandLine)

import re

def parse(string):
    chain = []
    breakc = ""
    
    #Command/String to execute.
    hyph = re.search('(?<=-)\w+',string)
    
    #Modifies command/string.
    equals = re.search('(?<==)\w+',string)
    
    #Provides a break condition.
    slash = re.search('(?<=/)\w+',string)
    
    #Modifies break condition.
    at = re.search('(?<=@)\w+',string)
    
    #Action to be performed at break
    money = re.search('(?<=$)\w+',string)
    
    #Modifies break action
    ands = re.search('(?<=&)\w+',string)
    
    #Command to perform between each other action.
    #Place at beginning of string. put |n for none.
    line = re.search('(?<=|)\w+',string)
    
    #Movement Chain
    if hyph.group() == 'M':
        directions = ['n','s','e','w']
        moveChain = equals.group(0)
        oldi = ''
        for i in moveChain:
            if i not in directions:
                for n in range(int(i)-1):
                    chain.append(oldi)
            else: chain.append(i)
            oldi = i
    elif hyph.group() == 'W':
        for i in range(int(equals.group(0))):
            chain.append('wander')
    else: chain.append(hyph.group())
    if line.group(0) != 'n':
        newchain = []
        for i in chain:
            newchain.append(i)
            newchain.append(line.group())
            chain = newchain[:]
    
    #Join commandlist into returnable chain string.
    command = [chain,breakc]
    return command[:]

choice = input('string: ')
print(parse(choice)[0])