import Grid


#Just x and y
#class Point2D:
    


#This can have a Point2D. Considered that but want to do it this way instead for now
class SnakePart:
    def __init__(self, posX, posY): 
        self.posX = posX
        self.posY = posY

    #I want to test this too
    def swapPart(lhs, rhs):
        tempX = lhs.posX
        tempY = lhs.posY

        lhs.posX = rhs.posX
        lhs.posY = rhs.posY

        rhs.posX = tempX
        rhs.posY = tempY

    #Test that swapPart works
    def TestSwap():
        lhs = SnakePart(1, 2)
        rhs = SnakePart(5, 7)

        assert lhs.posX == 1 and lhs.posY == 2
        assert rhs.posX == 5 and rhs.posY == 7

        SnakePart.swapPart(lhs, rhs)
        assert lhs.posX == 5 and lhs.posY == 7
        assert rhs.posX == 1 and rhs.posY == 2

        #Need to figure out if I can use a syntax like this though
        #assert(lhs.posX == 5 and lhs.posY == 7)
        #assert(rhs.posX == 1 and rhs.posY == 2)


class SnakeBody:
    def __init__(self, posX = 5, posY = 2, addParts = 6):
        self.snakeParts = []

        #Create the head
        self.snakeParts.append(SnakePart(posX, posY))
        self.dirX = 1
        self.dirY = 0
        #Add just one body for testing
        self.addBodies(addParts)

        #For movement, we do a 'swap in place' iteration of the list
        #Also can be used as a tail/head for whatever algo
        self.tempPart = SnakePart(0, 0)

    def addBodies(self, numParts):
        for x in range(numParts):
            self.addBody()

    #Just add one body first and call this inside a loop instead for reduced complexity
    def addBody(self):
        #Add in the opposite direction of movement

        #Set the add direction to be the tail (each to the body if just head)
        length = len(self.snakeParts)
        self.tempPart = self.snakeParts[length - 1]

        #The missile knows where it is at all times. 
        # It knows this because it knows where it isn't. By subtracting where it is from where it isn't, 
        # or where it isn't from where it is (whichever is greater), it obtains a difference, or deviation. 

        #Head follows a different rule where u can just add the opposite of the direction
        if length == 1:
            self.snakeParts.append(SnakePart(self.tempPart.posX - self.dirX, self.tempPart.posY - self.dirY))
        else:
            offsetX = self.tempPart.posX - self.snakeParts[length - 2].posX
            offsetY = self.tempPart.posY - self.snakeParts[length - 2].posY
            self.snakeParts.append(SnakePart(self.tempPart.posX + offsetX, self.tempPart.posY + offsetY))
        


    def setDir(self, dirX, dirY):
        #Reject directional sets that go 'inside' of itself
        if self.dirX is not -dirX:
            self.dirX = dirX
        if self.dirY is not -dirY:
            self.dirY = dirY

    def move(self):

        #I want this to be a copy but I am not sure if it will yet so to prevent bug I will do by hand first
        #self.tempPart = self.snakeParts[0]

        self.tempPart.posX = self.snakeParts[0].posX
        self.tempPart.posY = self.snakeParts[0].posY

        #We cannot just apply the same offset to every body. For now just do only the head
        self.snakeParts[0].posX += self.dirX
        self.snakeParts[0].posY += self.dirY

        #The missle will go to where it should be rather than where it ought to be

        #We use a 'swap' concept in order to iterate past the head. This will have a time complexity of O(n) 
        #and space of I think O(1 + 1) or something (since I use an extra cell as a temp)
        for i in range(1, len(self.snakeParts)):
            SnakePart.swapPart(self.tempPart, self.snakeParts[i])





#Snake controller 'has a' relationship with a grid (so they can set the placement)
#Snake controller also 'has a' snake to

#https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
class SnakeController:
    def __init__(self, grid : Grid.GridTable):
        #I think I already made a mistake somehow. If I was wise I'd test that this grid is the mutable reference or something
        #but honestly maybe doing anything where I have to consider the mutablity of my memory in Python is like trying to go
        #skateboarding using a surfboard with wheels drilled onto the side.
        self.grid = grid


        self.snake = SnakeBody()
        self.snake.setDir(0, 1)

        self.elapsedTickTime = 0
        self.tickRate = 0.10
    
    #Set snake color
    def updateSnake(self):
        for part in self.snake.snakeParts:
            self.grid.setCellColor(part.posX, part.posY, "green")

    
    def Draw(self, screen):
        self.grid.draw(screen)
    
    def moveSnake(self):
        #Reset the color of the previous snake inputs
        #One method is to just 'paint over' all the previous positions before the movemoment. Not the best as its O(n^2)
        #but N is not gonna be bigger than the grid.

        for part in self.snake.snakeParts:
            self.grid.setCellColor(part.posX, part.posY, self.grid.gridColor)

        self.snake.move()
        

    def setSnakeDirection(self, dirX, dirY):
 
        self.snake.setDir(dirX, dirY)

    def updateTick(self):
        self.moveSnake()
        self.updateSnake()

    def update(self, deltaTime):
        self.elapsedTickTime += deltaTime
        if self.elapsedTickTime > self.tickRate:
            self.elapsedTickTime = 0
            self.updateTick()
        



     

