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
def zoekDocent():
    #haal de ingevoerde_klantnaam op uit het invoerveld en gebruik dit om met SQL de klant in database te vinden
    gevonden_voornaam = MCdocentenSQL.zoekDocentInTabel(ingevoerde_voornaam.get())
    print(gevonden_voornaam) # om te testen
    invoerveldVoornaam.delete(0, END)
    invoerveldAfkorting.delete(0, END)
    invoerveldAchternaam.delete(0,END) 
    invoerveldAantalUur.delete(0, END)
    for rij in gevonden_voornaam: #voor elke rij dat de query oplevert
        #toon klantnummer, de eerste kolom uit het resultaat in de invoerveld
        invoerveldAfkorting.insert(END, rij[0]) 
        invoerveldAchternaam.insert(END, rij[3]) 
        invoerveldAantalUur.insert(END, R)

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

ingevoerde_voornaam = StringVar()
invoerveldVoornaam = Entry(venster, textvariable=ingevoerde_voornaam)
invoerveldVoornaam.grid(row=1, column=1, sticky="W")

labelAfkorting= Label(venster, text="Afkorting:")
labelAfkorting.grid(row=3, column=0, sticky="W")

labelTussenvoegsel = Label(venster, text="Tussenvoegsel:")
labelTussenvoegsel.grid(row=4, column=0, sticky="W")

labelAchternaam = Label(venster, text="Achternaam:")
labelAchternaam.grid(row=5, column=0, sticky="W")

ingevoerde_afkorting = StringVar()
invoerveldAfkorting = Entry(venster, textvariable=ingevoerde_afkorting)
invoerveldAfkorting.grid(row=3, column=1, sticky="W")

ingevoerde_tussenvoegsel = StringVar()
invoerveldTussenvoegsel = Entry(venster, textvariable=ingevoerde_tussenvoegsel)
invoerveldTussenvoegsel.grid(row=4, column=1, sticky="W")

ingevoerde_achternaam = StringVar()
invoerveldAchternaam = Entry(venster, textvariable=ingevoerde_achternaam)
invoerveldAchternaam.grid(row=5, column=1, sticky="W")

knopZoekVoornaam= Button(venster, text="Zoek docent", width=12, command=zoekDocent)
knopZoekVoornaam.grid(row=2, column=20)

# knopZoekOpPizzaNaam = Button(venster, text="Zoek pizza", width=12, command=zoekPizza)
# knopZoekOpPizzaNaam.grid(row=4, column=4)

# listboxMenu = Listbox(venster, height=6, width=50)
# listboxMenu.grid(row=5, column=1, rowspan=6, columnspan=2, sticky="W")
# listboxMenu.bind('<<ListboxSelect>>', haalGeselecteerdeRijOp)

# knopToonPizzas = Button(venster, text="Toon alle pizza's", width=12, command=toonMenuInListbox)
# knopToonPizzas.grid(row=5, column=4)

# labelAantal = Label(venster, text="Aantal:")
# labelAantal.grid(row=15, column=0, sticky="W")

# aantalGekozen = IntVar()
# aantalGekozen.set(1)
# optionMenuPizzaAantal = OptionMenu(venster, aantalGekozen, 1,2,3)
# optionMenuPizzaAantal.grid(row=15, column=1)

# knopVoegToe = Button(venster, text="Voeg toe", width=12, command=voegToeAanWinkelWagen)
# knopVoegToe.grid(row=15 , column=4)

# listboxWinkelwagen= Listbox(venster, height=6, width=50)
# listboxWinkelwagen.grid(row=16, column=1, rowspan=6, columnspan=2, sticky="W")
# listboxWinkelwagen.bind('<<ListboxSelect>>', haalGeselecteerdeRijOp)

# #reageert op gebruikersinvoer, deze regel als laatste laten staan
venster.mainloop()
# zoekKlant()

