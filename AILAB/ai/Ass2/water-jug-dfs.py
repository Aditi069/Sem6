def LevelOrderTraversal(root):
     
    if (root == None):
        return;
   
    # Standard level order traversal code
    # using queue
    q = []  # Create a queue
    q.append(root); # Enqueue root
    while (len(q) != 0):
     
        n = len(q);
  
        # If this node has children
        while (n > 0):
         
            # Dequeue an item from queue and print it
            p = q[0]
            q.pop(0)
            print(p.list, end=' ')
            # Enqueue all children of the dequeued item
            for i in range(len(p.child)):
             
                q.append(p.child[i]);
            n -= 1
   
        print() # Print new line between two levels
        print("-------")

def fill4LitreJug(list):
    if list[0] == 4:
        return False
    list[0] = 4
    return list

def fill3LitreJug(list):
    if list[1] == 3:
        return False
    list[1] = 3
    return list

def empty3(list):
    listt = list.copy()
    if listt[1] == 0:
        return False
    listt[1] = 0
    return listt

def empty4(list):
    listt = list.copy()
    if listt[0] == 0:
        return False
    listt[0] = 0
    return listt

def transferFrom_3to4(listt):
    if listt[0]==4:
        return False
    elif listt[1] == 0:
        return False
    elif listt[0] < 4:
        if (4 - listt[0]) >= listt[1]:
            listt[0] = listt[0] + listt[1]
            listt[1] = 0
        else:
            
            emptySpace = 4 - listt[0]
            listt[1] = listt[1] - emptySpace
            listt[0] = listt[0] + emptySpace
    
    return listt

def transferFrom_4to3(listt):
    if listt[1]==3:
        return False
    elif listt[0] == 0:
        return False
    elif listt[1] < 3:
        if (3 - listt[1]) >= listt[0]:
            listt[1] = listt[1] + listt[0]
            listt[0] = 0
        else:
            
            emptySpace = 3 - listt[1]
            listt[0] = listt[0] - emptySpace
            listt[1] = listt[1] + emptySpace
    
    return listt
GOAL = [2,0]

class Node:
     
    def __init__(self, list):
         
        self.list = list
        self.child = []
        self.myParents = []
   
 # Utility function to create a new tree node
def newNode(key):   
    temp = Node(key)
    return temp
     
# Prints the n-ary tree level wise

answerslist = []
#list = [0 , 0]
#-------------------------------------------------------------------
def findOptimalPath(node):

    if node.myParents:
        if node.myParents[-1] ==GOAL:
            #print("--",node.myParents[-1],"--")
            answerslist.append(node.myParents)

    if node.list in node.myParents:
        return

    childrenlist = []
    #print("Passed Node: ",node.list)

    list1 = empty4((node.list).copy())
    list2 = empty3((node.list).copy())

    list3 = transferFrom_3to4((node.list).copy())
    list4 = transferFrom_4to3((node.list).copy())
    
    list5 = fill4LitreJug((node.list).copy())
    list6 = fill3LitreJug((node.list).copy())

    #print("lists: ", list1, list2 ,list3, list4 , list5 , list6)
    
    childrenlist.extend((list1, list2, list3,list4,list5,list6))

    childrenlist = [x for x in childrenlist if x is not False]
    #print("Childrenlist: ",childrenlist)
    #print("\n")

    

    for i in range(0,len(childrenlist)):
        (node.child).append(newNode(childrenlist[i]))
        node.child[i].myParents.extend(node.myParents)
        node.child[i].myParents.append(node.list)

        if node.child[i].myParents[-1] ==GOAL:
            answerslist.append(node.child[i].myParents)
            return

        #print("myParents: ", i +1," : ", node.child[i].myParents )
        findOptimalPath(node.child[i])






    return

#-------------------------------------------------------------------
# WE START HERE !  ----- 
mainlist= [0, 0]

root = newNode(mainlist)

findOptimalPath(root)

#print("AnswersList: ", answerslist)
print("AnswersList")
print('\n'.join(map(str, answerslist)))
smallest = []
for i in answerslist:
    smallest.append(len(i))




print("\nThe Most Optimal Path to this Water Jug Problem is :\n", answerslist[smallest.index(min(smallest))])

#---
# RunTime Values
# Infinity to 0.9s to 0.5s to 0.1s

LevelOrderTraversal(root)
