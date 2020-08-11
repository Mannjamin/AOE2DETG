import random

print("Mann's Age of Empires Civilisation Generator")

# Collect Variables

# Number of Teams
numTeams = input("Enter number of teams: ")

# Yes or No Mutators
boolMutators = input("Enter Y or N for Mutators: ")

# Number of Mutators
if boolMutators == "Y" or "y": 
    numMutators = input("Enter number of mutators: ")

# Output chosen parameters
print("Number of Teams Selected: " + str(numTeams))

if boolMutators == "Y" or "y":
    print("Mutators? YES")
    print("Number of Mutators: " + str(numMutators))
else:
    print("Mutatos? NO")

civilisations = ["Aztecs", "Berbers", "Britons", "Bulgarians", "Celts", "Chinese", "Cumans", "Ethiopians", "Franks", "Goths", "Huns", "Incas", "Indians", "Italians", "Japanese", "Khmer", "Koreans", "Lithuanians", "Magyars", "Malay", "Malians", "Mayans", "Mongols", "Persians", "Portuguese", "Saracens", "Slavs", "Spanish", "Tatars", "Tuetons", "Turks", "Vietnamese", "Vikings"]

mutations =  ["No Infrantry", "Focus Infantry", "No Archers (incl Cavalry)", "Focus Archers", "No Cavalry (incl Camels and Elephants)", "Focus Cavalry", "No Siege Weapons (inc bombard cannons)", "Focus Siege Weapons", "No Blacksmith Upgrades", "No Trade (incl carts/caravans)", "No Monastery", "No Castles", "No Monks"]

for x in range(int(numTeams)):
    # Get Random Civilisation:
    chosenCiv = random.choice(civilisations)
    # Get Mutators
    if boolMutators == "Y" or "y":
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
            
    print("Team " + str(x) + " [Civilisation: " + str(chosenCiv) + "] [Mutators: " + str(chosenMut) +"]")

