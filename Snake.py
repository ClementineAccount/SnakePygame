import Grid



#Snake controller 'has a' relationship with a grid (so they can set the placement)


#https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
class SnakeController:
    def __init__(self, grid : Grid.GridTable):
        #I think I already made a mistake somehow. If I was wise I'd test that this grid is the mutable reference or something
        #but honestly maybe doing anything where I have to consider the mutablity of my memory in Python is like trying to go
        #skateboarding using a surfboard with wheels drilled onto the side.
        self.grid = grid

        #To Do: Make this a different class that has coordinates representing the body and head
        #Rows and Col
        self.snakeHeadPosX = 2
        self.snakeHeadPosY = 2
    
    #Set snake color
    def updateSnake(self):
        self.grid.setCellColor(self.snakeHeadPosX, self.snakeHeadPosY, "green")
    
    def Draw(self, screen):
        self.grid.draw(screen)
    
     
