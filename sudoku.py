
# sudoku grid
grid = [
        [0,0,0,0,9,1,4,0,0],
        [0,0,0,7,0,0,0,0,0],
        [5,0,3,0,0,4,9,0,0],
        [7,0,4,0,0,0,0,5,0],
        [9,0,0,0,2,0,0,0,1],
        [0,2,0,0,0,0,6,0,4],
        [0,0,6,3,0,0,0,0,7],
        [0,0,0,0,7,6,0,0,0],
        [0,0,7,8,1,0,0,0,0]
        ]

# printing sudoku grid
def print_grid():
  global grid
  for i in range(9):
    for j in range(9):
      print(grid[i][j],end=' ')
    print()


# checking row column and 3x3 box of grid
# If number exists, it returns False. If all conditions completes without return False it returns True, accepting number can be set in that position.
def check_row_col_mat(x,y,n):
  global grid

  # traversing through row and checking for number existence
  for i in range(9):
    if(grid[x][i]==n):
      return False

  # traversing through column and checking for number existence
  for j in range(9):
    if(grid[j][y]==n):
      return False

  # checking 3x3 matrix 
  x0 = (x//3)*3
  y0 = (y//3)*3
  for i in range(3):
    for j in range(3):
      if(grid[x0+i][y0+j]==n):
        return False

  return True


# solving sudoku using recursive by backtracing the wrong choices
def solve():
  global grid
  for r in range(9):
    for c in range(9):
      if(grid[r][c]==0):
        for n in range(1,10):
          if(check_row_col_mat(r,c,n)):
            grid[r][c] = n
            solve()
            grid[r][c] = 0
        return
  print_grid()
  input('more?')

solve()

