# Aufgabe 1:

# contienents = ["Asien", "Europa", "Afrika", "Nordamerika", "Südamerika", "Australien", "Antarktis"]

# for i in contienents:
#     print(i) # gibt die Kontinente aus

# for i in contienents:
#     if i == "Antarktis":
#         continue
#     print(i) # gibt die Kontinente aus, überspringt aber Antarktis


# stuff = ["Asien", "Europa", "Löffel", "Gabel", "Auto", "Bus"]

# for element in stuff:
#     if element in contienents:
#         print(element) # gibt die Kontinente aus, überspringt aber die anderen Elemente


# count = 0
# for i in stuff:
#     if i in contienents:
#         count += 1 # zählt die Kontinente
# print(count) # gibt die Anzahl der Kontinente aus


# Aufgabe 2:

# price = 50

# if price <= 20:
#     price = price * 0.8 # gibt 20% Rabatt
# elif price <= 50:
#     price = price * 0.6 # gibt 40% Rabatt
# else:
#     price = price * 0.4

# print(price) # gibt den Preis aus, nachdem der Rabatt abgezogen wurde

# prices = [2, 50, 70, 30]
# new_prices = []

# for price in prices:
#     if price <= 20:
#         price = price * 0.8 # gibt 20% Rabatt
#     elif price <= 50:
#         price = price * 0.6 # gibt 40% Rabatt
#     else:
#         price = price * 0.4
#     new_prices.append(price) # fügt den neuen Preis zur Liste hinzu
# print(new_prices) # gibt die neuen Preise aus, nachdem der Rabatt abgezogen wurde


# Aufgabe 3:

chaos =["old price: 40", "new price: 21", "old price: 29", "old price: 50", "new price: 101"]
order = []

for i in chaos:

    price = int((i.split(": ")[1])) # trennt den String und konvertiert den Preis in einen Integer
    if "old" in i:
        if price <= 20:
            price *= 0.8
        elif price <= 50:
            price *= 0.6
        else:
            price *= 0.4
    order.append(price) # fügt den neuen Preis zur Liste hinzu
print(order) # gibt die neuen Preise aus, nachdem der Rabatt abgezogen wurde