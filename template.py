def solve(s, t):

    x = 0
    if len(s) > len(t):
        s, t = t, s
    for i in range(len(s)):
        if s[i] == t[i]:
            x += 1
        else:
            break
        
    if x == 0:
        return len(s) + len(t)

    return len(s) + len(t) - x + 1

# Read input
t = int(input())  # Number of test cases
for _ in range(t):
    s = str(input())
    a = str(input())
    print(solve(s, a))
