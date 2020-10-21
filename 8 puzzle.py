import random
import colorama
import msvcrt

colorama.init()
box = [[' ','1','2'],
            ['3','4','5'],
            ['6','7','8']]

def display():
	s = ''
	for i in range(3):
		s += " +-----------+\n"
		for j in range(3):
			s += " | "+str(box[i][j])
		s += " |\n"
	s += " +-----------+\n"
	print(s)
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
		if(j > 0):
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
		if(i > 0):
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
left = b'a'
right = b'd'
up = b'w'
down = b's'
pointer = [0,0]
shuffle()
while(True):
	display()
	action = msvcrt.getch()
	if(action == b'q'):
		break
		
	print("\033[A"*9)
	takeaction(action)
