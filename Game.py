# Game
#Player needs to pass few rounds given and by the end the player should have atleast min health of 1.The player can use the Armour given

power = [1,2,3,6]
armor = 7 
total = sum(power)

armorused = min(armor,max(power))

print( total- armorused +1)
