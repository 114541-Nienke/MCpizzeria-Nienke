# Dit bestand zorgt voor de gebruikersinterface (GUI)van onze programma.
# Vul hier de naam van je programma in:
#
#
# Vul hier jullie namen in:
# Alex Goverde, Nienke Schilders
#
#


### --------- Bibliotheken en globale variabelen -----------------
from tkinter import *
import MCdocentenSQL

### ---------  Functie definities  -----------------
# def zoekKlant():
#     #haal de ingevoerde_klantnaam op uit het invoerveld en gebruik dit om met SQL de klant in database te vinden
#     gevonden_klanten = MCPizzeriaSQL.zoekKlantInTabel(ingevoerde_klantnaam.get())
#     print(gevonden_klanten) # om te testen
#     invoerveldKlantnaam.delete(0, END) #invoerveld voor naam leeg maken
#     invoerveldKlantNr.delete(0, END) #invoerveld voor klantNr leeg maken
#     for rij in gevonden_klanten: #voor elke rij dat de query oplevert
#         #toon klantnummer, de eerste kolom uit het resultaat in de invoerveld
#         invoerveldKlantNr.insert(END, rij[0]) 
#     #toon klantAchternaam, de tweede kolom uit het resultaat in de invoerveld
#     invoerveldKlantnaam.insert(END, rij[1]) 

# def zoekPizza(): 
#     gevonden_pizza = MCPizzeriaSQL.zoekPizzaInTabel(ingevoerde_pizza.get())
#     print(gevonden_pizza)

# def toonMenuInListbox():
#     listboxMenu.delete(0, END) #maak de listbox leeg
#     pizza_tabel = MCPizzeriaSQL.vraagOpGegevensPizzaTabel()
#     listboxMenu.insert(0, "ID Gerecht Prijs")
#     for regel in pizza_tabel:
#         listboxMenu.insert(END, regel) #voeg elke regel uit resultaat in listboxMenu

# def voegToeAanWinkelWagen():
#     klantNr = invoerveldKlantNr.get()
#     gerechtID = ingevoerde_geselecteerdePizza.get()
#     aantal = aantalGekozen.get()
#     MCPizzeriaSQL.voegToeAanWinkelWagen(klantNr, gerechtID, aantal )
#     winkelwagen_tabel = MCPizzeriaSQL.vraagOpGegevensWinkelWagenTabel()
#     listboxWinkelwagen.delete(0, END) #listbox eerst even leeg maken
#     for regel in winkelwagen_tabel:
#         listboxWinkelwagen.insert(END, regel)


# ### functie voor het selecteren van een rij uit de listbox en deze in een andere veld te plaatsen
# def haalGeselecteerdeRijOp(event):
#     #bepaal op welke regel er geklikt is
#     geselecteerdeRegelInLijst = listboxMenu.curselection()[0] 
#     #haal tekst uit die regel
#     geselecteerdeTekst = listboxMenu.get(geselecteerdeRegelInLijst) 
#     #verwijder tekst uit veld waar je in wilt schrijven, voor het geval er al iets staat
#     invoerveldGeselecteerdePizza.delete(0, END) 
#     #zet tekst in veld
#     invoerveldGeselecteerdePizza.insert(0, geselecteerdeTekst)

# ### --------- Hoofdprogramma  ---------------

venster = Tk()
venster.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
venster.wm_title("MC Docenten")

labelIntro = Label(venster, text="Welkom!")
labelIntro.grid(row=0, column=0, sticky="W")

knopSluit = Button(venster, text="Sluiten", width=10, command=venster.destroy)
knopSluit.grid(row=17, column=4)

labelVoornaam = Label(venster, text="Voornaam:")
labelVoornaam.grid(row=1, column=0, sticky="W")

# ingevoerde_klantnaam = StringVar()
# invoerveldKlantnaam = Entry(venster, textvariable=ingevoerde_klantnaam)
# invoerveldKlantnaam.grid(row=1, column=1, sticky="W")

labelAfkorting= Label(venster, text="Afkorting:")
labelAfkorting.grid(row=2, column=0, sticky="W")

# invoerveldKlantNr = Entry(venster)
# invoerveldKlantNr.grid(row=2, column=1, sticky="W")

# knopZoekOpKlantnaam = Button(venster, text="Zoek klant", width=12, command=zoekKlant)
# knopZoekOpKlantnaam.grid(row=1, column=4)

labelTussenvoegsel = Label(venster, text="Tussenvoegsel:")
labelTussenvoegsel.grid(row=4, column=0, sticky="W")

# ingevoerde_pizza= StringVar()
# invoerveldPizzanaam = Entry(venster, textvariable=ingevoerde_pizza)
# invoerveldPizzanaam.grid(row=4, column=1, sticky="W")

# knopZoekOpPizzaNaam = Button(venster, text="Zoek pizza", width=12, command=zoekPizza)
# knopZoekOpPizzaNaam.grid(row=4, column=4)

labelAchternaam = Label(venster, text="Achternaam:")
labelAchternaam.grid(row=5, column=0, sticky="W")

# listboxMenu = Listbox(venster, height=6, width=50)
# listboxMenu.grid(row=5, column=1, rowspan=6, columnspan=2, sticky="W")
# listboxMenu.bind('<<ListboxSelect>>', haalGeselecteerdeRijOp)

# knopToonPizzas = Button(venster, text="Toon alle pizza's", width=12, command=toonMenuInListbox)
# knopToonPizzas.grid(row=5, column=4)

# labelGekozenPizza = Label(venster, text="Gekozen pizza:")
# labelGekozenPizza.grid(row=14, column=0, sticky="W")

# ingevoerde_geselecteerdePizza = StringVar()
# invoerveldGeselecteerdePizza= Entry(venster, textvariable=ingevoerde_geselecteerdePizza)
# invoerveldGeselecteerdePizza.grid(row=14, column=1, sticky="W")

# labelAantal = Label(venster, text="Aantal:")
# labelAantal.grid(row=15, column=0, sticky="W")

# aantalGekozen = IntVar()
# aantalGekozen.set(1)
# optionMenuPizzaAantal = OptionMenu(venster, aantalGekozen, 1,2,3)
# optionMenuPizzaAantal.grid(row=15, column=1)

# knopVoegToe = Button(venster, text="Voeg toe", width=12, command=voegToeAanWinkelWagen)
# knopVoegToe.grid(row=15 , column=4)

# labelBestelling = Label(venster, text="Bestelling:")
# labelBestelling.grid(row=16, column=0, sticky="W")

# listboxWinkelwagen= Listbox(venster, height=6, width=50)
# listboxWinkelwagen.grid(row=16, column=1, rowspan=6, columnspan=2, sticky="W")
# listboxWinkelwagen.bind('<<ListboxSelect>>', haalGeselecteerdeRijOp)

# #reageert op gebruikersinvoer, deze regel als laatste laten staan
# venster.mainloop()
# zoekKlant()

