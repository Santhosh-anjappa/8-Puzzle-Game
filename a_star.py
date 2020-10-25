import copy
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
    return cost

Q.append(Node(box,0,get_cost(box.box), None, None))

def check_node_exists(node):
    for inode in Q:
        for i in range(node.config.size):
            for j in range(node.config.size):
                if(inode.config.box[i][j] != node.config.box[i][j]):
                    return True
    return False

to_visit = [Q[0]]
count = 0
while(True):
    flag = False
    for node in to_visit:
        parent = node
        print("++ Parent ++")
        parent.config.display()
        print("|| Parent ||")

        act = parent.config.takeaction(np.Box.left)
        new_node = Node(parent.config, parent.g + 1, get_cost(parent.config.box), np.Box.left, parent)
        if(act): 
            parent.config.takeaction(np.Box.right)
        if(check_node_exists(new_node)):
            Q.append(new_node)
            print("|| left:",new_node.f)
            # new_node.config.display()
            # parent.config.display()
            if(get_cost(parent.config.box) == 0):
                print("Got it")
                parent.config.display()
                flag = True
                break
        # input("press ok: ")
    
        act = parent.config.takeaction(np.Box.right)
        new_node = Node(parent.config, parent.g + 1, get_cost(parent.config.box), np.Box.right, parent)
        if(act): parent.config.takeaction(np.Box.left)
        if(check_node_exists(new_node)):
            Q.append(new_node)
            print("|| right:",new_node.f)
            # new_node.config.display()
            # parent.config.display()
            if(get_cost(parent.config.box) == 0):
                print("Got it")
                parent.config.display()
                flag = True
                break
        # input("press ok: ")

        act = parent.config.takeaction(np.Box.up)
        new_node = Node(parent.config, parent.g + 1, get_cost(parent.config.box), np.Box.up, parent)
        if(act): parent.config.takeaction(np.Box.down)
        if(check_node_exists(new_node)):
            Q.append(new_node)
            print("|| up:",new_node.f)
            # new_node.config.display()
            # parent.config.display()
            if(get_cost(parent.config.box) == 0):
                print("Got it")
                parent.config.display()
                flag = True
                break
        # input("press ok: ")

        act = parent.config.takeaction(np.Box.down)
        new_node = Node(parent.config, parent.g + 1, get_cost(parent.config.box), np.Box.down, parent)
        if(act): parent.config.takeaction(np.Box.up)
        if(check_node_exists(new_node)):
            Q.append(new_node)
            print("|| down:",new_node.f)
            # new_node.config.display()
            # parent.config.display()
            if(get_cost(parent.config.box) == 0):
                print("Got it")
                parent.config.display()
                flag = True
                break
        # input("press ok: ")

        parent.visited = True
        count += 1

    print("checked:{}".format(count))
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
            input("tets")
        # print("======================")
        for node in Q:
            if(node.f == mn_f and node.visited != True):
                to_visit.append(node)
                # node.config.display()
        # print("======================")
        # input("press ok: ")
        

    else:
        print("Solved it ")
        exit()