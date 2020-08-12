import random
numTeams = '0'
numMutators = '0'
civilisations = ['Aztecs', 'Berbers', 'Britons', 'Bulgarians', 'Celts', 'Chinese', 'Cumans', 'Ethiopians', 'Franks', 'Goths', 'Huns', 'Incas', 'Indians', 'Italians', 'Japanese', 'Khmer',
                 'Koreans', 'Lithuanians', 'Magyars', 'Malay', 'Malians', 'Mayans', 'Mongols', 'Persians', 'Portuguese', 'Saracens', 'Slavs', 'Spanish', 'Tatars', 'Tuetons', 'Turks', 'Vietnamese', 'Vikings']
mutations = ['No Infrantry', 'Focus Infantry', 'No Archers (incl Cavalry)', 'Focus Archers', 'No Cavalry (incl Camels and Elephants)', 'Focus Cavalry',
             'No Siege Weapons (inc bombard cannons)', 'Focus Siege Weapons', 'No Blacksmith Upgrades', 'No Trade (incl carts/caravans)', 'No Monastery', 'No Castles', 'No Monks']
chosenCivilisations = []
chosenMutations = []
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

# Print User Inputs
def getInputs():
    print('-------------------------------------------------------------------------')
    # Number of Teams:
    print('Number of Teams Selected: ' + str(numTeams))
    # Number of Mutators:
    print('Number of Mutators: ' + str(numMutators))

# Collect list of Random Civilisations
def getCivilisations():
    global numTeams, chosenCivilisations
    for x in range(int(numTeams)):  # pylint: disable=unused-variable
        # Get Random Civilisation:
        chosenCiv = random.choice(civilisations)
        chosenCivilisations.append(chosenCiv)

# Collect list of Random Mutations per Civilisation
def getMutations():
    global chosenCivilisations, chosenMutations, mutations
    for x in range(len(chosenCivilisations)):  # pylint: disable=unused-variable
        teamMutations = []
        for y in range(int(numMutators)):  # pylint: disable=unused-variable
            randMute = random.choice(mutations)
            if randMute in teamMutations:
                while randMute in teamMutations:
                    randMute = random.choice(mutations)
                if randMute not in teamMutations:
                    break
            teamMutations.append(randMute)
        chosenMutations.append(teamMutations)
    viabilityCheck()

# Check if certain factions are viable
def viabilityCheck():
    for x in range(len(chosenCivilisations)):
        # Check Goths have Infantry Units.
        civIndex = x
        if str(chosenCivilisations[x]) == 'Goths':
            civIndex = x
            if 'No Infantry' in chosenMutations[civIndex]:
                mutIndex = chosenMutations[civIndex].index('No Infantry')
                replaceMutation(civIndex, mutIndex, 'No Infantry')
                viabilityCheck()
        # Check Aztecs don't have Focus Cavalry
        if str(chosenCivilisations[x]) == 'Aztecs':
            civIndex = x
            if 'Focus Cavalry' in chosenMutations[civIndex]:
                mutIndex = chosenMutations[civIndex].index('Focus Cavalry')
                replaceMutation(civIndex, mutIndex, 'Focus Cavalry')
                viabilityCheck()
        # Check Incas don't have Focus Cavalry
        if str(chosenCivilisations[x]) == 'Incas':
            civIndex = x
            if 'Focus Cavalry' in chosenMutations[civIndex]:
                mutIndex = chosenMutations[civIndex].index('Focus Cavalry')
                replaceMutation(civIndex, mutIndex, 'Focus Cavalry')
                viabilityCheck()
        # Check Mayans don't have Focus Cavalry
        if str(chosenCivilisations[x]) == 'Mayans':
            civIndex = x
            if 'Focus Cavalry' in chosenMutations[civIndex]:
                mutIndex = chosenMutations[civIndex].index('Focus Cavalry')
                replaceMutation(civIndex, mutIndex, 'Focus Cavalry')
                viabilityCheck()
        # Check Civilisation doesn't have both forms of Infantry Mutation
        if "No Infantry" in chosenMutations[civIndex] and "Focus Infantry" in chosenMutations[civIndex]:
            civIndex = x
            mutIndex = chosenMutations[civIndex].index('Focus Infantry')
            replaceMutation(civIndex, mutIndex, 'Focus Infantry')
            viabilityCheck()
        if "Focus Infantry" in chosenMutations[civIndex] and "No Infantry" in chosenMutations[civIndex]:
            civIndex = x
            mutIndex = chosenMutations[civIndex].index('No Infantry')
            replaceMutation(civIndex, mutIndex, 'No Infantry')
            viabilityCheck()
        # Check Civilisation doesn't have both forms of Cavalry Mutation
        if "No Cavalry (incl Camels and Elephants)" in chosenMutations[civIndex] and "Focus Infantry" in chosenMutations[civIndex]:
            civIndex = x
            mutIndex = chosenMutations[civIndex].index(
                'No Cavalry (incl Camels and Elephants)')
            replaceMutation(civIndex, mutIndex,
                            'No Cavalry (incl Camels and Elephants)')
            viabilityCheck()
        if "Focus Cavalry" in chosenMutations[civIndex] and "No Cavalry (incl Camels and Elephants)" in chosenMutations[civIndex]:
            civIndex = x
            mutIndex = chosenMutations[civIndex].index(
                'No Cavalry (incl Camels and Elephants)')
            replaceMutation(civIndex, mutIndex,
                            'No Cavalry (incl Camels and Elephants)')
            viabilityCheck()
        # Check Civilisation doesn't have both forms of Archery Mutation
        if "No Archers (incl Cavalry)" in chosenMutations[civIndex] and "Focus Archers" in chosenMutations[civIndex]:
            civIndex = x
            mutIndex = chosenMutations[civIndex].index(
                'No Archers (incl Cavalry)')
            replaceMutation(civIndex, mutIndex, 'No Archers (incl Cavalry)')
            viabilityCheck()
        if "Focus Archers" in chosenMutations[civIndex] and "No Archers (incl Cavalry)" in chosenMutations[civIndex]:
            civIndex = x
            mutIndex = chosenMutations[civIndex].index('Focus Archers')
            replaceMutation(civIndex, mutIndex, 'Focus Archers')
            viabilityCheck()
        # Check Civilisation doesn't have both forms of Siege Mutation
        if "No Siege Weapons (inc bombard cannons)" in chosenMutations[civIndex] and "Focus Siege Weapons" in chosenMutations[civIndex]:
            civIndex = x
            mutIndex = chosenMutations[civIndex].index(
                'No Siege Weapons (inc bombard cannons)')
            replaceMutation(civIndex, mutIndex,
                            'No Siege Weapons (inc bombard cannons)')
            viabilityCheck()
        if "Focus Siege Weapons" in chosenMutations[civIndex] and "No Siege Weapons (inc bombard cannons)" in chosenMutations[civIndex]:
            civIndex = x
            mutIndex = chosenMutations[civIndex].index('Focus Siege Weapons')
            replaceMutation(civIndex, mutIndex, 'Focus Siege Weapons')
            viabilityCheck()

# Replace Unwanted Mutations
def replaceMutation(civIndex, mutIndex, unwantedMutator):
    global chosenMutations
    randMute = unwantedMutator
    while randMute == unwantedMutator:
        randMute = random.choice(mutations)
        if randMute != unwantedMutator:
            break
    randMute = random.choice(mutations)
    chosenMutations[civIndex][mutIndex] = randMute

# Print out Results
def getResults():
    print("-------------------------------------------------------------------------")
    for x in range(len(chosenCivilisations)):
        print('Team ' + str(x) + ', Civilisation: ' +
              str(chosenCivilisations[x]) + ', Mutators: ' + str(chosenMutations[x]))
    print("-------------------------------------------------------------------------")

# Execute Code
print("-------------------------------------------------------------------------")
print("Mann's Age of Empires Civilisation Generator")

setNumTeams()
setNumMutators()
getInputs()
getCivilisations()
getMutations()
getResults()