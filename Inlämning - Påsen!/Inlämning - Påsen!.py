påse = []

while True:
    print("\nMeny:")
    print("[V] Visa innehållet i påsen")
    print("[S] Spara i påsen")
    print("[F] Leta (finns) i påsen")
    print("[Q] Avsluta programmet")
    
    val = input("Välj ett alternativ: ").upper()
    
    if val == "V":
        if påse:
            print("Påsen innehåller:", ", ".join(påse))
        else:
            print("Påsen är tom.")
    
    elif val == "S":
        sak = input("Vad vill du lägga i påsen? ")
        påse.append(sak)
        print(f"'{sak}' har lagts i påsen.")
    
    elif val == "F":
        sak = input("Vad vill du leta efter i påsen? ")
        if sak in påse:
            print(f"'{sak}' finns i påsen.")
        else:
            print(f"'{sak}' finns inte i påsen.")
    
    elif val == "Q":
        print("Programmet avslutas. Hej då!")
        break
    
    else:
        print("Ogiltigt val, försök igen.")