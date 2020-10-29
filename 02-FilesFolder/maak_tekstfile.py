# import
import io

 
bestand = open("test.txt", "w")


bestand.write("Test 123!");  


bestand.close()

# zodat ik weet dat ik er in heb geschreven 
print("je hebt in het bestand geschreven")

bestand2 = open("bestand2.txt", "r")

bestand2.write("Lekker alles overschrijven")

# zodat ik weet dat ik read only mode heb gedaan
print("readonly mode + geschreven")
