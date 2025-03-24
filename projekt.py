import json
import pandas as pd
import random

with open("baza.json",encoding="UTF-8") as baza:
    baza_slownik = json.load(baza)

dane = pd.read_excel("dane.xlsx",sheet_name="Arkusz1")

lista_zadan = list(range(1,9))
grupy = []
uczniownie = []
zadania = []
for i in range(0,89):
    uczniownie.append(dane.iloc[i,9])
    grupy.append(random.randint(1,2))
    zadania.append(random.sample(lista_zadan,4))

lista = dict(zip(uczniownie, zip(grupy,zadania)))
print(lista)

ile = input("Ile Chcesz Wygenerować testów? = ")

for i,(k,w) in enumerate(lista.items()):
    grupa = int(w[0])-1
    zad1 = w[1][0]
    zad2 = w[1][1]
    zad3 = w[1][2]
    zad4 = w[1][3]
    baza_slownik["cells"][2]["source"] = str(dane.iloc[grupa,zad1]).split("\n")
    baza_slownik["cells"][5]["source"] = str(dane.iloc[grupa,zad2]).split("\n")
    baza_slownik["cells"][8]["source"] = str(dane.iloc[grupa,zad3]).split("\n")
    baza_slownik["cells"][11]["source"] = str(dane.iloc[grupa,zad4]).split("\n")
    with open(f"{k}.ipynb","w") as test:
        json.dump(baza_slownik,test,ensure_ascii="false",indent=4)
    if i == (int(ile)-1):
        break

#zrobnie kolosow nie z listy
#baza.json ma sie robic z excela
#optymalizcja kodu
#pasek ładowania
#opcja usuwania pozostalosci
#zrobic z tego funkcje
#zrobic to uniwersalne
#zeby lista nie byla excel tylko w parametrach funkcji
