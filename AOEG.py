import random

numTeams = '0'
numMutators = '0'

civilisations = ['Aztecs', 'Berbers', 'Britons', 'Bulgarians', 'Celts', 'Chinese', 'Cumans', 'Ethiopians', 'Franks', 'Goths', 'Huns', 'Incas', 'Indians', 'Italians', 'Japanese', 'Khmer',
                'Koreans', 'Lithuanians', 'Magyars', 'Malay', 'Malians', 'Mayans', 'Mongols', 'Persians', 'Portuguese', 'Saracens', 'Slavs', 'Spanish', 'Tatars', 'Tuetons', 'Turks', 'Vietnamese', 'Vikings']
mutations = ['No Infrantry', 'Focus Infantry', 'No Archers (incl Cavalry)', 'Focus Archers', 'No Cavalry (incl Camels and Elephants)', 'Focus Cavalry',
            'No Siege Weapons (inc bombard cannons)', 'Focus Siege Weapons', 'No Blacksmith Upgrades', 'No Trade (incl carts/caravans)', 'No Monastery', 'No Castles', 'No Monks']

chosenCivilisations = []

# List of List
chosenMutations = []

# List of List
newChosenMutations = []

# Get Number of Teams
def setNumTeams():
    global numTeams
    try:
        numTeams = input('Enter number of teams: ')
        try:
            numTeams = int(numTeams)
        except ValueError:
            print('Input is not a number, try again.')
            setNumTeams()
    except SyntaxError:
        print('No input found, try again.')
        setNumTeams()

# Get Number of Mutators wanted.
def setNumMutators():
    global numMutators
    try:
        numMutators = input('Enter number of mutators: ')
        try:
            numMutators = int(numMutators)
        except ValueError:
            print('Input is not a number, try again.')
            setNumMutators()
    except SyntaxError:
        print('No input found, try again.')
        setNumMutators()

# Print User Chosen Parametrs
def printParams():
    print('-------------------------------------------------------------------------')
    # Number of Teams:
    print('Number of Teams Selected: ' + str(numTeams))
    # Number of Mutators:
    print('Number of Mutators: ' + str(numMutators))

def getCivilisations():
    global numTeams, chosenCivilisations
    for x in range(int(numTeams)):
        # Get Random Civilisation:
        chosenCiv = random.choice(civilisations)
        chosenCivilisations.append(chosenCiv)

def getMutations():
    global chosenCivilisations, chosenMutations, mutations
    for x in range(len(chosenCivilisations)):
        teamMutations = []
        for y in range(int(numMutators)):
            randMute = random.choice(mutations)
            if randMute in teamMutations:
                while randMute in teamMutations:
                    randMute = random.choice(mutations)
                if randMute not in teamMutations:
                    break
            teamMutations.append(randMute)
        chosenMutations.append(teamMutations)
    viabilityCheck()

def viabilityCheck():
    for x in range(len(chosenCivilisations)):
        if str(chosenCivilisations[x]) == 'Goths':
            civIndex = x
            if 'No Infantry' in chosenMutations[civIndex]:
                mutIndex = chosenMutations[civIndex].index('No Infantry')
                replaceMutation(civIndex, mutIndex, 'No Infantry')
        if str(chosenCivilisations[x]) == 'Aztecs':
            civIndex = x
            if 'Focus Cavalry' in chosenMutations[civIndex]:
                mutIndex = chosenMutations[civIndex].index('Focus Cavalry')
                replaceMutation(civIndex, mutIndex, 'Focus Cavalry')
        if str(chosenCivilisations[x]) == 'Incas':
            civIndex = x
            if 'Focus Cavalry' in chosenMutations[civIndex]:
                mutIndex = chosenMutations[civIndex].index('Focus Cavalry')
                replaceMutation(civIndex, mutIndex, 'Focus Cavalry')
        if str(chosenCivilisations[x]) == 'Mayans':
            civIndex = x
            if 'Focus Cavalry' in chosenMutations[civIndex]:
                mutIndex = chosenMutations[civIndex].index('Focus Cavalry')
                replaceMutation(civIndex, mutIndex, 'Focus Cavalry')




def replaceMutation(civIndex, mutIndex, unwantedMutator):
    global chosenMutations
    randMute = unwantedMutator
    while randMute == unwantedMutator:
        randMute = random.choice(mutations)
        if randMute != unwantedMutator:
            break
    randMute = random.choice(mutations)
    chosenMutations[civIndex][mutIndex] = randMute

# Generate User Chosen Parameters
def getParams():
    print("-------------------------------------------------------------------------")
    for x in range(len(chosenCivilisations)):
        print('Team ' + str(x) + ', Civilisation: ' + str(chosenCivilisations[x]) + ', Mutators: ' + str(chosenMutations[x]))
    print("-------------------------------------------------------------------------")

# Execute Code
print("-------------------------------------------------------------------------")
print("Mann's Age of Empires Civilisation Generator")

setNumTeams()
setNumMutators()
printParams()
getCivilisations()
getMutations()
getParams()

