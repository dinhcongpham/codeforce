## link problem: https://codeforces.com/problemset/problem/1913/A

def solve(ab):
  for i in range(len(ab) // 2, 0, -1):
    if ab[i] == '0':
      continue
    l, r = int(ab[0:i]), int(ab[i:len(ab)])
    if l <  r:
      return f"{l} {r}"
  return -1


# Read input
t = int(input())  # Number of test cases
for _ in range(t):
    ab = str(input())
    print(solve(ab))
