'Sting -> Ganze Zahl'

a = "5"
b = "6"
print(int(a) + int(b)) #gibt 56 aus, weil es als String interpretiert wird

'String -> Kommazahl'

a = "5.5"
b = "6.6"

print(float(a) + float(b)) #gibt 12.1 aus, weil es als Kommazahl interpretiert wird


'Zahl -> String'

age = 26
print("Ich bin " + str(age) + " Jahre alt") #gibt Ich bin 26 Jahre alt aus, weil es als String interpretiert wird


'Liste -> String'

studens = ["Max", "John", "Tom", "Sam"]
print(", ".join(studens))

studens_as_string = ", ".join(studens)
print("Die Studenten sind: " + studens_as_string) #gibt Die Studenten sind: Max, John, Tom, Sam aus


'String -> Liste'

i = "Max, John, Tom, Sam"
print(i.split(", ")) #gibt ['Max', 'John', 'Tom', 'Sam'] aus, weil es als Liste interpretiert wird


s = "ich bin ein Satz mit vielen Wörtern"
print(s.split(" ")) #gibt ['ich', 'bin', 'ein', 'Satz', 'mit', 'vielen', 'Wörtern'] aus, weil es als Liste interpretiert wird
print(len(s.split(" "))) #gibt 7 aus, weil es die Anzahl der Wörter zählt
