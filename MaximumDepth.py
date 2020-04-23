# Python3 program to find the maximum depth of Node


# A binary Node node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = -1


    def getPath(self):
        path = []
        if self.left:
            path = self.left.heightPath()

        path.append(self.data)

        if self.right:
            path = path + self.right.heightPath()

        return path


    def heightPath(self):

        path = []

        hLeft = 0
        hRight = 0
        if self.left is not None:
            hLeft = self.left.height
        if self.right is not None:
            hRight = self.right.height

        if hLeft > hRight:
            path.append(self.data)
            path = self.left.heightPath()

        elif hRight > 0:
            path.append(self.data)
            path = path + self.right.heightPath()

        else:
            path = [self.data]

        return path


    # Compute the "node height" of a Node -- the number of nodes
    # along the longest path from the root node down to the
    # farthest leaf node
    def calculateHeight(self):

        depth = 0

        if self.height > -1:
            depth = self.height;

        else:

            # Compute the depth of each subNode
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

    rDepth = 0
    lDepth = 0
    maxDepth = 0
    maxRoot = None
    for node in forest:
        depth = node.calculateHeight()
        lDepth = 0
        if node.left is not None:
            lDepth = node.left.height

        rDepth = 0
        if node.right is not None:
            rDepth = node.right.height

        if (rDepth+lDepth+1) > maxDepth:
            maxDepth = rDepth+lDepth+1
            maxRoot = node

        print("Height of the node " + str(node.data))
        print(" is " + str(depth)+" and depth sum is " + str(rDepth+lDepth+1))

    print("The node with max depth is " + str(maxRoot.data)+ " and its depth is " + str(maxRoot.calculateHeight()))
    print( " and sum depth is " + str(maxDepth))

    print( "longest path is " + str(maxRoot.getPath()))





if __name__ == "__main__":
    run_tests()


