import random
from chromosome import Chromosome

DX = [0, 1, 2, 2, 1, -1, -2, -2, -1]
DY = [0, -2, -1, 1, 2, 2, 1, -1, -2]

class Knight:

  def __init__(self, chromosome = None):

    # if no chromosome if given, create new one
    if chromosome is None:
      self.chromosome = Chromosome()
    else:
      self.chromosome = chromosome
    
    self.position = (0, 0)
    self.fitness = 0
    self.path = [(0,0)] #visited positions


  def move_forward(self, direction):
    new_x = self.position[0] + DX[direction] 
    new_y = self.position[1] + DY[direction]
    self.position = (new_x, new_y)
    self.path.append(self.position) # to keep track of the path taken


  def move_backward(self, direction):
      old_x = self.position[0] - DX[direction] 
      old_y = self.position[1] - DY[direction]
      self.position = (old_x, old_y)
      self.path.pop() # to remove last position

  def check_moves(self, cycle=None):
    #start from the initial position
    self.position = (0, 0)
    self.path = [(0,0)]

    #choose a random direction in the move cycle, stays the same for the whole chromosome
    step = random.choice([1,-1]) if cycle is None else cycle

    genes = self.chromosome.genes

    for i in range(len(genes)):
      direction = genes[i] # Initialize direction (can be 1 to 8)
      valid_move = False

      for attempt in range(8): # we have a max of 8 attempts
        if attempt > 0: #if its not our first move, we move one step
          direction = direction + step
          if direction == 9: #if we go over 8, we loop back to 1
            direction = 1
          if direction == 0: #if we go under 1, we loop back to 8
            direction = 8

        self.move_forward(direction) #move forward

        x = self.position[0]
        y = self.position[1]

        inside_board = (x >= 0 and x < 8 and y >= 0 and y < 8)

        already_visited = self.path.count(self.position) > 1

        if inside_board and not already_visited: #if the new move is valid, we break. move on to the next gene
          valid_move = True
          break

        if attempt < 7: #if we still have attempts left, move back and try agin
          self.move_backward(direction)

      if not valid_move:
        break

      genes[i] = direction
      

  def evaluate_fitness(self):
    self.fitness = 0
    visited = [] #list of visited squares

    for square in self.path: #for each square in the knight's path
      x = square[0]
      y = square[1]

      if x<0 or x>=8 or y<0 or y>=8: #if off the board, we stop counting
        break

      if square in visited: #if square already visited, we stop counting
        break

      visited.append(square) #if valid square, add to list
      self.fitness += 1

    return self.fitness
