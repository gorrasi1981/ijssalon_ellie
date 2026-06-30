import csv
from helper import *
from prestatie import presenteer

inkomsten = {
    "Aardbeien-ijs-totaal":1000,
    "Vanille-ijs-totaal":2000,
    "Chocolade-ijs-totaal": 1500,
    "Waterijsjes-totaal": 750
}

with open('boekhouding.csv','w',newline='') as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile,delimiter=';')
        writer.writerow([key,value])

totaal_inkomsten = som(inkomsten)
presenteer(inkomsten, totaal_inkomsten)