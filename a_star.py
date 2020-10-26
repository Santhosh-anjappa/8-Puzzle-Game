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

Q.append(Node(box,0,get_cost(box.box), None, None))

def check_node_exists(node):
    for inode in Q:
        flag = False
        for i in range(node.config.size):
            for j in range(node.config.size):
                if(inode.config.box[i][j] != node.config.box[i][j]):
                    flag = True
                    break
            if(flag): break
        if(not flag):
            return False
    return True

to_visit = [Q[0]]
visited_nodes = []
count = 0
solution = None
box_action = [np.Box.left, np.Box.right, np.Box.up, np.Box.down]
box.display()
while(True):
    flag = False
    for node in to_visit:
        parent = node

        for action in box_action:
            new_node = Node(parent.config, parent.g + 1, get_cost(parent.config.box), action, parent)
            act = new_node.config.takeaction(action)
            if(check_node_exists(new_node) and act):
                Q.append(new_node)
                if(get_cost(new_node.config.box) == 0):
                    solution = new_node
                    flag = True
                    break

        parent.visited = True
        count += 1
    # populate to_visit nodes ( nodes with min f will be choosen to visit )
    if(flag == False):
        to_visit = []
        mn_f = None
        for node in Q:
            if(node.visited != True):
                if(mn_f is None):
                    mn_f = node.f
                elif(mn_f > node.f):
                    mn_f = node.f
        if(mn_f == None):
            print("all are visited")
            input("Hmm...")
        for node in Q:
            if(node.f == mn_f and node.visited != True):
                to_visit.append(node)
        
        print("Items to explore in this round {}".format(len(to_visit)),end='\r')

    else:
        actions = []
        print("Solved it ")
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
        print("Numbers of nodes explores: {}".format(count))
        exit()