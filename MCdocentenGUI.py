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
# Deze functie vult de gegevens die bij een voornaam horen in en checkt of de invoer klopt. Hij laat ook een plaatjes per docent zien.
def zoekDocent():
    ingevoerde_voornaam_tekst = (invoerveldVoornaam.get())  # Haal de invoer op
    # Checkt of de invoer geen cijfers bevat
    if not ingevoerde_voornaam_tekst.isalpha():
        labelFoutmelding.config(text="Alleen letters toegestaan!", fg="red")
        invoerveldVoornaam.delete(0, END)
        return 
    # Checkt de lengte van de invoer
    if len(ingevoerde_voornaam_tekst) > 15:
        labelFoutmelding.config(text="Max 15 tekens!", fg="red")
        invoerveldVoornaam.delete(0, END)
        return
    gevonden_voornaam = MCdocentenSQL.zoekDocentInTabel(ingevoerde_voornaam_tekst)
    # Checkt of de naam in de tabel staat
    if not gevonden_voornaam:  
        labelFoutmelding.config(text="Deze docent bestaat niet", fg="red")
        invoerveldVoornaam.delete(0, END)
        return  
    print(gevonden_voornaam) 
    #Haalt de foutmelding weg als de invoer klopt
    labelFoutmelding.config(text="")  
    # Verwijdert de gegevens zodat er nieuwe kun worden ingevuld
    invoerveldAfkorting.delete(0, END)
    invoerveldAchternaam.delete(0, END)
    invoerveldTussenvoegsel.delete(0, END)
    
    # Zet bijpassende waardes in de invoervelden
    for rij in gevonden_voornaam:  # Voor elke rij in het resultaat
        invoerveldAfkorting.insert(END, rij[0])
        invoerveldTussenvoegsel.insert(END, rij[2])
        invoerveldAchternaam.insert(END, rij[3]) 

    #Laat de plaatjes zien
    if ingevoerde_voornaam_tekst == "Mark":
        padFotoGeselecteerdeDocent =  ImageTk.PhotoImage(file="Markie.png")
        fotoDocent.config(image=padFotoGeselecteerdeDocent)
        fotoDocent.image = padFotoGeselecteerdeDocent
        return padFotoGeselecteerdeDocent
    if ingevoerde_voornaam_tekst == "Renske":
        padFotoGeselecteerdeDocent =  ImageTk.PhotoImage(file="renske.png")
        fotoDocent.config(image=padFotoGeselecteerdeDocent)
        fotoDocent.image = padFotoGeselecteerdeDocent
        return padFotoGeselecteerdeDocent
    if ingevoerde_voornaam_tekst == "Laurens":
        padFotoGeselecteerdeDocent =  ImageTk.PhotoImage(file="laurens.png")
        fotoDocent.config(image=padFotoGeselecteerdeDocent)
        fotoDocent.image = padFotoGeselecteerdeDocent
        return padFotoGeselecteerdeDocent

def toonVakkenInListbox():
    listboxVakken.delete(0, END) #maak de listbox leeg
    vak_tabel = MCdocentenSQL.vraagOpGegevensVakken()
    listboxVakken.insert(0, "Alle vakken:")
    for regel in vak_tabel:
        listboxVakken.insert(END, regel) #voeg elke regel uit resultaat in listboxMenu

# Hoort bij het stukje vakken
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
    invoerveldAantalLessen.delete(0,END) 
    for rij in gevonden_gegevens: #voor elke rij dat de query oplevert
        invoerveldAantalLessen.insert(END, rij[3]) 

def toonAfkortingenInListbox():
    listboxAfkortingen.delete(0, END) #maak de listbox leeg
    afkorting_tabel = MCdocentenSQL.vraagOpGegevensAfkortingen()
    listboxAfkortingen.insert(0, "Alle afkortingen:")
    for regel in afkorting_tabel:
        listboxAfkortingen.insert(END, regel) #voeg elke regel uit resultaat in listboxMenu

# Hoort bij het stukje afkortingen
def haalGeselecteerdeRijOp1(event):
    #bepaal op welke regel er geklikt is
    geselecteerdeRegelInLijst = listboxAfkortingen.curselection()[0] 
    #haal tekst uit die regel
    geselecteerdeTekst = listboxAfkortingen.get(geselecteerdeRegelInLijst) 
    print(geselecteerdeTekst)
    #verwijder tekst uit veld waar je in wilt schrijven, voor het geval er al iets staat
    invoerveldGekozenAfkorting.delete(0, END) 
    #zet tekst in veld
    invoerveldGekozenAfkorting.insert(0, geselecteerdeTekst[0])

def zoekAfkorting():
    #haal de ingevoerde_klantnaam op uit het invoerveld en gebruik dit om met SQL de klant in database te vinden
    gevonden_gegevens = MCdocentenSQL.zoekAfkortinginTabel(ingevoerde_afkorting.get())
    print(gevonden_gegevens) # om te testen
    invoerveldVakCombi.delete(0,END) 
    for rij in gevonden_gegevens: #voor elke rij dat de query oplevert
        invoerveldVakCombi.insert(END, rij[0]) 

### --------- Hoofdprogramma  ---------------

venster = Tk()
venster.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
venster.wm_title("MC Docenten")
venster.config(bg="orange")

knopSluit = Button(venster, text="Sluiten", width=10, command=venster.destroy)
knopSluit.grid(row=100, column=300, sticky="E")

# Stukje links boven 
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

labelFoutmelding = Label(venster, text="", fg="red", bg="orange")
labelFoutmelding.grid(row=5, column=0, padx=15, pady=2, sticky="W")

knopZoekVoornaam= Button(venster, text="Zoek docent", width=12, command= zoekDocent)
knopZoekVoornaam.grid(row=1, column=20, padx=25)

fotoDocent = Label(venster, bg="orange")
fotoDocent.grid(row=6, column=0, rowspan= 35, columnspan=15, padx=15, pady=5, sticky="W")

# Stukje linksonder
labelOranje = Label(venster, text="", bg="orange")
labelOranje.grid(row=41, column=0, rowspan=20, columnspan=5)

labelVakken = Label(venster, text="Vakken:")
labelVakken.grid(row=61, column=0, sticky="W", padx=15, pady=2)

listboxVakken = Listbox(venster, height = 6, width = 20)
listboxVakken.grid(row=61, column=1, rowspan=6, columnspan=20, sticky="W")
listboxVakken.bind('<<ListboxSelect>>', haalGeselecteerdeRijOp)

scrollbarlistbox = Scrollbar(venster)
scrollbarlistbox.grid(row=61, column=1, rowspan=6, sticky="E")
listboxVakken.config(yscrollcommand=scrollbarlistbox.set)
scrollbarlistbox.config(command=listboxVakken.yview)

labelGekozenVak = Label(venster, text="Gekozen vak:")
labelGekozenVak.grid(row=68, column=0, sticky="W", padx=15, pady=2)

ingevoerde_vak = StringVar()
invoerveldGekozenVak = Entry(venster, textvariable=ingevoerde_vak)
invoerveldGekozenVak.grid(row=68, column=1, sticky="W")

knopToonVakken= Button(venster, text="Toon alle vakken", width=12, command=toonVakkenInListbox)
knopToonVakken.grid(row=61, column=15, sticky="W", padx=20, pady=2)

labelNiveau = Label(venster, text="Niveau:")
labelNiveau.grid(row=69, column=0, sticky="W", padx=15, pady=2)

niveauGekozen = StringVar()
niveauGekozen.set("Havo")
optionMenuNiveau = OptionMenu(venster, niveauGekozen, "Havo", "Vwo")
optionMenuNiveau.grid(row=69, column=1)

labelAantalLessen = Label(venster, text="Aantal lessen:")
labelAantalLessen.grid(row=70, column=0, sticky="W", padx=15, pady=2)

ingevoerde_aantal_lessen = StringVar()
invoerveldAantalLessen = Entry(venster, textvariable=ingevoerde_aantal_lessen)
invoerveldAantalLessen.grid(row=70, column=1, sticky="W")

knopZoekVak= Button(venster, text="Zoek vak", width=12, command=zoekVak)
knopZoekVak.grid(row=68, column=20, sticky="W", padx=20, pady=2)

# fotoPad = "school.png"
# padFoto =  ImageTk.PhotoImage(file=fotoPad)
# fotoDocent = Label(venster, image=padFoto)
# fotoDocent.grid(row=20, column=60, rowspan= 40, columnspan=60, padx=20, pady=2, sticky="E")

# Stukje rechtsboven
labelOranje1 = Label(venster, height = 1, width = 50, text="", bg="orange")
labelOranje1.grid(row=1, column=25, rowspan=10, columnspan=20)

labelAfkortingLijst = Label(venster, text="Afkorting:")
labelAfkortingLijst.grid(row=1, column=55, sticky="W", padx=15, pady=2)

listboxAfkortingen = Listbox(venster, height = 6, width = 20)
listboxAfkortingen.grid(row=1, column=56, sticky="W", rowspan=6, columnspan=20)
listboxAfkortingen.bind('<<ListboxSelect>>', haalGeselecteerdeRijOp1)

knopToonAfkortingen= Button(venster, text="Toon alle afkortingen", width=18, command=toonAfkortingenInListbox)
knopToonAfkortingen.grid(row=1, column=60, padx=20, pady=2)

labelGekozenAfkorting = Label(venster, text="Gekozen afkorting:")
labelGekozenAfkorting.grid(row=8, column=55, sticky="W", padx=15, pady=2)

ingevoerde_afkorting = StringVar()
invoerveldGekozenAfkorting = Entry(venster, textvariable=ingevoerde_afkorting)
invoerveldGekozenAfkorting.grid(row=8, column=56, sticky="W")

labelVakCombi = Label(venster, text="Vak:")
labelVakCombi.grid(row=9, column=55, sticky="W", padx=15, pady=2)

ingevoerde_vak_combi = StringVar()
invoerveldVakCombi = Entry(venster, textvariable=ingevoerde_vak_combi)
invoerveldVakCombi.grid(row=9, column=56, sticky="W")

knopZoekAfkorting= Button(venster, text="Zoek Afkorting", width=12, command= zoekAfkorting)
knopZoekAfkorting.grid(row=8, column=60, padx=25, sticky="W")

# #reageert op gebruikersinvoer, deze regel als laatste laten staan
venster.mainloop()
# zoekKlant()

