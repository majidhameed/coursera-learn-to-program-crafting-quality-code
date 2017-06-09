# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """
    
    def __init__(self, symbol, row, col):
        '''(Rat, str, int, int) -> NoneType
        
        Creates Rat object for the given symbol (1-char), sets rats initial (grid) location the given row, col values.
        Set sprouts eaten count to zero
        
        >>> rat_1 = Rat('J',1,2)
        >>> rat_1.symbol
        'J'
        >>> rat_1.row
        1
        >>> rat_1.col
        2
        >>> rat_1.num_sprouts_eaten
        0
        '''
        
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0
        
    def set_location(self, row, col):
        '''(Rat, int, int) -> NoneType
        
        Sets the Rat location to new location using given row, col values
        
        >>> rat_2 = Rat('P',1,0)
        >>> rat_2.set_location(2,3)
        >>> rat_2.row
        2
        >>> rat_2.col
        3
        '''
        self.row = row
        self.col = col    
    
    def eat_sprout(self):
        '''(Rat) -> NoneType
        
        Rat eats the sprout
        
        >>> rat_1 = Rat('J',0,0)
        >>> rat_1.eat_sprout()
        >>> rat_1.num_sprouts_eaten
        1
        '''
        self.num_sprouts_eaten += 1
        
    def __str__(self):
        '''(Rat) -> str
        
        Return a string representation of the rat, in this format: symbol at (row, col) ate num_sprouts_eaten sprouts.
        
        >>> rat_1 = Rat('J',3,2)
        >>> rat_1.eat_sprout()
        >>> str(rat_1)
        'J at (3, 2) ate 1 sprouts.'
        '''
        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.symbol, self.row, self.col, self.num_sprouts_eaten) 

class Maze:
    """ A 2D maze. """

    def __init__(self, maze, rat_1, rat_2):
        '''(Maze, list of list of str, Rat, Rat) -> NoneType
        
        Initializes the Maze object with the given maze (grid) and 2 rats rat_1 and rat_2.
        Initially num_sprouts_left is set to the number of sprouts present in maze
        
        >>> maze_1 = Maze([['#', '#', '#', '#', '#', '#', '#'],
        ... ['#', '.', '.', '.', '.', '.', '#'],
        ... ['#', '.', '#', '#', '#', '.', '#'],
        ... ['#', '.', '.', '@', '#', '.', '#'],
        ... ['#', '@', '#', '.', '@', '.', '#'],
        ... ['#', '#', '#', '#', '#', '#', '#']],
        ... Rat('J', 1, 1),
        ... Rat('P', 1, 4))
        >>> str(maze_1.rat_1)
        'J at (1, 1) ate 0 sprouts.'
        >>> str(maze_1.rat_2)
        'P at (1, 4) ate 0 sprouts.'
        >>> len(maze_1.maze)
        6
        >>> len(maze_1.maze[0])
        7
        >>> maze_1.maze[3][3]=='@'
        True
        >>> maze_1.num_sprouts_left
        3
        '''
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        
        sprouts_in_maze = 0
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if self.get_character(row, col) == SPROUT:
                    sprouts_in_maze += 1
        self.num_sprouts_left = sprouts_in_maze       
        
    def is_wall(self, row, col):
        '''(Maze, int, int) -> bool
        
        Return True if and only if there is a wall at the given row and column of the maze.
        
        >>> maze_1 = Maze([['#', '#', '#', '#', '#', '#', '#'],
        ... ['#', '.', '.', '.', '.', '.', '#'],
        ... ['#', '.', '#', '#', '#', '.', '#'],
        ... ['#', '.', '.', '@', '#', '.', '#'],
        ... ['#', '@', '#', '.', '@', '.', '#'],
        ... ['#', '#', '#', '#', '#', '#', '#']],
        ... Rat('J', 1, 1),
        ... Rat('P', 1, 4))
        >>> maze_1.is_wall(0,0)
        True
        >>> maze_1.is_wall(3,3)
        False
        '''
        return self.maze[row][col] == WALL
        
    def get_character(self, row, col):
        '''(Maze, int, int) -> str
        
        Return the character in the maze at the given row and column. 
        If there is a rat at that location, then its character should be returned rather than HALL
        
        >>> maze_1 = Maze([['#', '#', '#', '#', '#', '#', '#'],
        ... ['#', '.', '.', '.', '.', '.', '#'],
        ... ['#', '.', '#', '#', '#', '.', '#'],
        ... ['#', '.', '.', '@', '#', '.', '#'],
        ... ['#', '@', '#', '.', '@', '.', '#'],
        ... ['#', '#', '#', '#', '#', '#', '#']],
        ... Rat('J', 1, 1),
        ... Rat('P', 1, 4))
        >>> maze_1.get_character(1,1)
        'J'
        >>> maze_1.get_character(1,4)
        'P'
        >>> maze_1.get_character(0,0)
        '#'
        >>> maze_1.get_character(3,3)=='@'
        True
        >>> maze_1.get_character(1,2)
        '.'
        >>> maze_1.get_character(0,0)=='#'
        True
        >>> maze_1.get_character(3,3)=='@'
        True
        '''
       
        if [self.rat_1.row,self.rat_1.col]==[row,col]:
            return self.rat_1.symbol
        elif [self.rat_2.row,self.rat_2.col]==[row,col]:
            return self.rat_2.symbol
        else:
            return self.maze[row][col]
        
    def move(self, rat, vertical_direction_change, horizontal_direction_change):
        '''(Maze, Rat, int, int) -> bool
        
        Move the rat in the given direction, unless there is a wall in the way. 
        Also, check for a Brussels sprout at that location and, if present:
            have the rat eat the Brussels sprout,
            make that location a HALL, and
            decrease the value that num_sprouts_left refers to by one.
        Return True if and only if there wasn't a wall in the way.
        
        >>> maze_1 = Maze([['#', '#', '#', '#', '#', '#', '#'],
        ... ['#', '.', '.', '.', '.', '.', '#'],
        ... ['#', '.', '#', '#', '#', '.', '#'],
        ... ['#', '.', '.', '@', '#', '.', '#'],
        ... ['#', '@', '#', '.', '@', '.', '#'],
        ... ['#', '#', '#', '#', '#', '#', '#']],
        ... Rat('J', 1, 1),
        ... Rat('P', 1, 4))
        >>> maze_1.move(maze_1.rat_2,DOWN,NO_CHANGE)
        False
        >>> maze_1.move(maze_1.rat_1,DOWN,NO_CHANGE)
        True
        >>> maze_1.move(maze_1.rat_1,DOWN,NO_CHANGE)
        True
        >>> str(maze_1.rat_1)
        'J at (3, 1) ate 0 sprouts.'
        >>> maze_1.move(maze_1.rat_1,DOWN,NO_CHANGE)
        True
        >>> str(maze_1.rat_1)
        'J at (4, 1) ate 1 sprouts.'
        >>> print(maze_1)
        #######
        #...P.#
        #.###.#
        #..@#.#
        #J#.@.#
        #######
        J at (4, 1) ate 1 sprouts.
        P at (1, 4) ate 0 sprouts.
        '''
        row = rat.row 
        col = rat.col
        
        row += vertical_direction_change
        col += horizontal_direction_change
        
        if self.is_wall(row, col):
            return False
        else:
            if self.get_character(row, col) == SPROUT:
                rat.eat_sprout()
                self.num_sprouts_left -=1
            rat.row = row
            rat.col = col
            self.maze[row][col] = HALL     
            return True
        
        
    def __str__(self):
        '''(Maze) -> str
        
        Return a string representation of the maze, using the format shown in this example:
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        
        >>> maze_1 = Maze([['#', '#', '#', '#', '#', '#', '#'],
        ... ['#', '.', '.', '.', '.', '.', '#'],
        ... ['#', '.', '#', '#', '#', '.', '#'],
        ... ['#', '.', '.', '@', '#', '.', '#'],
        ... ['#', '@', '#', '.', '@', '.', '#'],
        ... ['#', '#', '#', '#', '#', '#', '#']],
        ... Rat('J', 1, 1),
        ... Rat('P', 1, 4))
        >>> print(maze_1)
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        '''
        maze_str = ''
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                maze_str+=self.get_character(row, col)
            maze_str+='\n'
        
        maze_str+=str(self.rat_1)
        maze_str+='\n'
        maze_str+=str(self.rat_2)
        return maze_str

if __name__=='__main__':
    import doctest
    doctest.testmod()
