totalPeople = int(input("Enter total number of people: "))

if totalPeople == 1:
  print("The person survives by default")
elif totalPeople == 2:
  print("The last person who will survive will be the 1st person")
elif totalPeople >= 3:
  nearestPowerOf2 = []

  for i in range(totalPeople):
    x = 2**i
    nearestPowerOf2.append(x)
  
    if x > totalPeople:
      break
  
  
  difference = (totalPeople - nearestPowerOf2[-2])
  
  answer = 1 + (difference * 2)
  
  if answer % 10 == 1:
    print("The last person who will survive will be the", str(answer) + "st person")
  
  elif answer % 10 == 2:
    print("The last person who will survive will be the", str(answer) + "nd person")
  
  elif answer % 10 == 3:
    print("The last person who will survive will be the", str(answer) + "rd person")
  
  else:
    print("The last person who will survive will be the", str(answer) + "th person")
else:
  print("Invalid")