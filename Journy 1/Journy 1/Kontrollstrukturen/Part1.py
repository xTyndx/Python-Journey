# n = 13

# if n < 42:
#     print("n ist kleiner als 42")
# else: 
#     print("n ist größer als 42")


# word = "Hallo"
# print(word == "Hallo") #gibt True aus, weil die Wörter gleich sind
# print(word != "Hallo") #gibt False aus, weil die Wörter gleich sind


# Booleans (and or not)

# age = 30

# if age >= 30 and age <= 40:
#     print("Du bist in deinen 30ern")

# age = 15

# if age < 30 or age > 40:
#     print("Du bist nicht in deinen 30ern")

# above_18 = age >= 30

# print(above_18) #gibt True aus, weil age >= 30 ist


# age = 25

# above_20 = age >= 20
# print(above_20) #gibt True aus, weil age >= 20 ist

# if above_20:
#     print("if-Abfrage wurde ausgeführt")

# print(True and True) #gibt True aus, weil beide Werte True sind
# print(False and False)
# print(True and False) #gibt False aus, weil einer der Werte False ist
# print(False and True) #gibt False aus, weil einer der Werte False ist
# print(True or True) #gibt True aus, weil einer der Werte True ist
# print(False or False) #gibt False aus, weil beide Werte False sind
# print(True or False) #gibt True aus, weil einer der Werte True ist
# print(False or True) #gibt True aus, weil einer der Werte True ist

# country = "US"
# age = 20

# if (country == "US" and age >= 21) or (country != "US" and age >= 18):
#     print("Du kannst Alkohol kaufen")


# students = ["Max", "John", "Tom", "Sam"]

# print("Monika" in students) #gibt False aus, weil Monika nicht in der Liste ist
# print("Max" in students) #gibt True aus, weil Max in der Liste ist

# if "Monika" in students:
#     print("Monika ist in der Liste")
# else:
#     print("Monika ist nicht in der Liste") #gibt Monika ist nicht in der Liste aus, weil Monika nicht in der Liste ist

# if "Max" in students:
#     print("Max ist in der Liste") #gibt Max ist in der Liste aus, weil Max in der Liste ist
# else:
#     print("Max ist nicht in der Liste")


# Geht auch bei Strings

# sentence = "Ich bin ein Satz mit vielen Wörtern"
# if "?" in sentence:
#     print("Der Satz enthält ein Fragezeichen")
# else:  
#     print("Der Satz enthält kein Fragezeichen")

# if "i" in sentence:
#     print("Der Satz enthält ein i") #gibt Der Satz enthält ein i aus, weil i in dem Satz ist
# else:
#     print("Der Satz enthält kein i")

# Not-Operator

# age = 25
# if not age >= 30:
#     print("ausgeführt")
# if age < 30:
#     print("ausgeführt")

# names = ["Max", "John", "Tom", "Sam"]
# if not "Monika" in names:
#     print("ausgeführt")
# if "Max" not in names:
#     print("ausgeführt")


# Elif

# Currency = "€"

# if Currency == "$":
#     print("US Dollar")
# elif Currency == "€":
#     print("Euro")
# elif Currency == "£":
#     print("Pfund")
# elif Currency == "¥":
#     print("Yen")
# elif Currency == "₹":
#     print("Rupie")