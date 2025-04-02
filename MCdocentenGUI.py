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
from tkinter import Tk, Label
from PIL import Image, ImageTk 
import tkinter.messagebox

### ---------  Functie definities  -----------------
def zoekDocent():
    #haal de ingevoerde_klantnaam op uit het invoerveld en gebruik dit om met SQL de klant in database te vinden
    gevonden_voornaam = MCdocentenSQL.zoekDocentInTabel(ingevoerde_voornaam.get())
    print(gevonden_voornaam) # om te testen
    invoerveldAfkorting.delete(0, END)
    invoerveldAchternaam.delete(0,END) 
    for rij in gevonden_voornaam: #voor elke rij dat de query oplevert
        #toon klantnummer, de eerste kolom uit het resultaat in de invoerveld
        invoerveldAfkorting.insert(END, rij[0]) 
        invoerveldTussenvoegsel.insert(END, rij[2])
        invoerveldAchternaam.insert(END, rij[3]) 

# def zoekPizza(): 
#     gevonden_pizza = MCPizzeriaSQL.zoekPizzaInTabel(ingevoerde_pizza.get())
#     print(gevonden_pizza)

def toonVakkenInListbox():
    listboxVakken.delete(0, END) #maak de listbox leeg
    vak_tabel = MCdocentenSQL.vraagOpGegevensVakken()
    listboxVakken.insert(0, "Alle vakken:")
    for regel in vak_tabel:
        listboxVakken.insert(END, regel) #voeg elke regel uit resultaat in listboxMenu

#maakt een pop-up met tekst
def onClick(): 
    tkinter.messagebox.showinfo("Dit is een pop-up venster!")
#Zorgt voor knop waar dat een pop-up opent
 
# def voegToeAanWinkelWagen():
#     klantNr = invoerveldKlantNr.get()
#     gerechtID = ingevoerde_geselecteerdePizza.get()
#     aantal = aantalGekozen.get()
#     MCPizzeriaSQL.voegToeAanWinkelWagen(klantNr, gerechtID, aantal )
#     winkelwagen_tabel = MCPizzeriaSQL.vraagOpGegevensWinkelWagenTabel()
#     listboxWinkelwagen.delete(0, END) #listbox eerst even leeg maken
#     for regel in winkelwagen_tabel:
#         listboxWinkelwagen.insert(END, regel)


### functie voor het selecteren van een rij uit de listbox en deze in een andere veld te plaatsen
def haalGeselecteerdeRijOp(event):
    #bepaal op welke regel er geklikt is
    geselecteerdeRegelInLijst = listboxVakken.curselection()[0] 
    #haal tekst uit die regel
    geselecteerdeTekst = listboxVakken.get(geselecteerdeRegelInLijst) 
    print(geselecteerdeTekst)
    #verwijder tekst uit veld waar je in wilt schrijven, voor het geval er al iets staat
    invoerveldGekozenVak.delete(0, END) 
    #zet tekst in veld
    invoerveldGekozenVak.insert(0, geselecteerdeTekst[1])

def zoekVak():
    #haal de ingevoerde_klantnaam op uit het invoerveld en gebruik dit om met SQL de klant in database te vinden
    gevonden_gegevens = MCdocentenSQL.zoekVakinTabel(ingevoerde_vak.get(), niveauGekozen.get())
    print(gevonden_gegevens) # om te testen
    invoerveldAantalLessen.delete(0,END) 
    for rij in gevonden_gegevens: #voor elke rij dat de query oplevert
        print(rij)
        invoerveldAantalLessen.insert(END, rij[3]) 

def foutInvoer():
    ingevoerde_voornaam_tekst = invoerveldVoornaam.get()  # Haal de invoer op uit het veld

    if not ingevoerde_voornaam_tekst.isalpha():  
        print("Ongeldige invoer: alleen letters zijn toegestaan!")
        invoerveldVoornaam.delete(0, END)  # Wis het invoerveld
        labelFoutmelding.config(text="Alleen letters toegestaan!", fg="red")
        return  # Stop de functie hier

    if len(ingevoerde_voornaam_tekst) > 15:
        print("Dat zijn wel veel letters. Probeer het nog een keer")
        invoerveldVoornaam.delete(0, END)
        labelFoutmelding.config(text="Max 15 tekens!", fg="red")
        return  

    # Als alles goed is, haal de foutmelding weg


### --------- Hoofdprogramma  ---------------

venster = Tk()
venster.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
venster.wm_title("MC Docenten")
venster.config(bg="orange")

knopSluit = Button(venster, text="Sluiten", width=10, command=venster.destroy)
knopSluit.grid(row=100, column=300, sticky="E")

labelVoornaam = Label(venster, text="Voornaam:")
labelVoornaam.grid(row=1, column=0, sticky="W", padx=15, pady=2)

ingevoerde_voornaam = StringVar()
invoerveldVoornaam = Entry(venster, textvariable=ingevoerde_voornaam)
invoerveldVoornaam.grid(row=1, column=1, sticky="W")

labelTussenvoegsel = Label(venster, text="Tussenvoegsel:")
labelTussenvoegsel.grid(row=2, column=0, sticky="W", padx=15, pady=2)

ingevoerde_tussenvoegsel = StringVar()
invoerveldTussenvoegsel = Entry(venster, textvariable=ingevoerde_tussenvoegsel)
invoerveldTussenvoegsel.grid(row=2, column=1, sticky="W")

labelAchternaam = Label(venster, text="Achternaam:")
labelAchternaam.grid(row=3, column=0, sticky="W", padx=15, pady=2)

ingevoerde_achternaam = StringVar()
invoerveldAchternaam = Entry(venster, textvariable=ingevoerde_achternaam)
invoerveldAchternaam.grid(row=3, column=1, sticky="W")

labelAfkorting= Label(venster, text="Afkorting:")
labelAfkorting.grid(row=4, column=0, sticky="W", padx=15, pady=2)

ingevoerde_afkorting = StringVar()
invoerveldAfkorting = Entry(venster, textvariable=ingevoerde_afkorting)
invoerveldAfkorting.grid(row=4, column=1, sticky="W")

knopZoekVoornaam= Button(venster, text="Zoek docent", width=12, command= zoekDocent)
knopZoekVoornaam.grid(row=1, column=20, padx=25, pady=2)

labelOranje = Label(venster, height = 1, width = 50, text="", bg="orange")
labelOranje.grid(row=1, column=25, rowspan=10, columnspan=50)

labelVakken = Label(venster, text="Vakken:")
labelVakken.grid(row=1, column=75, sticky="W", padx=15, pady=2)

listboxVakken = Listbox(venster, height = 6, width = 20)
listboxVakken.grid(row=1, column=76, rowspan=6, columnspan=20)
listboxVakken.bind('<<ListboxSelect>>', haalGeselecteerdeRijOp)

scrollbarlistbox = Scrollbar(venster)
scrollbarlistbox.grid(row=1, column=76, rowspan=6, sticky="E")
listboxVakken.config(yscrollcommand=scrollbarlistbox.set)
scrollbarlistbox.config(command=listboxVakken.yview)

labelGekozenVak = Label(venster, text="Gekozen vak:")
labelGekozenVak.grid(row=7, column=75, sticky="W", padx=15, pady=2)

ingevoerde_vak = StringVar()
invoerveldGekozenVak = Entry(venster, textvariable=ingevoerde_vak)
invoerveldGekozenVak.grid(row=7, column=76, sticky="W")

knopToonVakken= Button(venster, text="Toon alle vakken", width=12, command=toonVakkenInListbox)
knopToonVakken.grid(row=1, column=130, sticky="W", padx=20, pady=2)

# knopToonPizzas = Button(venster, text="Toon alle pizza's", width=12, command=toonMenuInListbox)
# knopToonPizzas.grid(row=5, column=4)

labelNiveau = Label(venster, text="Niveau:")
labelNiveau.grid(row=8, column=75, sticky="W", padx=15, pady=2)

niveauGekozen = StringVar()
niveauGekozen.set("Havo")
optionMenuNiveau = OptionMenu(venster, niveauGekozen, "Havo", "Vwo")
optionMenuNiveau.grid(row=8, column=76)

labelAantalLessen = Label(venster, text="Aantal lessen:")
labelAantalLessen.grid(row=9, column=75, sticky="W", padx=15, pady=2)

ingevoerde_aantal_lessen = StringVar()
invoerveldAantalLessen = Entry(venster, textvariable=ingevoerde_aantal_lessen)
invoerveldAantalLessen.grid(row=9, column=76, sticky="W")

knopZoekVak= Button(venster, text="Zoek vak", width=12, command=zoekVak)
knopZoekVak.grid(row=7, column=130, sticky="W", padx=20, pady=2)

fotoPad = "Markie.png"
padFotoGeselecteerdeDocent =  ImageTk.PhotoImage(file=fotoPad)
fotoDocent = Label(venster, width=200, height=200, 
image=padFotoGeselecteerdeDocent)
fotoDocent.grid(row=18, column=0, padx=20, pady=2)


# Voeg een foutmelding-label toe in je GUI
labelFoutmelding = Label(venster, text="", fg="red")
labelFoutmelding.grid(row=2, column=2)

# Voeg een knop toe om te testen
knopCheckInvoer = Button(venster, text="Check invoer", command=foutInvoer)
knopCheckInvoer.grid(row=1, column=2, padx=10, pady=2)

# #reageert op gebruikersinvoer, deze regel als laatste laten staan
venster.mainloop()
# zoekKlant()

