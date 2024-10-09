#start and end cities
startCity = 'a'
endCity = 'e'

cityMap = {'a':('b', 'g'), 'b':('a', 'c'), 'c':('b','d', 'e', 'f'), 'g':('a', 'h', 'i'), 'i':('g', 'j'), 'd':('c'), 'e':('c'), 'f':('c'), 'h':('g'), 'j':('i')}

def getNeighbors(currentCity):
  return cityMap[currentCity]


def checkPath(path):
  currentCity = 'a'
  for step in path:
    if step in cityMap[currentCity]:
      currentCity = step
    else:
      return "Path is not valid"
  if path[-1] == endCity:
    return "Path is valid, congrats!"
  return "Path is invalid"
