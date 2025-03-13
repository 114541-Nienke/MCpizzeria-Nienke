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
 # Maak een nieuwe tabel met 3 kolommen: id, naam, prijs
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
                   aantal_uur INTEGER,
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
    print("gegevens toegevoegd")
    printTabel("tbl_NAWGegevens")

# def verwijderPizza(gerechtNaam):
#     cursor.execute("DELETE FROM tbl_pizzas WHERE gerechtNaam = ?", (gerechtNaam,))
#     print("Gerecht verwijderd uit 'tbl_pizzas':", gerechtNaam )
#     db.commit() #gegevens naar de database wegschrijven
#     printTabel("tbl_pizzas")

# def pasGerechtAan(gerechtID, nieuweGerechtNaam, nieuwePrijs):
#     cursor.execute("UPDATE tbl_pizzas SET gerechtNaam = ?, gerechtPrijs = ? WHERE gerechtID = ?", (nieuweGerechtNaam, nieuwePrijs, gerechtID ))
#     db.commit() #gegevens naar de database wegschrijven
#     print("Gerecht aangepast")
#     printTabel("tbl_pizzas")

# def voegKlantToe(naam_nieuwe_klant):
#     cursor.execute("INSERT INTO tbl_klanten VALUES(NULL, ?)", (naam_nieuwe_klant,))
#     db.commit()
#     print("Klant toegevoegd:")
#     printTabel("tbl_klanten")

# #Zoek alle gegevens over klant met ingevoerde naam
# def zoekKlantInTabel(ingevoerde_klantnaam):
#     cursor.execute("SELECT * FROM tbl_klanten WHERE klantAchternaam = ?", (ingevoerde_klantnaam,))
#     zoek_resultaat = cursor.fetchall()
#     if zoek_resultaat == []: #resultaat is leeg, geen gerecht gevonden
#         print("Geen klant gevonden met achternaam", ingevoerde_klantnaam)
#         print("Klant wordt nu toegevoegd.")
#         cursor.execute("INSERT INTO tbl_klanten VALUES(NULL, ? )", (ingevoerde_klantnaam, ))
#         db.commit() #gegevens in de database zetten
#         print("Klant toegevoegd aan 'tbl_klanten':" + ingevoerde_klantnaam )
#         printTabel("tbl_klanten")
#         #nu dat klant in tabel is gezet, kunnen we zijn gegevens ophalen
#         cursor.execute("SELECT * FROM tbl_klanten WHERE klantAchternaam = ?",(ingevoerde_klantnaam,))
#         zoek_resultaat = cursor.fetchall()
    
#     return zoek_resultaat

# def zoekPizzaInTabel(ingevoerde_pizza):
#     cursor.execute("SELECT * FROM tbl_pizzas WHERE gerechtNaam = ?",(ingevoerde_pizza,))
#     zoek_resultaat = cursor.fetchall()
#     return zoek_resultaat

# def vraagOpGegevensPizzaTabel():
#     cursor.execute("SELECT * FROM tbl_pizzas")
#     resultaat = cursor.fetchall()
#     print("Tabel tbl_pizzas:", resultaat)
#     return resultaat

# def voegToeAanWinkelWagen(klantNr, gerechtID, aantal):
#     cursor.execute("INSERT INTO tbl_winkelWagen VALUES(NULL, ?, ?, ?)", (klantNr, gerechtID, aantal,))
#     db.commit()#gegevens in de database zetten
#     printTabel("tbl_winkelWagen")

# def vraagOpGegevensWinkelWagenTabel():
#     cursor.execute("SELECT * FROM tbl_winkelWagen")
#     resultaat = cursor.fetchall()
#     print("Tabel tbl_winkelWagen:", resultaat)
#     return resultaat

# ### --------- Hoofdprogramma  ---------------

maakTabellenAan()

# #Voeg klanten toe aan tabel:
voegDocentToe("WEER","Renske", "", "Weeda")
voegDocentToe("COUM","Mark","", "Coumans")

# #Voeg pizza's toe aan tabel:
# voegPizzaToe("Margarita", 9.50)
# voegPizzaToe("Hawaii", 12.25)
# voegPizzaToe("Salami", 10.00)

# #zoekKlantInTabel("Smit")
