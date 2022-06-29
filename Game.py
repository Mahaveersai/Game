# Game
#Player needs to pass few rounds given and by the end the player should have atleast min health of 1.The player can use the Armour given

power = [1,2,3,6] #given power levels
armor = 7 #given armor
total = sum(power)
armourUsed = 0

for i in power:
  if armor <= i:
    armourUsed = armor
    break
  elif armourUsed < i:
    armourUsed = i
    
print(total - armourUsed + 1) # +1 is because to maintain min health
  
