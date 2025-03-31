import json
import pandas as pd
import random
import uuid
import os

def generatorbazy(ilezadan=4):
    komorki = []
    dane = {'nbformat': 4,
             'nbformat_minor': 0,
               'metadata': {'colab': {'provenance': []},
                'kernelspec': {'name': 'python3',
                'display_name': 'Python 3'},
                'language_info': {'name': 'python'}},
                'cells':komorki}
    for i in range(1,ilezadan+1):
        komorki.append({"cell_type":"markdown","source":[f"Zadanie {i}"],"metadata":{"id":str(uuid.uuid4())}})
        komorki.append({"cell_type":"markdown","source":["------"],"metadata":{"id":str(uuid.uuid4())}})
        komorki.append({"cell_type":"code","source":[],"metadata":{"id":str(uuid.uuid4())},"execution_count":0,"outputs":[]})
    with open("baza.json","w",encoding="UTF-8") as bazav2:
        json.dump(dane,bazav2,ensure_ascii="false",indent=4)
    return f"Baza Utworzona z {ilezadan} zadaniami."

def genkolos(ile,zlisty = False,kolosilezadan=4):
    generatorbazy(kolosilezadan)
    with open("baza.json",encoding="UTF-8") as baza:
        baza_slownik = json.load(baza)

    dane = pd.read_excel("dane.xlsx",sheet_name="Arkusz1")

    lista_zadan = list(range(1,9))
    grupy = []
    if zlisty == True:
        with open("lista.txt",encoding="UTF-8") as plikuczniowie:
            uczniownie = plikuczniowie.readlines()
        uczniownie = [v.rstrip("\n") for v in uczniownie]
    else:
        uczniownie = range(ile)
    
    zadania = []
    for i in range(0,len(uczniownie)):
        grupy.append(random.randint(1,2))
        zadania.append(random.sample(lista_zadan,kolosilezadan))

    lista = dict(zip(uczniownie, zip(grupy,zadania)))
    print(lista)

    for i,(k,w) in enumerate(lista.items()):
        grupa = int(w[0])-1
        iterator = 0
        for zad in range(1,3*kolosilezadan+1,3):
            baza_slownik["cells"][zad]["source"] = str(dane.iloc[grupa,w[1][iterator]]).split("\n")
            iterator += 1
        with open(f"testy/{k}.ipynb","w") as test:
            json.dump(baza_slownik,test,ensure_ascii="false",indent=4)
        if i == (int(ile)-1):
            break
    os.remove("baza.json")
    return f"Pomyślnie wygenerowano {ile} testów."

print(genkolos(2,False,5)) #ile kolosow #czy ma sie generowac z listy #ile zadan ma byc na kolosie