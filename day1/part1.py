def main():
    f = open('input.txt', 'r')
    instructions = f.read()
    instructionList = instructions.split(', ')
    coords = [0, 0, 0, 0] #up right down left
    direction = 0
    for instruction in instructionList:
        direction = getDirection(direction, instruction[:1])
        coords[direction] += int(instruction[1:])
    print (coords)
    x = coords[0] - coords[2]
    y = coords[1] - coords[3]
    total = abs(x) + abs(y)
    print (total)

def getDirection(direction, turn):
    if (turn == 'R'):
        direction += 1
    else:
        direction -= 1
    
    if (direction > 3):
        return 0
    elif (direction < 0):
        return 3
    
    return direction



if __name__ == '__main__':
    main()