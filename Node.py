# code is from https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/

class Edge:
    def __init__(self, src, des):
        self.src = src
        self.des = des


class DAG:
    def __init__(self):
        self.nodes = set()
        self.edges = set()

    def edgeExists(self, src, des):
        for edge in self.edges:
            if edge.src == src and edge.des == des:
                return True
        return False

    def addEdge(self, src, des):
        if self.edgeExists(src, des):
            return False

        if not self.edgeExists(src, des):
            node = self.getNode(src)
            node2 = self.getNode(des)

            if self.isChild(src, des):
                print("Cannot add edge (" + str(src) + "," + str(des) + ") because it would create a cycle in an acyclic graph")
                return False
            self.edges.add(Edge(src, des))

            newNode = node
            newNode.children.add(des)
            self.nodes.remove(node)
            self.nodes.add(newNode)

            newNode2 = node2
            newNode2.parents.add(src)
            self.nodes.remove(node2)
            self.nodes.add(newNode2)
            return True
        else:
            print("edge (" + str(src) + "," + str(des) + ") already exists")
            return False

    def getNode(self, key):
        node = None
        for currentNode in self.nodes:
            if currentNode.key == key:
                node = currentNode
        return node


    def getListOfParentNodes(self, key):
        listOfParents = self.getListOfParentNodesRecursive(key, 0)
        listOfParents.sort(key=lambda tup: tup[1])
        return listOfParents

    def getListOfParentNodesRecursive(self, key, depth):
        node = self.getNode(key)
        if node is None:
            print("node with key " + key + " does not exist")
            return []
        listOfParents = [(node.key, depth)]
        for parent in node.parents:
            listOfParents += self.getListOfParentNodesRecursive(parent, depth+1)
            listOfParents = list(dict.fromkeys(listOfParents))
        return listOfParents



    # checks if node with key1 is child of node with key2
    def isChild(self, key1, key2):
        if key1 == key2:
            return False
        node = self.getNode(key1)
        node2 = self.getNode(key2)
        if node is None or node2 is None:
            if node is None:
                print("node with key " + str(key1) + " does not exist in graph")
            if node2 is None:
                print("node with key " + str(key2) + " does not exist in graph")
            return False
        for parent in node.parents:
            if parent == key2:
                return True

        return self.isChildRecursive(key1, key2)

    def isChildRecursive(self, key1, key2):
        node = self.getNode(key1)
        node2 = self.getNode(key2)
        for parent in node.parents:
            if parent == key2:
                return True

        node = self.getNode(key1)
        childFound = False
        for parent in node.parents:
            if self.isChildRecursive(parent, key2):
                childFound = True
        return childFound

    def addNode(self, key):
        nodeExists = False
        for currentNode in self.nodes:
            if currentNode.key == key:
                print("node " + str(key) + " already exists")
                return False

        self.nodes.add(Node(key))
        return True


    def findLCA(self, key1, key2):
        node1 = self.getNode(key1)
        node2 = self.getNode(key2)
        if node1 is None or node2 is None:
            if node1 is None:
                print("node with key " + str(key1) + " does not exist")
            if node2 is None:
                print("node with key " + str(key2) + " does not exist")
            return None
        node1Parents = self.getListOfParentNodes(key1)
        node2Parents = self.getListOfParentNodes(key2)
        node1ParentsDict = dict(self.getListOfParentNodes(key1))
        node2ParentsDict = dict(self.getListOfParentNodes(key2))

        lca = None
        for index in range(0, max(len(node1Parents), len(node2Parents))):
            if index < len(node1Parents):
                try:
                    depth = node2ParentsDict[node1Parents[index][0]]
                    lca = node1Parents[index][0]
                    break
                except KeyError:
                    pass
            if index < len(node2Parents):
                try:
                    depth = node1ParentsDict[node2Parents[index][0]]
                    lca = node2Parents[index][0]
                    break
                except KeyError:
                    pass
        return lca


class Node:
    def __init__(self, key):
        self.key = key
        self.parents = set()
        self.children = set()
