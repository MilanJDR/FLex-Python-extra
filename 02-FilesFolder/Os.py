#import 
import os

# De huidige directory opvragen en opslaan in de variabele: werkmap
werkmap = os.getcwd()

# De letters cwd staan voor: current working directory (de huidige map!)

# Op het scherm printen
print("De huidige map is: " + werkmap)

# Een nieuwe map maken met os.mkdir()
os.mkdir("nieuwe map")
#zodat ik weet dat er een nieuwe map is gemaakt
print("er is een nieuwe map aangemaakt genaamd: nieuwe map")
