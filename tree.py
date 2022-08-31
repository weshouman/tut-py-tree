import os
DEBUG = True

DEFAULT_PATH = "sample"
DEFAULT_ROOT = "a.txt"
def getFileTree(dirname, filename):

  data = {"dir": dirname}
  node = getFileNodes(filename, data)
  tree = Tree(node=node)

  return tree

def getFileNodes(filename, data={}):
  """
  Given a filename, parse it
  return a node with children assigned based on the filename parsed from the given file content, recursively
  """

  # Capture data
  lines = []

  parentNode = TreeNode(filename)

  with open (os.path.join(data["dir"], filename), "r") as f:
    lines = f.readlines()

  if (DEBUG):
    if len(lines)> 0:
      linesStr = ', '.join(lines).replace('\n','')
      print(f"- [create]  [children] [{linesStr}] of {filename}")

  for line in lines:
    
    childNode = getFileNodes(line.strip(), data)
    if (DEBUG): print(f"- [created] [child]    {childNode}")
    parentNode.AddChild(childNode)

  if (DEBUG): print(f"- [return]  [parent]   {parentNode}")
  return parentNode

class Tree():
  def __init__(self, data=None, node=None):
    if (data):
      self.root = TreeNode(data)
    elif (node):
      self.root = node

  def SetRoot(self, data):
    self.root = TreeNode(data)

  def Print(self):
    self.root.Traverse()

class TreeNode():
  def __init__(self, data):
    self.data = data
    self.children = []

  # DO NOT USE the following, otherwise the same children list will be used every node
  # def __init__(self, data, children=[]):
  #   self.data = data
  #   self.children = children

  def __str__(self):
    # expected size for spacing
    EXP_MAX_DATA_LEN = 10
    return f"Node : {id(self)} : {self.data:<{EXP_MAX_DATA_LEN}} : child count {len(self.children)}"

  def AddChildByData(self, data):
    self.children.append(TreeNode(data))
    return self.children[-1]

  def AddChild(self, node):
    self.children.append(node)
    return self.children[-1]

  def _traversalPrint(self, level):
    dash ="`-"
    print(f"{dash:>{level}}{self.data}")

  def Traverse(self, level = 1, function=None):
    if function != None:
      function(self)
    else:
      self._traversalPrint(level)
    for node in self.children:
      node.Traverse(level+1, function)

def main():
  if (DEBUG): print("# Tree creation\n")
  tree = getFileTree(DEFAULT_PATH, DEFAULT_ROOT)

  if (DEBUG): print("\n---\n")

  if (DEBUG): print("# Tree printing\n")
  tree.Print()

if __name__ == "__main__":
  main()
