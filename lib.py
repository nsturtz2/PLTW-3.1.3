import var


def ordersand():

    sand = input("Please enter the type of sandwich you would like ")
    if sand == "chicken":
        var.cost["total"] = var.cost["total"] + var.cost["S1"]

    elif sand == "beef":
        var.cost["total"] = var.cost["total"] + var.cost["S2"]

    elif sand == "tofu":
        var.cost["total"] = var.cost["total"] + var.cost["S3"]

    else:
        ordersand()


def menu():
    print("Hello")
    print("Here is the menu")
    print("Sandwich: chicken $5.25, beef $6.25, tofu $5.75")
    print("Drink: Small $1.00 Medium $1.75 Large $2.25")
    print("French Fries: Small $1.00 Medium $1.50 Large $2.00")
    print("Ketchup Packets: $0.25 per packet")
    print(
        "We are running a special: if you get a sandwich, french fries, and a beverage then we take $1.00 off of your order"
    )


def cost():
    print(var.cost["total"])
    menu()


def orderpop():
    pop = input(
        "Please enter the size of drink you would like (s/m/l) or enter (n/no) for no drink "
    )
    if pop == "s":
        var.cost["total"] = var.cost["total"] + var.cost["D1"]

    elif pop == "m":
        var.cost["total"] = var.cost["total"] + var.cost["D2"]

    elif pop == "l":
        var.cost["total"] = var.cost["total"] + var.cost["D3"]

    elif pop == "n" or pop == "no":
        orderfries()
        var.cost["total"] = 0
    else:
        print("Error on our side please try agian")
        orderpop()


def orderfries():
    fri = input(
        "Please enter the size of fries you would like (s/m/l) or enter (n/no) for no fries"
    )
    if fri == "s":
        upgradefri()
    elif fri == "m":
        var.cost["total"] = var.cost["total"] + var.cost["F2"]
        print(var.cost["total"])
    elif fri == "l":
        var.cost["total"] = var.cost["total"] + var.cost["F3"]
    elif fri == "n" or fri == "no":
        orderkp()
        var.cost["total"] = 0
    else:
        orderfries()


def upgradefri():
    friup = input("Do you want to mega-size your fries? (y/n)")
    if friup == "y":
        var.cost["total"] = var.cost["total"] + var.cost["F3"]
    elif friup == "n":
        var.cost["total"] = var.cost["total"] + var.cost["F1"]
    else:
        upgradefri()


def orderkp():
    kp = int(input("Do you want ketchup packets (# of ketchup packets)"))
    gtotal = var.cost["total"]
    kp_s2 = 0
    kp_s2 = kp * 0.25
    var.cost["total"] = gtotal + kp_s2





def grand():
    if var.cost["combo"] == 1:
      print("With the special your grand total is:")
      print(var.cost["total"])
    else:
      print("You where not elaable for the special, your grand total is:")
      print(var.cost["total"])
def combopost():
    if var.cost["combo"] == 1:
        var.cost["total"] = var.cost["total"] - 1
    else:
        grand()
