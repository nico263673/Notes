def urknall():
    print("wilkommen in der python note app")

def start():
    print("")
    print("moechtest du notes")
    print("1. oefnen")
    print("2. erweitern")
    print("3. alles loeschen")
    print("oder 4. die app verlassen")


def lesen():
    with open("note_py.txt","r") as datei:
        inhalt = datei.read()

    return inhalt

def erweitern():
    with open("note_py.txt","a") as datei:
        while True:
            try:
                neuer_text = input("was möchtest du hinzufügen ")

                datei.write(neuer_text + "\n")

                while True:
                    try:
                        print("")
                        print("willst du mehr text hinzufügen? ")
                        weiter = input("J/N ").lower()

                        if weiter == "j":
                            break
                        elif weiter == "n":
                            start()
                            return 0

                    except ValueError:
                        print("du musst j oder n eingeben")
                        continue

            except ValueError:
                print("du musst text eingeben")

def notizen_delete():
    with open("note_py.txt","w") as datei:
        inhalt = datei.write("")

def wirklich_notes_del():
    print("")
    print("willst du deine notizen wirklich loeschen? ")
    while True:
        try:
            wirklich_schliessen = input("Ja oder Nein ").lower()
            if wirklich_schliessen == "ja":
                notizen_delete()
                break
            elif wirklich_schliessen == "nein":
                start()
                break
            else:
                print("du musst ja oder nein schreiben")
        except ValueError:
            print("du darfst nur mit text antworten")


def main():
    urknall()
    start()

    while True:
        try:
            entscheidung = int(input("schriebe bitte die zahl für die du dich entscheidest "))

            if entscheidung == 1:
                text = lesen()
                print(text)
            elif entscheidung == 2:
                erweitern()
            elif entscheidung == 3:
                wirklich_notes_del()
            elif entscheidung == 4:
                print("bye")
                break
            else:
                print("du darfst nur eine zahl von 1 bis 4 schreiben")
        except ValueError:
            print("du musst eine zahl schreiben")

if __name__ == '__main__':
    main()