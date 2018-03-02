import random
box = [[' ','1','2'],
            ['3','4','5'],
            ['6','7','8']]

def display():
	for i in range(3):
		print(" +-----------+")
		for j in range(3):
			print(" | "+str(box[i][j]),end='')
		print(" |")
	print(" +-----------+")
#display()

def shuffle():
	n = random.randint(50,100)
	i = 0
	while(i< n):
		action = random.randint(97,100)
		takeaction(chr(action))
		#display()
		i += 1

def moveleft(pointer):
	i = pointer[0]
	j = pointer[1]
	try:
		box[i][j] = box[i][j+1]
		j += 1
	except IndexError:
		pass
	box[i][j] = ' '
	return [i,j]

def moveright(pointer):
	i = pointer[0]
	j = pointer[1]
	try:
		box[i][j] = box[i][j-1]
		j -= 1
	except IndexError:
		pass
	box[i][j] = ' '
	return [i,j]

def moveup(pointer):
	i = pointer[0]
	j = pointer[1]
	try:
		box[i][j] = box[i+1][j]
		i += 1
	except IndexError:
		pass
	box[i][j] = ' '
	return [i,j]

def movedown(pointer):
	i = pointer[0]
	j = pointer[1]
	try:
		box[i][j] = box[i-1][j]
		i -= 1
	except IndexError:
		pass
	box[i][j] = ' '
	return [i,j]


def takeaction(action):
	global pointer
	if(action == left):
		# if a is pressed
		pointer = moveleft(pointer)
	elif(action == right):
		# if d is pressed
		pointer = moveright(pointer)
	elif(action == up):
		# if w is pressed
		pointer = moveup(pointer)
	elif(action == down):
		# if s is pressed
		pointer = movedown(pointer)
left = 'a'
right = 'd'
up = 'w'
down = 's'
pointer = [0,0]
shuffle()
display()
action = input()
while(action != 'q'):
	takeaction(action)
	display()
	action = input()