## link problem: https://codeforces.com/problemset/problem/1913/B

def solve(s):
    num_1 = num_0 = 0
    for i in range(len(s)):
        if s[i] == '1':
            num_1 += 1
        else:
            num_0 += 1
    for i in range(len(s)):
        if s[i] == '1':
            if num_0 == 0:
                return len(s) - i
            num_0 -= 1
        if s[i] == '0':
            if num_1 == 0:
                return len(s) - i
            num_1 -= 1
            
    return 0


# Read input
t = int(input())  # Number of test cases
for _ in range(t):
    s = str(input())
    print(solve(s))
