
oddelovac = "-" * 40
prihlasovaci_udaje = {"bob" : "123", "ann" : "pass123", "mike": "password123", "liz" : "pass123"}

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

print(oddelovac)
print("Vítej!")
print(oddelovac)

jmeno = input("Zadej přihlašovací jméno: ")
heslo = input("Zadej heslo: ")


if jmeno in prihlasovaci_udaje.keys() and heslo == prihlasovaci_udaje[jmeno]:
    print("Jsi přihlášen.")
else:
    print("Nesprávné uživatelské jméno nebo heslo.")
    exit()

print(oddelovac)
cislo_textu = int(input("Zadej číslo vybraného textu (1-3): "))

vybrany_text = TEXTS[cislo_textu-1]
rozdeleny_text = vybrany_text.split()

pocet_slov = 0
zacinajici_velkymi = 0
velkymi_pismeny = 0
malymi_pismeny = 0
pocet_cisel = 0
soucet_cisel = 0
delky_slov = []

for slovo in rozdeleny_text:
    pocet_slov += 1
    delky_slov.append(len(slovo))
    if slovo[0].isupper():
       zacinajici_velkymi += 1
    if slovo.isupper():
       velkymi_pismeny += 1
    if slovo.islower():
       malymi_pismeny += 1
    if slovo.isnumeric():
       pocet_cisel += 1
       soucet_cisel += int(slovo)

print(oddelovac)
print(f"Počet slov v textu: {pocet_slov}.")
print(f"Počet slov začínajících velkým písmenem: {zacinajici_velkymi}.")
print(f"Počet slov psaných velkými písmeny: {velkymi_pismeny}.")
print(f"Počet slov psaných malými písmeny {malymi_pismeny}.")
print(f"Počet čísel v textu: {pocet_cisel}.")
print(f"Součet všech čísel v textu: {soucet_cisel}.")

print(oddelovac)
print("GRAF DÉLEK SLOV V TEXTU")
print(oddelovac)

for delka in sorted(set(delky_slov)):
    pocet_delky = delky_slov.count(delka)
    print(delka, "*" * pocet_delky, pocet_delky)
