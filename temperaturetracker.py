"""
Rasmus Hén
Windows 10
"""

december = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def decemberInput(): #Takes the user's input (in float) concerning temerature of every given day of december and puts it in the list "december"
    count = 0
    while count < 31:
        for index in range(len(december)):
            try:
                december[count] = float(input("Hur många grader var det " + str(count + 1) + " December? "))
                count = count + 1
                if count > 30:
                    break
            except ValueError:
                print("Fel typ av input.")
            
def actionMax(): #Collects the maximum value among the elements of the list "december"
    print("Den högsta temperaturen i December var", max(december), "grader.")

def actionMin(): #Collects the minimum value among the elements of the list "december"
    print("Den lägsta temperaturen i December var", min(december), "grader.")

def actionMid(): #Collects the avarage value for all the elements of the list "december"
    sumDecember = sum(december)
    midValue = sumDecember / 31
    midValue = str(round(midValue, 2))
    print("Medeltemperaturen under December var", midValue, "grader.")

def actionDay(): #Collects a given value among the elements of the list "december"
    while True:
        try:
            day = int(input("Vilken dag gäller det? "))
            if day > 0 and day < 32:
                day = day - 1
                print("Den dagen var det", december[day], "grader.")
                break
            else:
                print("Ange en siffra mellan 1-31.")
        except ValueError:
            print("Ange en siffra mellan 1-31.")

def mainMenu(): #Main menu that calls the different functions depending on the user's input  
    while True:
        action = input("\n\nMånadens högsta temperatur, skriv MAX\nMånadens lägsta temperatur, skriv MIN\nMånadens medeltemperatur, skriv MEDEL\nVälj dag genom att skriva DAG\nAvsluta med EXIT\n\nAnge ditt val: ").lower()
        if action == "max":
            actionMax()
        elif action == "min":
            actionMin()
        elif action == "medel":
            actionMid()
        elif action == "dag":
            actionDay()
        elif action == "exit":
            print("Hejdå!")
            break
        else:
            print("Det är inte ett val, försök igen.")

decemberInput()
mainMenu()
