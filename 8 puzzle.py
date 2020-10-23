import random
import colorama
import msvcrt
import math
n = int(input("Enter Board Size: "))	# Puzzle board size
colorama.init()

box = [[str(i) for i in range(j,j+n)] for j in range(1,n*n,n)]
box[-1][-1] == ' '

def display():
	ntimes = math.floor(math.log10(n*n))
	s = ''
	brd = "---" + "-"*ntimes + "+"
	line = " +" + brd*n + "\n"
	for i in range(n):
		s += line
		
		for j in range(n):
			s += " | {0:>{1}s}".format(str(box[i][j]), ntimes+1)
		s += " |\n"
	s += line
	print(s)
#display()

def shuffle():
	n = random.randint(50,250)
	i = 0
	while(i< n):
		# action = random.randint(97,100)
		action = random.choice([left,right,up,down])
		takeaction(action)
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
pointer = [n-1,n-1]
shuffle()
while(True):
	display()
	action = msvcrt.getch()
	if(action == b'q'):
		break
		
	print("\033[A"*9)
	takeaction(action)
