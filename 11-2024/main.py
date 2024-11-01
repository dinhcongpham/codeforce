## link problem: https://codeforces.com/problemset/problem/1906/A

def find_smallest_word(grid):
    # Define directions for adjacency (8 directions)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), 
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]
    n = 3  # Size of the grid
    smallest_word = None

    def is_in_bounds(r, c):
        return 0 <= r < n and 0 <= c < n

    # DFS function to find 3-letter words
    def dfs(r, c, path, word):
        nonlocal smallest_word
        if len(word) == 3:
            if smallest_word is None or word < smallest_word:
                smallest_word = word
            return

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if is_in_bounds(nr, nc) and (nr, nc) not in path:
                dfs(nr, nc, path | {(nr, nc)}, word + grid[nr][nc])

    # Try starting DFS from each cell
    for r in range(n):
        for c in range(n):
            dfs(r, c, {(r, c)}, grid[r][c])

    return smallest_word
      
  
# Read input
#t = int(input())  # Number of test cases
t = 3
m = []
for _ in range(t):
  x = str(input())
  m.append(list(x))
print(find_smallest_word(m))