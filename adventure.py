import random

dir = 'x'
x = 10
y = 10
border = 20
treasure_x = random.randint(0,border)
treasure_y = random.randint(0,border)
hole_x = random.randint(0,border)
hole_y = random.randint(0,border)


print ("welcome to the adventure game.")
print ("to move type w=North, s= south d=East and a=West")
print ("press q to quit")
while dir[0] != 'q':

	print ("your location is: " + str(x) + "," + str(y))
	dir = input () + ' '
	#move your player
	if dir[0] == 'w' and y < border:
		y += 1
	if dir[0] == 's' and y > 0:
		y -= 1
	if dir[0] == 'd' and x < border:
		x += 1
	if dir[0] == 'a' and x > 0:
		x -= 1
	#treasure location
	if x == treasure_x and y == treasure_y :
		print ("you found treasure")

	#hole location
	if x == hole_x and y == hole_y :
		print ("you found a hole")
		print ("game over")
		break
