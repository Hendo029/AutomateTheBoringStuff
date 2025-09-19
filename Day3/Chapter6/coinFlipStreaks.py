import random
tries = 10000
flipAmount = 100
streakAmount = 6
streakCounter = 0

def createList():
    for i in range(flipAmount):
        temp = random.randint(0,1)
        if temp == 0:
            coinList.append('T')
        else:
            coinList.append('H')

def checkList():
    global coinList
    global streakCounter
    for i in range(len(coinList)):
        if i == (len(coinList) - 6):
            return
        elif coinList[i:i+6] == ['H','H','H','H','H','H'] or coinList[i:i+6] == ['T','T','T','T','T','T']:
            streakCounter += 1
            return


'''
def checkList():
    temp = coinList[0]
    counter = 0
    for i, j in enumerate(coinList):
        if j == temp:
            counter += 1
        else:
            counter = 1
            temp = coinList[i]
        if counter == streakAmount:
            return True
    return False
'''

for i in range(tries):
    coinList = []
    createList()
    checkList()
    
    #if checkList():
    #    streakCounter += 1

print('The percentage of games with a same side streak of %s is: %.2f%%.' % (streakAmount, (streakCounter / tries * 100)))