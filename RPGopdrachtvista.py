from random import randrange
critter_names = ["JOHN CENA", "Domme mongool", "Iphone gebruiker", "Macbook gebruiker", "Fles Ice", "Erik Steens", "Raymond Backus", "Bak koffie", "Jeroen van Alphen", "Max Stegmann", "Cara Kerckhoffs", "Bubbort flumberdink", "Zilan"]
character = {"name": "VISTA SLAYER", "armour_naam": "Platen", "armor_sterkte": 1, "weapon_naam": "Franse stokbrood", "weapon_sterkte" : 10, "hp": 100}

size = input("Hoe groot moet de map worden waarin gespeelt wordt? (tussen de 10 / 20 wordt aangeraden)")
Karakter = [0,0]
Wapen_Lijst = {}
Speelveld = [randrange(0, int(size)), randrange(0, int(size))]
new_level = True
player_in_range = False
level = 0
def Aanval(name):
    Wapen_Lijst[name][2] = Wapen_Lijst[name][2] - character["weapon_sterkte"]

def Verdedigen(name):
    character["hp"] = character["hp"] - (Wapen_Lijst[name][3]/character["armor_sterkte"])

def mapmeting_gen():
    for i in critter_names:
        if randrange(1, 6) == 3:
            Wapen_Lijst[i] = [randrange(0, int(size)), randrange(0, int(size)), randrange(1, 100), randrange(1, 25)]




def player_input():
    move = input("Het is jou beurt, Beweeg je poppetje et WSAD, Je Opject is @. Zorg ervoor dat je de D bereikt voordat de M je pakt! ")
    if move == "w" and Karakter[0] > 0:
        Karakter[0] -= 1
    elif move == "a" and Karakter[1] > 0:
        Karakter[1] -= 1
    elif move == "s" and Karakter[0] < int(size) - 1:
        Karakter[0] += 1
    elif move == "d" and Karakter[1] < int(size) - 1:
        Karakter[1] += 1
    elif move == "e":
        if Speelveld[0] == Karakter[0] and Speelveld[1] == Karakter[1]:
            new_level = True
    elif move == "f":
        for i in Wapen_Lijst:
            if Wapen_Lijst[i][0] == Karakter[0] and Wapen_Lijst[i][1] == Karakter[1]:
                Aanval(i)
                Verdedigen(i)
            elif Wapen_Lijst[i][0] == Karakter[0] + 1 and Wapen_Lijst[i][1] == Karakter[1] + 1:
                Aanval(i)
            elif Wapen_Lijst[i][0] == Karakter[0] - 1 and Wapen_Lijst[i][1] == Karakter[1] + 1:
                Aanval(i)
            elif Wapen_Lijst[i][0] == Karakter[0] + 1 and Wapen_Lijst[i][1] == Karakter[1] - 1:
                Aanval(i)
            elif Wapen_Lijst[i][0] == Karakter[0] - 1 and Wapen_Lijst[i][1] == Karakter[1] - 1:
                Aanval(i)
            elif Wapen_Lijst[i][0] == Karakter[0] and Wapen_Lijst[i][1] == Karakter[1] + 1:
                Aanval(i)
            elif Wapen_Lijst[i][0] == Karakter[0] and Wapen_Lijst[i][1] == Karakter[1] - 1:
                Aanval(i)
            elif Wapen_Lijst[i][0] == Karakter[0] + 1 and Wapen_Lijst[i][1] == Karakter[1]:
                Aanval(i)
            elif Wapen_Lijst[i][0] == Karakter[0] - 1 and Wapen_Lijst[i][1] == Karakter[1]:
                Aanval(i)
    else:
        print("Deze commando wordt niet geacepteerd, Probeer iets anders of lees de beschrijving")
def map_gen():
    asc = '-'
    gen = [int(size)*[asc] for i in range(int(size))]
    gen[Karakter[0]][Karakter[1]] = '@'
    for i in Wapen_Lijst:
        if Wapen_Lijst[i][2] > 0:
            gen[Wapen_Lijst[i][0]][Wapen_Lijst[i][1]] = "M"
        else:
            gen[Wapen_Lijst[i][0]][Wapen_Lijst[i][1]] = "X"
    gen[Speelveld[0]][Speelveld[1]] = "D"
    print('\n'.join(' '.join(row) for row in gen))
def ai():
    for i in Wapen_Lijst:
        if Wapen_Lijst[i][2] > 0:
            if Wapen_Lijst[i][0] == Karakter[0] and Wapen_Lijst[i][1] == Karakter[1]:
                Aanval(i)
                Verdedigen(i)
                player_in_range = True
            elif Wapen_Lijst[i][0] == Karakter[0] + 1 and Wapen_Lijst[i][1] == Karakter[1] + 1:
                Verdedigen(i)
                player_in_range = True
            elif Wapen_Lijst[i][0] == Karakter[0] - 1 and Wapen_Lijst[i][1] == Karakter[1] + 1:
                Verdedigen(i)
                player_in_range = True
            elif Wapen_Lijst[i][0] == Karakter[0] + 1 and Wapen_Lijst[i][1] == Karakter[1] - 1:
                Verdedigen(i)
                player_in_range = True
            elif Wapen_Lijst[i][0] == Karakter[0] - 1 and Wapen_Lijst[i][1] == Karakter[1] - 1:
                Verdedigen(i)
                player_in_range = True
            elif Wapen_Lijst[i][0] == Karakter[0] and Wapen_Lijst[i][1] == Karakter[1] + 1:
                Verdedigen(i)
                player_in_range = True
            elif Wapen_Lijst[i][0] == Karakter[0] and Wapen_Lijst[i][1] == Karakter[1] - 1:
                Verdedigen(i)
                player_in_range = True
            elif Wapen_Lijst[i][0] == Karakter[0] + 1 and Wapen_Lijst[i][1] == Karakter[1]:
                Verdedigen(i)
                player_in_range = True
            elif Wapen_Lijst[i][0] == Karakter[0] - 1 and Wapen_Lijst[i][1] == Karakter[1]:
                Verdedigen(i)
                player_in_range = True
            else:
                player_in_range = False
            if player_in_range == False:
                c_move = randrange(1, 6)
                if c_move == 1 and Wapen_Lijst[i][0] < int(size) - 1:
                    Wapen_Lijst[i][0] += 1
                elif c_move == 2 and Wapen_Lijst[i][1] < int(size) - 1:
                    Wapen_Lijst[i][1] += 1
                elif c_move == 4 and Wapen_Lijst[i][0] > 0:
                    Wapen_Lijst[i][0] -= 1
                elif c_move == 5 and Wapen_Lijst[i][1] > 0:
                    Wapen_Lijst[i][1] -= 1
while character["hp"] > 0:
    if new_level == True:
        Speelveld = [randrange(0, int(size)), randrange(0, int(size))]
        Wapen_Lijst = {}
        mapmeting_gen()
        map_gen()
        level += 1
        new_level = False
    elif new_level == False:
        print("NAAM:  " + character["name"])
        print("LEVENSDUUR:  " + str(character["hp"]))
        print("WAPEN:  " + str(character["weapon_sterkte"]) + "     " + character["weapon_naam"])
        print("BESCHERMING:  " + str(character["armor_sterkte"]) + "     " + character["armour_naam"])
        for i in Wapen_Lijst:
            print("TEGENSTANDER:  " + str(i) + "     " + "KRACHT: " + str(Wapen_Lijst[i][2]) + "     " + "AANVAL STERKTE: " + str(Wapen_Lijst[i][3]))
        player_input()
        ai()
        map_gen()
        if Speelveld[0] == Karakter[0] and Speelveld[1] == Karakter[1]:
            new_level = True

print()
print()
print(" ________________________________________________")
print("|    G    A    M    E        O    V    E    R    |")
print(" IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
print()
print("            BEHAALDE: L E V E L: " + str(level))