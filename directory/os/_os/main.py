import os

"""
🐍 Uitgebreide Uitleg van gebruikte functies uit de os-module:

- os.getcwd():
  Geeft de huidige werkdirectory (map) terug waarin Python werkt.

- os.chdir(pad):
  Verandert de huidige werkdirectory naar het opgegeven pad. 
  Het pad moet bestaan, anders krijg je een FileNotFoundError.

- os.listdir(pad='.'):
  Geeft een lijst terug met alle bestanden en mappen in de opgegeven directory.
  Als er geen pad opgegeven wordt, is dit standaard de huidige directory.

- os.path.split(pad):
  Splitst een volledig bestandspad in twee delen:
  1. de map (pad)
  2. de bestandsnaam (bestand)

- os.path.isfile(pad):
  Geeft True terug als het opgegeven pad naar een bestaand bestand leidt, anders False.

- os.path.isdir(pad):
  Geeft True terug als het opgegeven pad naar een bestaande map leidt, anders False.

- os.path.join(pad1, pad2, ...):
  Combineert meerdere paden of bestandsnamen tot één compleet pad.
  Dit is platform-onafhankelijk (werkt dus op Windows, macOS en Linux).

- os.makedirs(pad, exist_ok=True):
  Maakt één of meerdere nieuwe directories aan. De parameter 'exist_ok=True' zorgt ervoor dat er géén foutmelding komt als de map al bestaat.

- os.rename(bron, bestemming):
  Hiermee hernoem of verplaats je een bestand of map.

🎯 Doelstelling van dit script:
- Demonstreren van het navigeren door directories.
- Inhoud van directories ophalen en weergeven.
- Bestandspaden opsplitsen.
- Filteren van bestanden op bestandsextensie (.txt).
- Overzicht geven van bestanden en mappen in de werkdirectory.
- Maken van een nieuwe map als deze nog niet bestaat.
- Bestand hernoemen en verplaatsen naar een andere map.

Dit script dient als basis voor automatiseringstaken zoals bestandsorganisatie, backups en algemene systeemcontroles.
"""

# Toon de werkdirectory waar het script momenteel draait.
print(f"Werk directory: {os.getcwd()}")

# Verander werkdirectory naar opgegeven locatie.
os.chdir(r"c:/Users/stout/Documents/Github/snippets/directory/os/_os/")
print(f"Veranderd huidige werkdirectory naar opgegeven locatie.")

# Controleer nieuwe werkdirectory door opnieuw te printen.
print(f"Werk directory opnieuw met wijziging: {os.getcwd()}\n")

# Print inhoud van de huidige werkdirectory (bestanden en mappen).
print(f"Inhoud van de huidige werk directory: {os.listdir()}\n")

# Splits een opgegeven bestandspad in twee delen (pad en bestand).
pad, bestand = os.path.split(
    r"c:/Users/stout/Documents/Github/snippets/directory/os/test_file.txt"
)
print(f"Pad naar projectfolder: {pad}")
print(f"Voorbeeld bestand eindigt op .txt: {bestand}")
print(f"Eindigt dit bestand inderdaad op .txt? {bestand.endswith('.txt')}\n")

# Loop door alle bestanden in de huidige werkdirectory en toon bestanden met extensie .txt
print("📝 Bestanden die eindigen op .txt:")
for item in os.listdir():
    volledig_pad = os.path.join(os.getcwd(), item)
    if os.path.isfile(volledig_pad) and item.endswith(".txt"):
        print(f" - Bestand eindigt op .txt: {item}")

print("\n")

# Toon overzicht van alle bestanden en mappen in de huidige werkdirectory
print("Alle bestanden en mappen in de huidige werk directory:")
for item in os.listdir():
    volledig_pad = os.path.join(os.getcwd(), item)
    if os.path.isfile(volledig_pad):
        print(f"📄 Bestand: {item}")
    elif os.path.isdir(volledig_pad):
        print(f"📁 Map: {item}")

print()

# 🔧 Extra Functionaliteit:
# Maak een nieuwe backup-map aan als deze nog niet bestaat.
os.makedirs("backup", exist_ok=True)
print("✅ Map 'backup' gecontroleerd (gemaakt indien nodig).")

# Hernoem en verplaats het bestand 'test_file.txt' naar de nieuwe 'backup'-map.
oud_bestand = "test_file.txt"
nieuw_bestand = os.path.join("backup", "test_file_backup.txt")

# Check of het bestand bestaat voordat we het verplaatsen om fouten te voorkomen.
print("voorbeeldjeeee")
print(os.path(file))


if os.path.isfile(oud_bestand):
    os.rename(oud_bestand, nieuw_bestand)
    print(f"✅ '{oud_bestand}' verplaatst en hernoemd naar '{nieuw_bestand}'.")
else:
    print(f"⚠️ Bestand '{oud_bestand}' niet gevonden!")
