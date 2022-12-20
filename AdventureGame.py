weapon = False

def strangeCreature():
  actions = ["Spring bosjes in","Ren weg"]
  global weapon
  print("Onderweg tussen het rennen naar de bossen kom je een agent tegen, Wat doe je?")
  userInput = ""
  while userInput not in actions:
    print("Options: Ren weg/Spring bosjes in")
    userInput = input()
    if userInput == "Spring bosjes in":
      if weapon:
        print("Je bent weggekomen, Goed bezig!")
      else:
        print("De politie heeft je te pakken, Volgende keer beter.")
      quit()
    elif userInput == "Ren weg":
      showSkeletons()
    else:
      print("Voer een geldige commando in.")
      
def showSkeletons():
  directions = ["Vooruit","forward"]
  global weapon
  print("You see a wall of skeletons as you walk into the room. Someone is watching you. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: left/Vooruit/forward")
    userInput = input()
    if userInput == "left":
      print("You find that this door opens into a wall. You open some of the drywall to discover a knife.")
      weapon = True
    elif userInput == "Vooruit":
      introScene()
    elif userInput == "forward":
      strangeCreature()
    else:
      print("Voer een geldige commando in.")
      

def hauntedRoom():
  directions = ["right","left","Vooruit"]
  print("You hear strange voices. You think you have awoken some of the dead. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: right/left/Vooruit")
    userInput = input()
    if userInput == "right":
      print("Multiple goul-like creatures start emerging as you enter the room. You are killed.")
      quit()
    elif userInput == "left":
      print("You made it! You've found an exit.")
      quit()
    elif userInput == "Vooruit":
      introScene()
    else:
      print("Voer een geldige commando in.")

def cameraScene():
  directions = ["forward","Vooruit"]
  print("You see a camera that has been dropped on the ground. Someone has been here recently. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: forward/Vooruit")
    userInput = input()
    if userInput == "forward":
      print("You made it! You've found an exit.")
      quit()
    elif userInput == "Vooruit":
      showShadowFigure()
    else:
      print("Voer een geldige commando in.")
      
def showShadowFigure():
  directions = ["right","Vooruit"]
  print("You see a dark shadowy figure appear in the distance. You are creeped out. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: right/left/Vooruit")
    userInput = input()
    if userInput == "right":
      cameraScene()
    elif userInput == "left":
      print("You find that this door opens into a wall.")
    elif userInput == "backward":
      introScene()
    else:
      print("Voer een geldige commando in.")


def introScene():
  directions = ["left","right","Vooruit"]
  print("You are at a crossroads, and you can choose to go down any of the four hallways. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: left/right/backward/Vooruit")
    userInput = input()
    if userInput == "left":
      showShadowFigure()
    elif userInput == "right":
      showSkeletons()
    elif userInput == "Vooruit":
      hauntedRoom()
    elif userInput == "backward":
      print("You find that this door opens into a wall.")
    else: 
      print("Voer een geldige commando in.")

if __name__ == "__main__":
  while True:
    print("Welkom bij mijn avontuur spel!")
    print("Als de Red nose Shooter ben jij zojuist het huis van de burgemeester verlaten.")
    print("Helaas waren er camera's aanwezig in en rondom het pand.")
    print("Ze hebben jou dus gespot, Help de Red Nose Shooter om vrij te komen!")
    print("Laten we beginnen met jou naam: ")
    name = input()
    print("Veel succes, " +name+ ".")
    introScene()