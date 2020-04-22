# Python3 program to find the maximum depth of tree

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = -1


    # Compute the "node height" of a tree -- the number of nodes
    # along the longest path from the root node down to the
    # farthest leaf node
    def calculateHeight(self):

        depth = 0

        if self.height > -1:
            depth = self.height;

        else:

            # Compute the depth of each subtree
            lDepth = 0
            if self.left is not None:
                lDepth = self.left.calculateHeight()

            rDepth = 0
            if self.right is not None:
                rDepth = self.right.calculateHeight()

            # Use the larger one
            if (lDepth > rDepth):
                depth = lDepth + 1
            else:
                depth = rDepth + 1

        self.height = depth

        return depth

def run_tests():
    forest = []

    # Driver program to test above function
    root1 = Node(1)
    forest.append(root1)

    root1.left = Node(2)
    forest.append(root1.left)

    root1.right = Node(3)
    forest.append(root1.right)

    root1.left.left = Node(4)
    forest.append(root1.left.left)

    root1.left.right = Node(5)
    forest.append(root1.left.left)

    root2 = Node(6)
    forest.append(root2)

    root2.left = Node(7)
    forest.append(root2.left)

    root2.right = Node(8)
    forest.append(root2.right)

    root2.left.left = Node(9)
    forest.append(root2.left.left)

    root2.left.right = Node(10)
    forest.append(root2.left.right)

    maxDepth = 0
    maxRoot = None
    for node in forest:
        print("Height of the node " + str(node.data))
        depth = node.calculateHeight()
        print(" is " + str(depth))
        if depth > maxDepth:
            maxDepth = depth
            maxRoot = node

    print("The node with max depth is " + str(maxRoot.data)+ " and its depth is " + str(maxRoot.calculateHeight()))

if __name__ == "__main__":
    run_tests()
