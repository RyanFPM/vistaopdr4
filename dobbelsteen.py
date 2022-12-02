import random

max = int(input("Hoeveel ogen heeft de dobbelsteen maximaal "))
totaalDobbel = []
aantal = int(input("Hoeveel dobbelstenen wil je gooien? "))
for i in range(aantal):
    print("Dobbelsteen",(i + 1),"gooide" ,random.randint(1,max) )
    totaalDobbel.append(random.randint(1,max))
print("je hebt totaal", sum(totaalDobbel), "ogen gegooid")
