#John Liu, jl4582
#Karan Rai, kr3287
#Justyn Ngo, jmn365

from room import Room

class Maze:
    #constructor
    def __init__(self, st=None, ex=None):
        self.start = st
        self.exit = ex
        self.current = st
    #getter for current location
    def getCurrent(self):
        return self.current
    #getter to determine the exit 
    def atExit(self):
        if self.current == self.exit:
            return True
        else:
            return False
    #move north, south, east or west and if they reach exit, print exit message
    def moveNorth(self):
        if self.current.getNorth() is None:
            print("Direction invalid, try again.")
        else:
            self.current = self.current.getNorth()
            if self.atExit():
                print("You have found the exit!")

    def moveSouth(self):
        if self.current.getSouth() is None:
            print("Direction invalid, try again.")
        else:
            self.current = self.current.getSouth()
            if self.atExit():
                print("You have found the exit!")

    def moveEast(self):
        if self.current.getEast() is None:
            print("Direction invalid, try again.")
        else:
            self.current = self.current.getEast()
            if self.atExit():
                print("You have found the exit!")

    def moveWest(self):
        if self.current.getWest() is None:
            print("Direction invalid, try again.")
        else:
            self.current = self.current.getWest()
            if self.atExit():
                print("You have found the exit!")
    
    #set current back to the start
    def reset(self):
        self.current = self.start
        print(f"You are now back at the start: {self.current}")