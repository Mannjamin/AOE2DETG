import random

numTeams = '0'
numMutators = '0'

civilisations = ["Aztecs", "Berbers", "Britons", "Bulgarians", "Celts", "Chinese", "Cumans", "Ethiopians", "Franks", "Goths", "Huns", "Incas", "Indians", "Italians", "Japanese", "Khmer",
                "Koreans", "Lithuanians", "Magyars", "Malay", "Malians", "Mayans", "Mongols", "Persians", "Portuguese", "Saracens", "Slavs", "Spanish", "Tatars", "Tuetons", "Turks", "Vietnamese", "Vikings"]
mutations = ["No Infrantry", "Focus Infantry", "No Archers (incl Cavalry)", "Focus Archers", "No Cavalry (incl Camels and Elephants)", "Focus Cavalry",
            "No Siege Weapons (inc bombard cannons)", "Focus Siege Weapons", "No Blacksmith Upgrades", "No Trade (incl carts/caravans)", "No Monastery", "No Castles", "No Monks"]

# Get Number of Teams
def setNumTeams():
    global numTeams
    try:
        numTeams = input("Enter number of teams: ")
        try:
            numTeams = int(numTeams)
        except ValueError:
            print("Input is not a number, try again.")
            setNumTeams()
    except SyntaxError:
        print("No input found, try again.")
        setNumTeams()

# Get Number of Mutators wanted.
def setNumMutators():
    global numMutators
    try:
        numMutators = input("Enter number of mutators: ")
        try:
            numMutators = int(numMutators)
        except ValueError:
            print("Input is not a number, try again.")
            setNumMutators()
    except SyntaxError:
        print("No input found, try again.")
        setNumMutators()

# Print User Chosen Parametrs
def printParams():
    print("-------------------------------------------------------------------------")
    # Number of Teams:
    print("Number of Teams Selected: " + str(numTeams))
    # Number of Mutators:
    print("Number of Mutators: " + str(numMutators))

# Generate User Chosen Parameters
def getParams():
    print("-------------------------------------------------------------------------")
    # Output chosen parameters
    for x in range(int(numTeams)):
        # Get Random Civilisation:
        chosenCiv = random.choice(civilisations)
        # Get Mutators
        if int(numMutators) > 0:
            chosenMut = []
            for y in range(int(numMutators)):
                # Second Check In
                while chosenCiv == "Goths":
                    randMute = random.choice(mutations)
                    while randMute == "No Infantry":
                        randMute = random.choice(mutations)
                        if randMute != "No Infantry":
                            break
                    chosenMut.append(randMute)
                    break    
                while chosenCiv == "Incas" or "Aztecs" or "Mayans":
                    randMute = random.choice(mutations)
                    while randMute == "Focus Cavalry":
                        randMute = random.choice(mutations)
                        if randMute != "Focus Cavalry":
                            break
                    chosenMut.append(randMute)
                    break 
        if int(numMutators) > 0:
            print("Team " + str(x+1) + " [Civilisation: " + str(chosenCiv) + "] [Mutators: " + str(chosenMut) +"]")
        else:
            print("Team " + str(x+1) + " [Civilisation: " + str(chosenCiv) +"]")
    print("-------------------------------------------------------------------------")

# Execute Code
print("-------------------------------------------------------------------------")
print("Mann's Age of Empires Civilisation Generator")

setNumTeams()
setNumMutators()
printParams()
getParams()

