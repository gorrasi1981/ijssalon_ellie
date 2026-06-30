def presenteer(dictionary,totaal):
    for key, value in dictionary.items():
        print(f"{key}:{value} euro")
    print("================================")          
    print(f"Totaal: {totaal} euro")