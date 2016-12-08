currentLocation = [0, 0] # x y
currentDirection = 0 # up right down left
pastLocations = []
  

def main():
  f = open('input.txt', 'r')
  instructions = f.read()
  instructionList = instructions.split(', ')
  pastLocations.append(currentLocation)
  for instruction in instructionList:
    moveToNewDirection(instruction)

def moveToNewDirection(instruction):
  changeIndex = getIndex(instruction[:1])
  changeAmount = getAmount(instruction[1:])
  changeCurrentLocation(instruction)

def getIndex(direction):
  if (direction == 'R'):
    currentDirection += 1
  else:
    currentDirection -= 1
  if (currentDirection > 3):
    currentDirection = 0
  elif (currentDirection < 0):
    currentDirection = 3

  if (currentDirection == 0 or currentDirection = 2):
    return 1
  return 0

def getAmount(int(changeAmount):
  if (currentDirection == 0 or currentDirection == 1)
    return changeAmount
  return -changeAmount

def changeCurrentLocation(instruction):
  

if __name__ == '__main__':
  main()