import io
#Bestand in read-only (r) mode openen
bestand2 = open("test.txt", "r")

# Alle tekst lezen met read() en opslaan in de variabele: inhoud
inhoud = bestand2.read()

# De inhoud op het scherm zetten:
print("De inhoud van het bestand is:")
print(inhoud)

print("==================================================")
klasgenoten = open("klasgenoten.txt", "r")

inhoud_2 = klasgenoten.read()

print(inhoud_2)
