import numpy

class Maze:
    #the newly-created maze has external walls but not internal walls
    def __init__(self, width=5, height=5):
        self.maze = []
        self.width = width
        self.height = height
        #external walls are blue
        for i in range(0, self.height):
            #look at tuples for N, E, S, W walls
            self.maze.append([])
            print(self.maze)
            #self.maze.append([["blue"]])
            for j in range(0, self.width):
                self.maze[i].append(['', '', '', ''])
                if i == 0:
                    #south
                    self.maze[i][j][2] = 'blue'
                elif i == self.height-1:
                    #north
                    self.maze[i][j][0] = "blue"

                elif j == self.width-1:
                    #east
                    self.maze[i][j][1] = "blue"

                elif j == 0:
                    #west
                    self.maze[i][j][3] = "blue"

        #test 1
        crd = ''
        for i in range(0, len(self.maze)):
            for j in range (0, len(self.maze[i])):
                crd += f"({i},{j})" + "  "
            print(crd)
            crd = ''
        #test 2
        crd = ''
        for i in range(0, len(self.maze)):
            for j in range(0, len(self.maze[i])):
                crd += f"{self.maze[i][j]}" + "  "
            print(crd)
            crd = ''

    def add_horizontal_wall(self, x_coordinate, horizontal_line):
        #horizontal walls are red
        #n, e, s, w
        #at actual crd it'll be south
        self.maze[x_coordinate][horizontal_line][2]('red')
        #at crd underneath it'll be north
        self.maze[x_coordinate][horizontal_line-1][0]('red')

    def add_vertical_wall(self, y_coordinate, vertical_line):
        #vertical walls are green
        # n, e, s, w
        # at actual crd it'll be east
        self.maze[vertical_line][y_coordinate][1].append('green')
        # at crd to its  it'll be west
        self.maze[vertical_line+1][y_coordinate][3]('green')

    def get_walls(self, x_coordinate:int, y_coordinate:int) -> tuple[bool, bool, bool, bool]:
        walls = self.maze[x_coordinate][y_coordinate]
        if_walls = []
        for i in range(0, len(walls)):
            if walls[i] != '':
                if_walls.append(True)
            else:
                if_walls.append(False)
        return (if_walls[0], if_walls[1], if_walls[2], if_walls[3])

maze = Maze(11, 5)

print(maze)
