'''Class representing objects at the bottom or Leaf of the hierarchy tree.'''

def __init__(self, *args): 

    ''''Takes the first positional argument and assigns to member variable "position".'''
    self.position = args[0] 

def showDetails(self): 

    '''Prints the position of the child element.'''
    print("\t", end ="") 
    print(self.position)