import train

#start and end cities are 'a' and 'e' respectively
startCity = train.startCity  #'a'
endCity = train.endCity  #'e'

#use this function to get neighbors
print(train.getNeighbors('a'))

#path
stack = [startCity]
checkedLocations = [startCity]
paths = {startCity: []}


def findPath():
  global stack
  global paths
  while True:
    tempStack = []
    while len(stack) > 0:
      currentLocation = stack.pop()
      for neighbor in train.getNeighbors(currentLocation):
        #if we have not checked the location yet
        if neighbor not in checkedLocations:
          #update stack and checkedLocations
          checkedLocations.append(neighbor)
          tempStack.append(neighbor)
          #update paths
          tempList = paths[currentLocation].copy()
          tempList.append(neighbor)
          paths[neighbor] = tempList
          #check if solution has been found
          if neighbor == endCity:
            return "solution found"
    stack = tempStack


#check if path is valid
findPath()
print(paths)
print(train.checkPath(paths[endCity]))
