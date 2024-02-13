#importierten Module die man für das Programm braucht
# mit * importiert man alles aber mit der messagebox hat das irgendwie nicht funktioniert, deswegen haben wir das nochmal importiert
#hat wahrscheinlich was mit dem Aufruf der Funktion zu tun. Das Programm ruft die messagebox ja mit messageox.showinfo auf. Wahrscheinlich reicht showinfo aus...?
from tkinter import *
from tkinter import messagebox
# Wenn man das mit dem * oder halt mit from time import time macht kann man die time.sleep() Funktion mit sleep() aufrufen. Ist wahrscheinlich das Gleiche wie mit der MessageBox
import time
import random
import threading



#Variabeln
AnzahlDerFragen = 0




#Antworten
Antwort1 = "Diese Antwort ist richtig. Gut gemacht!"
Antwort2 = "Diese Antwort war leider falsch. Schade!"

#Fragen
Fragen = ["Wenn es Steinzeit Menschen zu eng wird suchen sie sich eine...?","Womit verbringen Katzen einen Gutteil des Tages?", "Nicht nur Schauspieler waren zuletzt froh, \n konnten sie auf der Suche nach Klopapier …?","Jemanden, der aus der US-Glückspielmetropole zurückkommt, \n könnte man fragen:“..“?","Muss ein kleiner Equus aufpassen, \n dass er nicht auf einen kleinen Parus tritt, \n befindet sich offenbar …?", "Wer spielte bei der Fußballweltmeisterschaft 2006 mit?", "Wofür wird- je nach Hersteller- ein Mindestabstand \n von drei bis zehn Zentimetern zueinander empfohlen?", "Was darf laut EU-Verordnung seit 2018 bei Schwangeren und Stillenden \n nur noch in Ausnahmefällen verwendet werden?", " „Ein Zehntel der Geschwindigkeit mal drei“ \n gilt für Autofahrer als Faustformel zur Berechnung des …?", " Welche beiden Hauptstädte liegen ziemlich genau auf dem gleichen Breitengrad ?", "Welche Eselsbrücke dient dazu, \n sich die häufigsten Elemente in der Erdkruste zu merken?", "Was tritt fast ausschließlich tagsüber auf?", "Wo überprüft man bei Haustieren wie Hund oder Katze am besten den Puls","Worin ist häufig die sogenannte  \n Dortmunder- Mischung zu finden?","Wessen Witwe heiratete \n der dänische Diplomat Georg Nikolaus Nissen 1809?", "Sie haben gewonnen"]



#Antwortmöglichkeiten
Antwortmöglichkeiten =  ["Eine Nebenhöle", "ein Mittlohr ","eine Speiseröhre", "einen Lungenflügel ","putzen", "spülen",  "kochen", "bügeln ", "eine Rolle ergattern ", "einen Film drehen ", "eine Tournee absolvieren", "einen Engament bekommen",  "Wie war Las Vegas?", "Lof mie Tender", "Dscheel Haus Rock?", "Olwäs on mei Mind?", "eine Meise unterm Pony", "Eine Mücke beim Elefanten", "ein Hecht im Karpfenteich", "ein Wolf im Schafspelz", "Trinidad& Tobago", "Simon& Garfunkel", "Kastor& Pollux", "Siegfried & Roy", "Teelichter", " Grassamen", "Fahrradkettenblättern", "Teenies in der Pubertät", "Amalgam für Zahnfüllungen", "Einlagen bei Plattfüßen", "Pflaster auf Schürfwunden", "Kontaktlinsen als Sehhilfe", "Reaktionsweg", "Spritverbrauch", "zu erwartenden Bußgeldes", "Sicherheitsabstands", "Ankara & Peking", "Canberra & Kuala Lumpur", "Paris & Mexiko- Stadt", "Nairobi & Buenos Aires", "Oh, sie altes Ferkel!", "Ach,die dumme Kuh!", "Pfui, du krummer Hund!", "Na, ihr schrägen Vögel!", "Hagel", "Nieselregen", "Bodennebel", "Schäfchenwolken", "Oberschenkel- Innenseite", "Ohrenspitze", "Kehle", "Nabelgegend", "Kühlschränke", "Schwimmbecken", "Bierfässer", "Nasentropfen", "Mozart", "Napoleon", "Goethe", "Bismarck", "Sie haben gewonnen","Sie haben gewonnen","Sie haben gewonnen","Sie haben gewonnen"]#r"Sie haben gewonnen","Sie haben gewonnen","Sie haben gewonnen","Sie haben gewonnen"]

#Gewinne
Gewinne = [" 0€ ","100€", "200€", "300€", "500", "1.000€",  "2.000€", "4.000€", "8.000€", "16.000€", "32.000€", "64.000", "€ 125.000€", "500.000€", "1Millionen€","Sie haben gewonnen"] 


#braucht man eigentlich nicht war ein falscher Denkansatz
#Wir dachten man muss das Programm 15-mal wiederholen, weil es 15 Fragen gibt aber das Funktioniert auch mit (1)
for Nr in range (1)  :
    

    def button1Click():

        #Timer wird nach jedem richtigem Knopf Druck wieder auf 0 gesetzt 
        global my_timer
        my_timer = 0

       
        
        global Anzeige
        Anzeige.config(text = Antwort1)
        Button1.configure(background = 'green')
        messagebox.showinfo ("Antwort", "Antwort ist richtig")
        Button1.configure(background = 'white')

        #Variabeln die Zählt, wie oft der Button gedrückt wird. Ist für viele Funktionen wichtig
        global AnzahlDerFragen
        AnzahlDerFragen = AnzahlDerFragen+1
        
        
        
        #Buttons configurieren
        Anzeige.config(text = Fragen[AnzahlDerFragen])
        Button1.config(text = Antwortmöglichkeiten[0+(AnzahlDerFragen*4)])
        Button2.config(text = Antwortmöglichkeiten[1+(AnzahlDerFragen*4)])
        Button3.config(text = Antwortmöglichkeiten[2+(AnzahlDerFragen*4)])
        Button4.config(text = Antwortmöglichkeiten[3+(AnzahlDerFragen*4)])
        Button5.config(text = "Den Gewinn auszahlen:\n " + Gewinne[AnzahlDerFragen])

    
        #Abfrage für die MessageBox wenn man gewonnen hat
        if AnzahlDerFragen == 15 :
            messagebox.showinfo ("Hurra!", "Glückwunsch! Sie sind virtueller Millionär!")
            Fenster.destroy()


        #Button1 tauscht zufällig mit einem anderen Button den Platz
        
        Zufall=random.randint(2,4)
        print(Zufall)

        if Zufall == 1  :
            Button1.grid (row = 1, column = 100, padx = 200, pady = 20)
            Button2.grid (row = 1, column = 102, padx = 200, pady = 10)
            Button3.grid (row = 2, column = 100, padx = 200, pady = 20)
            Button4.grid (row = 2, column = 102, padx = 200, pady = 20)

            
        if Zufall == 2  :
            Button1.grid (row = 1, column = 102, padx = 200, pady = 10)
            Button2.grid (row = 1, column = 100, padx = 200, pady = 20)
            Button3.grid (row = 2, column = 100, padx = 200, pady = 20)
            Button4.grid (row = 2, column = 102, padx = 200, pady = 20)
        if Zufall == 3  :
            Button1.grid (row = 2, column = 100, padx = 200, pady = 20)
            Button2.grid (row = 1, column = 102, padx = 200, pady = 10)
            Button3.grid (row = 1, column = 100, padx = 200, pady = 20)
            Button4.grid (row = 2, column = 102, padx = 200, pady = 20)
        if Zufall == 4  :
            Button1.grid (row = 2, column = 102, padx = 200, pady = 20)
            Button2.grid (row = 1, column = 102, padx = 200, pady = 10)
            Button3.grid (row = 2, column = 100, padx = 200, pady = 20)
            Button4.grid (row = 1, column = 100, padx = 200, pady = 20)

              


 
                
    def button2Click():
        
        Anzeige.config(text = Antwort2)
        Button2.configure(background="red")
        Button3.configure(background="red")
        Button4.configure(background="red")
        Button1.config(background="green")
        messagebox.showinfo ("Antwort", Aufmunterungstext)
        Fenster.destroy()


   
    def button3Click():
        Anzeige.config(text = Antwort2)
        Button2.configure(background="red")
        Button3.configure(background="red")
        Button4.configure(background="red")
        Button1.config(background="green")
        messagebox.showinfo ("Antwort", Aufmunterungstext)
        Fenster.destroy()
     

    def button4Click():
        Anzeige.config(text = Antwort2)
        Button4.configure(background="red")
        Button2.configure(background="red")
        Button3.configure(background="red")
        Button1.config(background="green")
        messagebox.showinfo ("Antwort", Aufmunterungstext)
        Fenster.destroy()

    # Funktion für den "Ich nehme das Geld und höre auf button"( In diesem Programm auch Geldzähler Button genannt)
    def button5Click():
        
        MsgBox = messagebox.askquestion ("Ich nehme das Geld und höre auf","Bist du sicher,dass du nicht mehr weiter spielen willst?",icon = "warning")
        if MsgBox == "yes":
            
             Fenster.destroy()
        else:
             messagebox.showinfo("Zurück","Du wirst nun zurück zum Proogramm geleitet")


   # Funktion für den Timer 
    def countdown()  :
        global my_timer
        my_timer=0
        for Nr in range (100):
            
            my_timer = my_timer+1
            time.sleep(1)
            global Button6
            Button6.config(text="Verstrichende Zeit: \n" + str(my_timer))

            #Abfrage die das Fenster zerstört sobald der Timer zuende ist
            if my_timer == anzahlSekunden:
              global Fenster
              messagebox.showinfo("Keine Zeit","Du hast keine Zeit mehr. Das Programm wird geschlossen!")
              Fenster.destroy()

    #Funktion für den Schieberregler( passende Variabeln werden vergeben damit der sich den gewünschten Timer merkt   
    def scaleValue(self):
        global anzahlSekunden
        anzahlSekunden = Schieber.get()

    #Funktion, die nur gebraucht wird um den Timer zu konfigurieren wird gepasst wenn der Timer gar nicht an ist
    def button7Click():
        if timeron == True:
            
            
            global anzahlSekunden
            countdown_thread.start()
            global Fenster2
            Fenster2.destroy()
        if timeron == False:
            pass
        


#Hauptprogramm

#Den Timer muss man auf einem anderen Thread laufen lassen, weil das Hauptprogramm sonst gestört wird
countdown_thread = threading.Thread(target = countdown)

#Hauptfenster wo sich das Quiz abspielt wird definiert
global Fenster                                   
Fenster = Tk()
Anzeige = Label(Fenster, text = Fragen[AnzahlDerFragen])
Fenster.geometry ("1920x1080")
Fenster.configure (bg = 'blue')
Anzeige.grid (row = 0, column = 101,padx = 120, pady = 20)
#Abfrage die fragt ob man mit oder ohne Timer spielen möchte dann wird die Variabel timeron entweder auf True oder auf False gesetzt
MsgBox = messagebox.askquestion ("Timer","Willst du mit Timer spielen?",icon = "question")
if MsgBox == "yes":
    timeron= True
    global Fenster2
    Fenster2 = Tk()
    Anzeige2 = Label(Fenster2, text = "Stellen Sie ihr Zeitlimit ein")
    
    Fenster2.geometry ("600x500")
    Schieber = Scale(Fenster2, orient="horizontal")
    Schieber.config(length=430, showvalue=1, command=scaleValue)
if MsgBox == "no":
    
    timeron= False

        
#Variabel die in dem Geldzähler Button genutzt wird. Gibt den Gewinn aus der an der AnzahlDerFragen Stelle in der Liste Gewinne steht
Geldgewinne=Gewinne[AnzahlDerFragen]

#Abfrage die den Aufmunterungstext definiert. Wenn man nach 14 Fragen verliert kommt ein anderer Text als wenn man nach 5 Fragen verliert
if AnzahlDerFragen <= 5 :
    Aufmunterungstext= "Schade, das geht aber auch besser!"
if AnzahlDerFragen <=14 :
    Aufmunterungstext= "Schade, ganz gut, aber das geht noch besser!"
if Geldgewinne== 500.000  :
    messagebox.showinfo("Glückwunsch", "Sie sind virtueller Millionär")


#Buttons
Button1 = Button(Fenster, text = Antwortmöglichkeiten [0],  
command = button1Click)
Button2 = Button(Fenster, text = Antwortmöglichkeiten [1],
command = button2Click)
Button3 = Button(Fenster, text = Antwortmöglichkeiten [2],
command = button3Click)
Button4 = Button(Fenster, text = Antwortmöglichkeiten [3],
command = button4Click)

#Wenn man den Timer konfigurieren muss wird ein weiterer Button erstellt
if timeron == True:
    Button7 = Button(Fenster2, text="Fertig",
    command = button7Click)
    



#GeldzählerButton

Button5= Button(Fenster, text = Gewinne[0],
command = button5Click) 

#Button wo der Timer abgebildet wird. Ist als default leer. 
global Button6
Button6= Button(Fenster, text="Timer ist in diesem Spiel nicht vorhanden")


#Erste Buttons Anordnung

Button1.grid (row = 1, column = 100, padx = 200, pady = 20)
Button2.grid (row = 1, column = 102, padx = 200, pady = 10)
Button3.grid (row = 2, column = 100, padx = 200, pady = 20)
Button4.grid (row = 2, column = 102, padx = 200, pady = 20)
Button5.grid (row = 2, column = 103, padx = 30, pady = 20)
Button6.grid (row = 1, column = 103, padx = 30, pady = 20)

if timeron == True:
    Schieber.grid(row = 4, column = 13, padx = 20, pady = 20)
    Button7.grid (row = 5, column = 13, padx = 20, pady = 20)
    Anzeige2.grid (row = 0, column = 11)

#Braucht man wenn man mit tkinter arbeitet damit das Fenster geupdated wird.
Fenster.mainloop()











