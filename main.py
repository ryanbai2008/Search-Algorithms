import train

#start and end cities are 'a' and 'e' respectively
startCity = train.startCity #'a'
endCity = train.endCity #'e'

#use this function to get neighbors
print(train.getNeighbors('a'))

#path
paths = {startCity:[]}

def findPath():

  return None

#check if path is valid
print(f"The paths you have found are: {paths}")
print(train.checkPath(paths[endCity]))
