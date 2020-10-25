import random
import colorama
import msvcrt
import math
import copy

colorama.init()

class Box:
	left  = b'a'
	right = b'd'
	up    = b'w'
	down  = b's'
	def __init__(self, box_size):
		self.size = box_size
		self.box = [[str(i) for i in range(j,j+self.size)] for j in range(1,self.size*self.size,self.size)]
		self.box[-1][-1] = ' '
		self.bpos = [self.size-1, self.size-1]

	def swap(self, a, b):
		a, b = b, a

	def checkBoundry(self, i, j):
		if((i >= 0 and i < self.size) and (j >= 0 and j < self.size)):
			return True
		return False

	# action definations
	def moveleft(self,):
		i = self.bpos[0]
		j = self.bpos[1]
		if(self.checkBoundry(i, j+1)):
			# swap blank
			self.box[i][j], self.box[i][j+1] = self.box[i][j+1], self.box[i][j]
			self.bpos[1] += 1	

	def moveright(self,):
		i = self.bpos[0]
		j = self.bpos[1]
		if(self.checkBoundry(i, j-1)):
			# swap blank
			self.box[i][j], self.box[i][j-1] = self.box[i][j-1], self.box[i][j]
			self.bpos[1] -= 1

	def moveup(self,):
		i = self.bpos[0]
		j = self.bpos[1]
		if(self.checkBoundry(i+1, j)):
			# swap blank
			self.box[i][j], self.box[i+1][j] = self.box[i+1][j], self.box[i][j]
			self.bpos[0] += 1

	def movedown(self,):
		i = self.bpos[0]
		j = self.bpos[1]
		if(self.checkBoundry(i-1, j)):
			# swap blank
			self.box[i][j], self.box[i-1][j] = self.box[i-1][j], self.box[i][j]
			self.bpos[0] -= 1

	def takeaction(self, action):
		if(action == self.left):
			self.moveleft()
		elif(action == self.right):
			self.moveright()
		elif(action == self.up):
			self.moveup()
		elif(action == self.down):
			self.movedown()

	def shuffle(self, ):
		n = random.randint(50,250)
		i = 0
		while(i < n):
			action = random.choice([self.left,self.right,self.up,self.down])
			self.takeaction(action)
			i += 1

	def display(self, ):
		ntimes = math.floor(math.log10(self.size*self.size))
		s = ''
		brd = "---" + "-"*ntimes + "+"
		line = " +" + brd*n + "\n"
		for i in range(n):
			s += line
			
			for j in range(n):
				s += " | {0:>{1}s}".format(str(self.box[i][j]), ntimes+1)
			s += " |\n"
		s += line
		print(s)

if __name__ == "__main__":
	n = int(input("Enter Board Size: "))
	box = Box(n)
	target = copy.deepcopy(box)
	box.shuffle()
	while(True):
		box.display()
		action = msvcrt.getch()
		if(action == b'q'):
			break
		r = box.size*2+3
		print("\033[A"*r)
		box.takeaction(action)

