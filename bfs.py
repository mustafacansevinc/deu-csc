class Node(object):
    def __init__(self, name):
        self.name = name
        self.childs = []
        self.visited = False
        self.pre = None
    
    def connect(self,childs):
        for child in childs:
            self.childs.append(child)

def breadth_first_search():
    # For A to B
    node = A
    node.visited = True
    while node != B:
        for child in node.childs:    
            if child not in Q and child.visited == False:
                Q.append(child)
                child.pre = node
        node = Q.pop(0)
        node.visited = True
    print "The route is:"
    while node != None:
        print node.name
        node = node.pre

if __name__ == "__main__":
    A = Node("A")
    X = Node("X")
    Y = Node("Y")
    Z = Node("Z")
    K = Node("K")
    L = Node("L")
    M = Node("M")
    N = Node("N")
    T = Node("T")
    B = Node("B")
    
    A.connect([X, Y, Z])
    X.connect([A, Y, K])
    Y.connect([A, X, L, M, N])
    Z.connect([A, N])
    K.connect([X, L])
    L.connect([Y, K, M, B])
    M.connect([Y, L, T, B])
    N.connect([Y, Z, T])
    T.connect([M, N, B])
    
    Q = []
    
    breadth_first_search()
