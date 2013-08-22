import easygui
easygui.msgbox("Hallo, und willkommen in meiner Welt!", "Welt", "Weiter",image="wesnoth-icon.png")
while True:
    antwort=easygui.buttonbox("<Schlachter> Was willst du?", "Wunsch", ("Schaf","Kuh","Schwein","Ente","Beenden"),image="bandit.png")
    #Schaf------------------------
    if antwort =="Schaf":
        easygui.msgbox("Määähhhh!")
        antwort2=easygui.buttonbox("<Schlachter> Was willst du mit dem Schaf machen?","Schaf", ("Nix machen","Schlachten","Zurück zum Hauptmenü"),image="sword.png")
        if antwort2 =="Nix machen":
            easygui.msgbox("<Schlachter> Das ist schade")
        elif antwort2 =="Schlachten":
            easygui.msgbox("<Schlachter> Ein Schaf schlachte ich gerne für dich!")
            wolle=easygui.buttonbox("<Schlachter> Möchtest du die Wolle haben?","Wolle",("Ja bitte","Nein danke"))
        if wolle =="Ja bitte":
            bestechen=easygui.buttonbox("Möchtest du den Schlachter bestechen um die Wolle gratis zu bekommen!","Bestechen",("Ja","Nein","Das ist eine blöde Frage!"))
        if bestechen =="Ja":
                  easygui.msgbox("Du hast den Schlachter bestochen und hast statt um 3 Silberstücke die Wolle und das Schaf um 4 Silberstücke bekommen!")
                  break
        elif bestechen =="Nein":
                  easygui.msgbox("<Schlachter> Du bekommst das Schaf und die Wolle um 3 Silberstücke bekommen!")
                  break
        elif bestechen =="Das ist eine blöde Frage!":
                  easygui.msgbox("Das stimmt!")
                  break
        elif wolle =="Nein danke":
                  easygui.msgbox("<Schlachter> Ok, hier hast du dein Schaf")
                  break
                                                                                   
                                                          
        elif antwort =="Zurück zum Hauptmenü":
            break
    #Kuh--------------------------
    elif antwort =="Kuh":
        easygui.msgbox("Muuuhhh!")
        antwort3=easygui.buttonbox("<Schlachter> Ah eine Kuh! Was willst du mit ihr machen?","Kuh", ("Nix machen","Schlachten","Zurück zum Hauptmenü"),image="sword.png")
        if antwort3 =="Nix machen":
            easygui.msgbox("Mano!")
        elif antwort3 =="Schlachten":
              antwortkuh=easygui.buttonbox("<Schlachter> Willst du das Leder von der Kuh haben?(Das kostet extra)","Leder",("Ja bitte","Nein danke"))
              if antwortkuh =="Ja bitte":
                       easygui.msgbox("<Schlachter> Ok das sind dann 5 Silberstücke!")
                       antwortweglaufen=easygui.buttonbox("Willst du weglaufen oder bezahlen?","Weglaufen",("Weglaufen","Bezahlen"))
                       if antwortweglaufen =="Weglaufen":
                             easygui.msgbox("Du läufst weg!")
                             break
                       elif antwortweglaufen =="Bezahlen":
                             easygui.msgbox("Du bezahlst!")
                             break
              elif antwortkuh =="Nein danke":
                       easygui.msgbox("<Schlachter> Das wären dann 3 Silberstücke!")
                       antwortweglaufen1=easygui.buttonbox("Willst du weglaufen oder bezahlen?","Weglaufen",("Ja","Nein"))
                       if antwortweglaufen1 =="Ja":
                             easygui.msgbox("Du schnapst dir die Kuh und das Leder und läufst weg!")
                             break
                       elif antwortweglaufen1 =="Nein":
                             easygui.msgbox("Du bezahlst und gehst jetzt!")
                             break
                                                           
        elif antwort =="Zurück zum Hauptmenü":
            break
    #Schwein----------------------
    elif antwort =="Schwein":
        easygui.msgbox("Oinkoink!")
        antwort4=easygui.buttonbox("<Schlachter> Was willst du mit dem Schwein machen?","Schwein", ("Nix machen","Schlachten","Zurück zum Hauptmenü"),image="sword.png")
        if antwort4 =="Nix machen":
            easygui.msgbox("Schade")        
        elif antwort4 =="Schlachten":
              sk=easygui.buttonbox("<Schlachter> Ok ich schlachte dir ein Schwein möchtest du noch zwei weiter Schweine haben heute ist sonderangebot 3 Schweine zum Preis von 2 ein halb!","Schwein Kauf",("Ja bitte geben sie mir 3 Schweine","Nein danke ich nehme nur 1"))
              if sk =="Ja bitte geben sie mir 3 Schweine":
                       easygui.msgbox("<Schlachter> Ok warte hier!")
                       easygui.msgbox("2 Stunden später")
                       easygui.msgbox("<Schlachter> Hier sind deine Schweine das macht bitte 7 Silberstücke.")
                       sd=easygui.buttonbox("Möchtest du mit den Schweinen abhauen oder bezahlen?","Schweine Diebstahl",("Abhauen","Bezahlen"))
                       if sd =="Abhauen":
                            easygui.msgbox("Du haust mit deinen Schweinen ab!")
                            break
                       elif sd =="Bezahlen":
                            easygui.msgbox("Du bezahlst und gehst mit deinen Schweinen nach Hause")
                            break
              elif sk =="Nein danke ich nehme nur 1":
                            easygui.msgbox("<Schlachter> Ok warte hier!")
                            easygui.msgbox("1 Stunde später")
                            easygui.msgbox("<Schlachter> Hier ist dein Schwein das macht bitte 4 Silberstücke.")
                            ssd=easygui.buttonbox("Möchtest du mit deinem Schwein abbhauen oder bezahlen?","Schwein Diebstahl",("Abhauen","Bezahlen"))
                            if ssd =="Abhauen":
                                easygui.msgbox("Du haust mit deinem Schwein ab!")
                                break
                            elif ssd =="Bezahlen":
                                easygui.msgbox("Du bezahlst den Schlachter und gehst mit deinem Schwein nach hause!")
                                break
        elif antwort =="Zurück zum Hauptmenü":
            break
    #Ente-------------------------
    elif antwort =="Ente":
        easygui.msgbox("Quakquak!")
        antwort5=easygui.buttonbox("Was willst du mit dem Ente machen?","Ente", ("Nix machen","Schlachten","Zurück zum Hauptmenü"),image="sword.png")
        if antwort5 =="Nix machen":
            easygui.msgbox("Das ist ok")     
        elif antwort5 =="Schlachten":
                easygui.msgbox("<Computer> Na gut!")
        elif antwort =="Zurück zum Hauptmenü":
            break
    #Beenden----------------------
    elif antwort =="Beenden":
        easygui.msgbox(("Ok bis bald!"), image="boots_elven.png")
        easygui.msgbox("Der Schuh bedeuten du läufst weg")
        break
