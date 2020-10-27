import copy
import time
import heapq
np = __import__("8 puzzle")

class Node:
    def __init__(self, config, g, h, action, parent):
        self.config = copy.deepcopy(config)
        self.g = g
        self.h = h
        self.f = g+h
        self.action = action
        self.parent = parent
        self.visited = False
        self.act = self.config.takeaction(self.action)
        self.hash = self.getHash()

    def getHash(self,):
        h = ''
        for row in self.config.box:
            for ele in row:
                h += ele
        return h

    # for heap comparing
    def __lt__(self, other):
        return self.f < other.f
        
nodeH = {}
n = int(input("Enter Board Size: "))
Q = []
box = np.Box(n)
target = copy.deepcopy(box)
box.shuffle()


t_pos = {}
for i,row in enumerate(target.box):
    for j,ele in enumerate(row):
        t_pos[ele] = [i,j]

def get_cost(box):
    " computing manhattan cost"
    cost = 0
    for i,row in enumerate(box):
        for j,ele in enumerate(row):
            if(ele != ' '):
                cost += abs(i-t_pos[ele][0]) + abs(j-t_pos[ele][1])

    " computing linear conflicts"
    conflict_pairs = 0
    for i,row in enumerate(box):
        for j,ele in enumerate(row):
            if(ele != ' '):
                i1,j1 = t_pos[ele][0], t_pos[ele][1]
                if( (i == i1 and j != j1) or (i != i1 and j == j1)):
                    conflict_pairs += 1
    cost += conflict_pairs

    return cost

q = []
heapq.heappush(q, Node(box,0,get_cost(box.box), None, None))

def check_node_exists(node):
    if(node.hash in nodeH):
        return True
    return False
        
count = 0
solution = None
box_action = [np.Box.left, np.Box.right, np.Box.up, np.Box.down]
box.display()
nodeH[q[0].hash] = 1

while(True):
    flag = False
    ####
    if(q):
        parent = heapq.heappop(q)
    else:
        print("Solution not found")
        break
    for action in box_action:
        new_node = Node(parent.config, parent.g + 1, get_cost(parent.config.box), action, parent)
        if(not check_node_exists(new_node) and new_node.act):
            heapq.heappush(q, new_node)
            nodeH[new_node.hash] = 1
            if(get_cost(new_node.config.box) == 0):
                solution = new_node
                flag = True
                break

    parent.visited = True
    count += 1

    print("Total number of nodes explored {}".format(count),end='\r')
    if(flag):
        actions = []
        print("\nSolved it ")
        n_node = solution
        while(n_node.parent != None):
            actions.append(n_node.action)
            n_node = n_node.parent
        
        actions = actions[::-1]
        for i,act in enumerate(actions):
            box.takeaction(act)
            box.display()
            time.sleep(1)
            r = box.size*2+3
            if(i != len(actions)-1):
                print("\033[A"*r)
        print("Number of moves made: {}".format(len(actions)))
        exit()
    ####