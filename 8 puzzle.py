import random
import colorama
import msvcrt
import math
n = int(input("Enter Board Size: "))	# Puzzle board size
colorama.init()

box = [[str(i) for i in range(j,j+n)] for j in range(1,n*n,n)]
box[-1][-1] = ' '

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

def shuffle():
	n = random.randint(50,250)
	i = 0
	while(i< n):
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
		pointer = moveleft(pointer)
	elif(action == right):
		pointer = moveright(pointer)
	elif(action == up):
		pointer = moveup(pointer)
	elif(action == down):
		pointer = movedown(pointer)

if(__name__ == "__main__"):
	left  = b'a'
	right = b'd'
	up    = b'w'
	down  = b's'
	pointer = [n-1,n-1]
	shuffle()
	while(True):
		display()
		action = msvcrt.getch()
		if(action == b'q'):
			break

		r = n*2+3	
		print("\033[A"*r)
		takeaction(action)
