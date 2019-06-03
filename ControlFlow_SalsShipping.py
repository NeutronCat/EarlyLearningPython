#Write a program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.
def calc_ground(weight):
  if (weight > 10):
    ppp = 4.75
  elif (weight > 6) and (weight <= 10):
    ppp = 4.00
  elif (weight > 2) and (weight <= 6):
    ppp = 3.00
  else:
    ppp = 1.50
  groundship = (ppp + 20.00)
  return groundship

def calc_drone(weight):
  if (weight > 10):
    ppp = 14.25
  elif (weight > 6) and (weight <= 10):
    ppp = 12.00
  elif (weight > 2) and (weight <= 6):
    ppp = 9.00
  else:
    ppp = 4.50
  droneship = (ppp)
  return droneship

def calc_best_ship(weight):
  groundprice = calc_ground(weight)
  droneprice = calc_drone(weight)
  premprice = 125.00
  print("Premier Ground: " + str(premprice))
  print("Drone Price: " + str(droneprice))
  print("Ground Price: " + str(groundprice))
  if (premprice <= groundprice) and (premprice <= droneprice):
    return "Your cheapest shipping is Premium Ground! Total Cost: $"+str(premprice)
  elif (droneprice < premprice) and (droneprice < groundprice):
    return "Your cheapest shipping is Drone! Total Cost: $"+str(droneprice)
  elif (groundprice < premprice) and (groundprice < droneprice): 
    return "Your cheapest shipping is Ground! Total Cost: $"+str(groundprice)

print(calc_best_ship(8))
