sponsorMoney = 1000
goats = [["Lucy","Zelda","Mario","Bowser","Luigi","Link","Ganon","Tetra","Koopa Troopa"],[666, 1000, 500, 10, 120, 100, 150, 69, 420]]

def select():
  yeet = False
  while yeet == False:
    print("---------------------")
    print("Sponsor a goat today!")
    print("---------------------")
    print("1 = View goat Menu")
    print("2 = Find a goat")
    print("3 = Sponsor scheme funds")
    print("4 = Sponsor a goat")
    print("5 = Give us a goat")
    print("6 = Sponsor cost")
    print("0 = Yeet away today")
    choice = int(input("Your decision: "))
    if choice == 1:
      goatList()
    elif choice == 2:
      findGoat()
    elif choice == 3:
      schemeMoneys()
    elif choice == 4:
      adoptGoat()
    elif choice == 5:
      giveGoat()
    elif choice == 6:
      goatCost()
    elif choice == 0:
      yeet = True
    else:
      print("You have entered an invalid number. Please enter another option: ")

def goatList():
  print("The goats currently avaliable for sponsoship are: ")
  for y in range(0,len(goats[0])):
    print (goats[0][y])


def findGoat():
  found = True
  goatName = input("What is the name of the goat you would like to sponsor: ")
  for x in range(0,len(goats[0])):
    if goatName == goats[0][x]:
      found = False
  if found == False:
    print (goatName,"is currently avaliable to sponsor")
  else:
    print(goatName,"is not currently avaliable to sponsor")

def schemeMoneys():
  print("The goat sponsorship scheme currently has £", sponsorMoney)

def adoptGoat():
  adoptName = input("What goat would you like to adopt: ")
  yote = False
  for z in range(0,len(goats[0])):
    if adoptName == goats[0][z]:
      yote = True
  if yote == True:
    print("Your sponsorship is being processed and you should receive your forms in the next 3-5 working days")
    ind = goats[0].index(adoptName)
    global sponsorMoney
    sponsorMoney = sponsorMoney + goats[1][ind]
    goats[0].remove(adoptName)
    value = goats[1][ind]
    goats[1].remove(value)
  else:
    print(adoptName,"is not a goat currently avaliable for adoption. Please enter another choice: ")

def giveGoat():
  newGoat = input("What is the name of the goat you would like to donate: ")
  goats[0].append(newGoat)
  print ("Thank you for your contribution! Please consider donating to us as well!")

def goatCost():
  name = input("What is the name of the goat whose sponsorship price you would like to see: ")
  zoom = False
  for a in range(0,len(goats[0])):
    if name == goats[0][a]:
      zoom = True
  if zoom == True:
    indexNo = goats[0].index(name)
    print(name,"costs £",goats[1][indexNo])
  else:
    print(name,"is not a goat currently avaliable for sponsorship")

select()
