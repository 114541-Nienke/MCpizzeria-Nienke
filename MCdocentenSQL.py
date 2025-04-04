# Vul hier de naam van je programma in:
#
#
# Vul hier jullie namen in:
# Alex Goverde, Nienke Schilders
#
#


### --------- Bibliotheken en globale variabelen -----------------

import sqlite3
with sqlite3.connect("MCDocenten.db") as db:
    cursor = db.cursor()#cursor is object waarmee je data uit de database kan halen


### ---------  Functie definities  -----------------

def maakTabellenAan():
    cursor.execute("""CREATE TABLE IF NOT EXISTS tbl_NAWGegevens(
                   Afkorting TEXT NOT NULL PRIMARY KEY,
                    Voornaam TEXT NOT NULL, 
                   Tussenvoegsel TEXT, 
                   Achternaam TEXT NOT NULL);""")
    print("Tabel 'tbl_NAWGegevens' aangemaakt.")
    cursor.execute("""CREATE TABLE IF NOT EXISTS tbl_VakGegevens(
                   vak_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                   vak_naam TEXT NOT NULL);""")
    print("Tabel 'tbl_VakGegevens' aangemaakt.")
    cursor.execute("""CREATE TABLE IF NOT EXISTS tbl_VakDocentGegevens(
                   combi_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                   aantal_uur INTEGER,
                   vak_id INTEGER NOT NULL,
                   Afkorting TEXT NOT NULL,
                   FOREIGN KEY(vak_id) REFERENCES tbl_vakGegevens(vak_id)
                   FOREIGN KEY(Afkorting) REFERENCES tbl_NAWGegevens(Afkorting));""")
    print("Tabel 'tbl_VakDocentGegevens' aangemaakt.")
    cursor.execute("""CREATE TABLE IF NOT EXISTS tbl_VakPerNiveauGegevens(
                   Niveau_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                   aantal_lessen INTEGER NOT NULL, 
                   Niveau TEXT NOT NULL,
                   vak_id INTEGER NOT NULL,
                    FOREIGN KEY(vak_id) REFERENCES tbl_vakGegevens(vak_id));""")
    print("Tabel 'tbl_VakDocentGegevens' aangemaakt.")


def printTabel(tabel_naam):
    cursor.execute("SELECT * FROM " + tabel_naam) #SQL om ALLE gegevens te halen
    opgehaalde_gegevens = cursor.fetchall() #sla gegevens op in een variabele
    print("Tabel " + tabel_naam + ":", opgehaalde_gegevens) #druk gegevens af

def voegDocentToe(nieuwe_afkorting, nieuwe_voornaam, nieuw_tussenvoegsel, nieuwe_achternaam):
    cursor.execute("INSERT INTO tbl_NAWGegevens VALUES(?, ?, ?, ? )", (nieuwe_afkorting, nieuwe_voornaam, nieuw_tussenvoegsel, nieuwe_achternaam))
    db.commit() #gegevens naar de database wegschrijven

def voegVakToe(nieuw_vak):
    cursor.execute("INSERT INTO tbl_VakGegevens VALUES(NULL, ?)", (nieuw_vak,))
    db.commit()

def voegVakDocentToe(nieuw_aantal_uur, nieuw_vak_id, nieuwe_afkorting):
    cursor.execute("INSERT INTO tbl_VakDocentGegevens VALUES(NULL, ?, ?, ?)", (nieuw_aantal_uur, nieuw_vak_id, nieuwe_afkorting))
    db.commit()#gegevens in de database zetten

def voegVakNiveauToe(nieuw_aantal_lessen, nieuw_niveau, nieuw_vak_id):
    cursor.execute("INSERT INTO tbl_VakPerNiveauGegevens VALUES(NULL, ?, ?, ?)", (nieuw_aantal_lessen, nieuw_niveau, nieuw_vak_id))
    db.commit()#gegevens in de database zetten

#Zoek alle gegevens over klant met ingevoerde naam
def zoekDocentInTabel(ingevoerde_voornaam):
    cursor.execute("SELECT * FROM tbl_NAWGegevens WHERE voornaam = ?", (ingevoerde_voornaam,))
    zoek_resultaat = cursor.fetchall()
    if zoek_resultaat == []: 
        print("Geen docent gevonden met voornaam", ingevoerde_voornaam)
        cursor.execute("SELECT * FROM tbl_NAWGegevens WHERE voornaam = ?",(ingevoerde_voornaam,))
        zoek_resultaat = cursor.fetchall()
    return zoek_resultaat

def vraagOpGegevensVakken():
    cursor.execute("SELECT * FROM tbl_VakGegevens")
    resultaat = cursor.fetchall()
    print("Tabel tbl_VakGegevens:", resultaat)
    return resultaat

def zoekVakinTabel(ingevoerde_vak, niveauGekozen):
    cursor.execute("SELECT * FROM tbl_VakGegevens LEFT JOIN tbl_VakPerNiveauGegevens ON tbl_VakGegevens.vak_id = tbl_VakPerNiveauGegevens.vak_id  WHERE vak_naam = ? AND Niveau = ? " , (ingevoerde_vak, niveauGekozen,))
    vak_resultaat = cursor.fetchall()
    if vak_resultaat == []:  
        cursor.execute("SELECT * FROM tbl_VakGegevens LEFT JOIN tbl_VakPerNiveauGegevens ON tbl_VakGegevens.vak_id = tbl_VakPerNiveauGegevens.vak_id WHERE vak_naam = ? AND Niveau = ?" ,(ingevoerde_vak, niveauGekozen,))
        vak_resultaat = cursor.fetchall()
    return vak_resultaat

def vraagOpGegevensAfkortingen():
    cursor.execute("SELECT Afkorting FROM tbl_NAWGegevens")
    resultaat = cursor.fetchall()
    print("Tabel tbl_NAWGegevens:", resultaat)
    return resultaat

def zoekAfkortinginTabel(ingevoerde_afkorting):
    cursor.execute("SELECT vak_naam FROM tbl_NAWGegevens LEFT JOIN tbl_VakDocentGegevens ON tbl_NAWGegevens.Afkorting = tbl_VakDocentGegevens.Afkorting LEFT JOIN tbl_VakGegevens ON tbl_VakDocentGegevens.vak_id = tbl_VakGegevens.vak_id WHERE tbl_NAWGegevens.Afkorting = ? ",(ingevoerde_afkorting,))
    afkorting_resultaat = cursor.fetchall()
    if afkorting_resultaat == []:  
        cursor.execute("SELECT vak_naam FROM tbl_NAWGegevens LEFT JOIN tbl_VakDocentGegevens ON tbl_NAWGegevens.Afkorting = tbl_VakDocentGegevens.Afkorting LEFT JOIN tbl_VakGegevens ON tbl_VakDocentGegevens.vak_id = tbl_VakGegevens.vak_id WHERE tbl_NAWGegevens.Afkorting = ?" ,(ingevoerde_afkorting,))
        afkorting_resultaat = cursor.fetchall()
    return afkorting_resultaat
# ### --------- Hoofdprogramma  ---------------

maakTabellenAan()

# #Voeg docent toe aan tabel:
voegDocentToe("JALA", "Laurens", "", "Jansen")
voegDocentToe("WEER","Renske", "", "Weeda")
voegDocentToe("COUM","Mark","", "Coumans")
printTabel("tbl_NAWGegevens")

#Voeg vak toe aan tabel:
voegVakToe("Informatica")
voegVakToe("Wiskunde A")
voegVakToe("Wiskunde B")
voegVakToe("Scheikunde")
printTabel("tbl_VakGegevens")

# invullen tabel vak docent
voegVakDocentToe("10", "1", "WEER")
voegVakDocentToe("8", "2", "COUM")
voegVakDocentToe("20", "3", "COUM")
voegVakDocentToe("16", "4", "JALA")
printTabel("tbl_VakDocentGegevens")

# invullen tabel vak Niveau
voegVakNiveauToe("2", "Havo", "1")
voegVakNiveauToe("2", "Havo", "2")
voegVakNiveauToe("2", "Havo", "3")
voegVakNiveauToe("2", "Havo", "4")
voegVakNiveauToe("2", "Vwo", "1")
voegVakNiveauToe("3", "Vwo", "2")
voegVakNiveauToe("3", "Vwo", "3")
voegVakNiveauToe("2", "Vwo", "4")
printTabel("tbl_VakPerNiveauGegevens")

