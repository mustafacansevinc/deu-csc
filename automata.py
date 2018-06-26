class NodeState:
    right, left, middle = range(3)

class Node:
    def __init__(self, name, left, middle, right, state):
        self.name = name
        self.left = left
        self.right = right
        self.middle = middle
        self.state = state

    def process_coin(self, coin):
        coin.path += self.name
        if self.state == NodeState.left:
                self.switch_state()
                self.left.process_coin(coin)
        elif self.state == NodeState.right:
                self.switch_state()
                self.right.process_coin(coin)
        elif self.state == NodeState.middle:
                self.switch_state()
                if self.middle is None:
                    print coin.path
                else:
                    self.middle.process_coin(coin)

    def switch_state(self):
        if self.state == NodeState.left: self.state = NodeState.right
        elif self.state == NodeState.right: self.state = NodeState.left

        # if self.State == NodeState.Middle and self.Middle is None:
        #     print "We're on one of the Exit Nodes. Handle"

class Coin:
    def __init__(self):
        self.path = ""

if __name__ == "__main__":
    # Lets say we have a gambling machine design as below.
    # Player throws coin from one of the inputs,
    # The coin hits the switchs and therefore navigates.
    # If the coin hits one of the Exit Nodes the player wins.
    # We don't want the player to win, so we want to handle the exit nodes.
    # This is a program doing it on automata basis.
    
    C = Node("C", None, None, None, NodeState.middle)
    D = Node("D", None, None, None, NodeState.middle)
    N2 = Node("2", C, None, D, NodeState.right)
    N1 = Node("1", C, None, N2, NodeState.right)
    N3 = Node("3", N2, None, D, NodeState.right)
    A = Node("A", None, N1, None, NodeState.middle)
    B = Node("B", None, N2, None, NodeState.middle)
    coin1 = Coin()
    A.process_coin(coin1)   # A is the input node for coin1.
    for i in range(5):
        A.process_coin(Coin())
