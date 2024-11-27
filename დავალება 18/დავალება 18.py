# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# def printLeafNodes(root):
#     if root is None:
#         return
#     if root.left is None and root.right is None:
#         print(root.data, end=" ")
#     else:
#         printLeafNodes(root.left)
#         printLeafNodes(root.right)

# def countEdges(root):
#     if root is None:
#         return 0
#     return countEdges(root.left) + countEdges(root.right) + 1
