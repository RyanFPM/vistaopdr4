

while True:
  getal_1 = float(input("Voer het eerste getal in: "))
  print("Somsoort zijn: +, -, *, /")
  Somsoort = input("Voeg een Somsoort toe: ")
  getal_2 = float(input("Voer het tweede getal in: "))

  if Somsoort == "+":
    print("Het antwoord is: " + str(getal_1 + getal_2))
  elif Somsoort == "-":
    print("Het antwoord is: " + str(getal_1 - getal_2))
  elif Somsoort == "*":
    print("Het antwoord is: " + str(getal_1 * getal_2))
  elif Somsoort == "/":
    print("Het antwoord is: " + str(getal_1 / getal_2))
  else:
    print("Ik herken die Somsoort niet, probeer het opnieuw.")

# float = 
# str (string) = 