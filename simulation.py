import random
n=1000    #where n is the number of simulation per number of doors
for k in range(3,50): #k is the number of closed doors present
  switch,dont_switch=0,0
  for i in range(n): #looping through each simulation scenario

    #randomly choosing the door the contestant chooses
    chosenDoor=random.randint(1,k) 
    
    #randomly choosing the door behind which the prize actually exists
    prizeDoor=random.randint(1,k)

    #initalizing the door to be revealed by Monty
    revealDoor=random.randint(1,k)
    #Ensuring that the revealed door is not the one chosen by the contestant, nor is it the one which contains the prize
    while revealDoor==prizeDoor or revealDoor==chosenDoor:
      revealDoor=random.randint(1,k)
      
    #initalizing the door to be switched to by the contestant
    changedDoor=random.randint(1,k)
    #Ensuring that the switched door is not the one chosen initally by the contestant, nor is it the one which has been revealed by Monty
    while changedDoor==chosenDoor or changedDoor==revealDoor:
      changedDoor=random.randint(1,k)

    #If the switched door contains the prize, increment counter 'switch'
    switch+=1 if changedDoor==prizeDoor else 0
    #If the initally chosen door by the contestant contains the prize, increment counter 'dont_switch'
    dont_switch+=1 if chosenDoor==prizeDoor else 0
  print(k,"doors: ",switch*100/n,"%",dont_switch*100/n,"%") #Printing the chances of winning when the contestant decides to switch and not to switch
