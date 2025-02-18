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
import MCPizzeriaSQL


### ---------  Functie definities  -----------------
def zoekKlant():
    #haal de ingevoerde_klantnaam op uit het invoerveld en gebruik dit om met SQL de klant in database te vinden
    gevonden_klanten = MCPizzeriaSQL.zoekKlantInTabel(ingevoerde_klantnaam.get())
    print(gevonden_klanten) # om te testen
    invoerveldKlantnaam.delete(0, END) #invoerveld voor naam leeg maken
    invoerveldKlantNr.delete(0, END) #invoerveld voor klantNr leeg maken
    for rij in gevonden_klanten: #voor elke rij dat de query oplevert
        #toon klantnummer, de eerste kolom uit het resultaat in de invoerveld
        invoerveldKlantNr.insert(END, rij[0]) 
    #toon klantAchternaam, de tweede kolom uit het resultaat in de invoerveld
    invoerveldKlantnaam.insert(END, rij[1]) 

def zoekPizza(): 
    gevonden_pizza = MCPizzeriaSQL.zoekPizzaInTabel(ingevoerde_pizza.get())
    print(gevonden_pizza)

def toonMenuInListbox():
    listboxMenu.delete(0, END) #maak de listbox leeg
    pizza_tabel = MCPizzeriaSQL.vraagOpGegevensPizzaTabel()
    listboxMenu.insert(0, "ID Gerecht Prijs")
    for regel in pizza_tabel:
        listboxMenu.insert(END, regel) #voeg elke regel uit resultaat in listboxMenu


### --------- Hoofdprogramma  ---------------

venster = Tk()
venster.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
venster.wm_title("MC Pizzeria")

labelIntro = Label(venster, text="Welkom!")
labelIntro.grid(row=0, column=0, sticky="W")

knopSluit = Button(venster, text="Sluiten", width=10, command=venster.destroy)
knopSluit.grid(row=17, column=4)

labelKlantnaam = Label(venster, text="Klantnaam")
labelKlantnaam.grid(row=1, column=0, sticky="W")

ingevoerde_klantnaam = StringVar()
invoerveldKlantnaam = Entry(venster, textvariable=ingevoerde_klantnaam)
invoerveldKlantnaam.grid(row=1, column=1, sticky="W")

labelKlantnummer = Label(venster, text="Klantnummer")
labelKlantnummer.grid(row=2, column=0, sticky="W")

invoerveldKlantNr = Entry(venster)
invoerveldKlantNr.grid(row=2, column=1, sticky="W")

knopZoekOpKlantnaam = Button(venster, text="Zoek klant", width=12, command=zoekKlant)
knopZoekOpKlantnaam.grid(row=1, column=4)

labelPizzanaam = Label(venster, text="Pizzanaam:")
labelPizzanaam.grid(row=4, column=0, sticky="W")

ingevoerde_pizza= StringVar()
invoerveldPizzanaam = Entry(venster, textvariable=ingevoerde_pizza)
invoerveldPizzanaam.grid(row=4, column=1, sticky="W")

knopZoekOpPizzaNaam = Button(venster, text="Zoek pizza", width=12, command=zoekPizza)
knopZoekOpPizzaNaam.grid(row=4, column=4)

labelMogelijkheden = Label(venster, text="Mogelijkheden:")
labelMogelijkheden.grid(row=5, column=0, sticky="W")

listboxMenu = Listbox(venster, height=6, width=50)
listboxMenu.grid(row=5, column=1, rowspan=6, columnspan=2, sticky="W")

knopToonPizzas = Button(venster, text="Toon alle pizza's", width=12, command=toonMenuInListbox)
knopToonPizzas.grid(row=5, column=4)


#reageert op gebruikersinvoer, deze regel als laatste laten staan
venster.mainloop()
zoekKlant()

