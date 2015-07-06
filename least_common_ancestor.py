#########################################################################################################
# This module contains the definition and a simple unit test for the lca (least common ancestor) function
# which returns the closest common ancestors of the two nodes passed in. The algorithm I chose is as follows:
#
#   1. First find the depth of both nodes.
#   2. If one node is deeper than the other, then starting at the deepest node, we traverse upwards
#      (towards the root node) until we're at a node of the same depth as the other node.
#   3. Then, we traverse upwards from both of those nodes simultaneously until we arrive at the same node.
#   4. That node is the least common ancestor
#
# Time Analysis:
#
#   * Let's call the height of the tree H. One time-expensive part of the algorithm is this: no matter how
#     high the tree is, we have to find the depth of two nodes, which is at maximum 2*H traversals.
#   * Then we traverse upwards from the deepest node, until we're at the depth of the other node. This
#     could be at maximum H traversals. Given that a lof of nodes could live at the same height, this isn't
#     likely to be the longest process.
#   * Then we traverse upwards from both of those same-depth nodes until we arrive at the same node. The
#     worst case here is if we have two very deep nodes who's least common ancestor is the root node.
#
# Memory Analysis:
#
#   * The memory impact of this algorithm is very low. We're not copying any large pieces of data,
#     and the number of nodes doesn't have any effect the amount of memory used.
#   * There are no growing amounts of heap memory at all, just a few stack variables used
#     as the index in a for loop, or the results of some if statements.
#   * This uses no recursion, which means it's not allocating a stack over and over, which would
#     grow given a lot of elements or a tree of a large height.
#
# Alternate Solutions:
#
#   1. Build two lists, each containing the parent node list of one of the two nodes, then comparing
#      * In my chosen solution, and in this solution, we have to start by traversing up the list
#        twice, from the given nodes to the root node
#      * In this alternate solution, we'd have to traverse through that list of parents many times,
#        comparing with the results in the other list until we've found the matching value with the
#        lowest index in either list.
#      * Creating these two lists of parents would use a ton of heap memory as well, at maximum
#        2 * H * size of the Node data structure (or the size of the Node.value type)
#   2. Starting at the least deep node, check its subtrees for the other node, if not found, traverse up and
#      check the newly added subtree for the other node until we either find it, or we're at the root node.
#      * This, like my chosen solution would require finding the depth of the two nodes
#      * It wouldn't be ideal because we'd be basically traversing at least half of the entire tree. Very time costly.
#      * It wouldn't use up lots of memory though.
#
# Author: Dan Haggerty
# Date:   July 5th, 2015
#########################################################################################################

# Define a Node class with an init function
class Node:
    def __init__(self, value, parent=None):
        if not value:
            raise Exception("Node.__init__(): Must provide a value to a new Node object")
        if not parent:
            parent = self
        else:
            if not isinstance(parent, Node):
                raise Exception("Node.__init__(): parent parameter must be of type Node")
        self.value = value
        self.parent = parent

# Define our least common ancestor function
def lca(node1, node2):

    if not isinstance(node1, Node) or not isinstance(node2, Node):
        print "lca(): Inputs must be of type Node"
        return

    # Since node values are unique, we can compare two nodes by comparing their values
    if node1.value == node2.value:
        print "Node", node1.value, "and", node2.value, "are the same node, so their least common ancestor is Node", node1.value
        return node1

    # First get the depth of each branch, this is costly
    depth_node1 = 1
    depth_node2 = 1

    parent = node1.parent
    while parent != parent.parent: # Root node's parent is itself, I know that parent != parent.parent is kinda meaningless
        parent = parent.parent
        depth_node1 += 1

    parent = node2.parent
    while parent != parent.parent:
        parent = parent.parent
        depth_node2 += 1

    print "The least common ancestor of Node", node1.value, "and Node", node2.value,

    # Now traverse up the tree starting at the deepest of the two nodes, until we're at
    # the same depth as the other node
    if depth_node1 > depth_node2:
        for i in range(0, depth_node1 - depth_node2):
            node1 = node1.parent
    elif depth_node2 > depth_node1:
        for i in range(0, depth_node2 - depth_node1):
            node2 = node2.parent

    # Now we traverse up the tree starting at both nodes simultaneously until we are at the common ancestor
    while node1.value != node2.value:
        if node1.parent != node1:
            node1 = node1.parent
        if node2.parent != node2:
            node2 = node2.parent

    print "is Node", node1.value
    return node1

# Let's define the test tree data given in the problem
node1 = Node(1, None)
node2 = Node(2, node1)
node3 = Node(3, node1)
node4 = Node(4, node2)
node5 = Node(5, node2)
node6 = Node(6, node3)
node7 = Node(7, node3)
node8 = Node(8, node4)
node9 = Node(9, node4)

# Now let's run some tests
lca(node8, node9) # 8 and 9
lca(node5, node8) # 5 and 8
lca(node6, node9) # 6 and 9
lca(node1, node2) # 1 is parent of 2
lca(node1, node1) # Same node
lca(node2, Node(2, node1)) # Different node objects, same value and parent
lca("node1", "node2") # Non-nodes passed into function

