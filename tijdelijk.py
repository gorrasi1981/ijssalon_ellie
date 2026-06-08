prijzen = {"aardbei":3, "vanille":4,"chocolade":5}
aanbieding = prijzen ["aardbei"] * 0.8
reclame_tekst = (f"Vandaag in de aanbieding: vanilleijs, 1 liter - slechts € {aanbieding}")
#De index van de eerste 0 na de komma is 63, dus we knippen de tekst af bij index 63
reclame_tekst2 = reclame_tekst[:63]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split(" ")
for el in reclame_tekst4:
    if len(el) >= 5:
        print(el.upper())
else:
        print(el.lower())