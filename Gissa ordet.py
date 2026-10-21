ordet = input("Spelare 1, skriv in ett ord: ").lower()
print('\n' * 20)
gissningar = []
felgissningar = 0
max_fel = 6

lifeline = [
r"""
 ♥ ♥ ♥ ♥ ♥ ♥
       O
      /|\ 
      / \ 
""",
r"""
 ♥ ♥ ♥ ♥ ♥
       O
      /|\ 
      / \ 
""",
r"""
 ♥ ♥ ♥ ♥
       O
      /|\ 
      / \ 
""",
r"""
 ♥ ♥ ♥
       O
      /|\ 
      / \ 
""",
r"""
 ♥ ♥
       O
      /|\ 
      / \ 
""",
r"""
 ♥
       O
      /|\ 
      / \ 
""",
r"""
       O
      /|\ 
      / \ 
"""
]

while felgissningar < max_fel:
    display = ""

    for bokstav in ordet:
        if bokstav in gissningar:
            display += bokstav + " "
        else:
            display += "_ "

    print(lifeline[felgissningar])
    print("Word:", display)
    print("Gissade bokstäver:", gissningar)

    if "_" not in display:
        print("Grattis! Du vann!")
        print("Ordet var:", ordet)
        break

    gissning = input("Gissa en bokstav: ").lower()

    if len(gissning) != 1 or not gissning.isalpha():
        print("Skriv bara en bokstav!")
        continue

    if gissning in gissningar:
        print("Du har redan gissat på den bokstaven!")
        continue

    gissningar.append(gissning)

    if gissning in ordet:
        print("Rätt gissat!")
    else:
        felgissningar += 1
        print("Fel gissat!")

else:
    print(lifeline[max_fel])
    print("Game over!")
    print("Ordet var:", ordet)