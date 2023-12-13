# 0 = open space
# 1 = obstacle
grid = [
  [0, 0, 1, 0, 0],
  [1, 0, 0, 0, 1],
  [1, 0, 1, 0, 0],
  [1, 0, 0, 0, 0],
  [1, 1, 0, 1, 0]
]

# start and end index based on grid above
start = (0, 0)
end = (4, 2)

direction_priority = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# verify if cell is an open space or not
def verify(x, y, grid):
  rows, cols = len(grid), len(grid[0])
  return 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0


# solve for grid to find shortest path using dfs algorithm 
def solve(grid, current, end, visited, path):
  x, y = current

  if current == end:
    return path + [current]

  if not visited[x][y]:
    visited[x][y] = True

    for dx, dy in direction_priority:
      nx, ny = x + dx, y + dy
      
      if verify(nx, ny, grid):
        result = solve(grid, (nx, ny), end, visited, path + [current])
        
        if result:
          return result

  return None

# start = !*
# end = *!
# selected path = *
# unselected path = .
# obstacle = #
def print_grid(grid, path=None):
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if (i, j) == start:
        print("!*", end="   ")
      elif (i, j) == end:
        print("*!", end="   ")
      elif path and (i, j) in path:
        print("*", end="    ")
      elif grid[i][j] == 1:
        print("#", end="    ")  
      else:
        print(".", end="    ")  
    print()



def main():
  print("Input grid:")
  print_grid(grid)

  visited = [[False] * len(grid[0]) for _ in range(len(grid))]
  path = solve(grid, start, end, visited, [])

  print("\nOutput grid for shortest path:")
  print_grid(grid, path)

if __name__ == "__main__":
  main()