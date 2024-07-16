# Day 6: :Let's Review

# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input().strip())

for _ in range(t):
    S = input().strip()
    N = len(S)
    oddString = ""
    evenString = ""
    for i in range(N):
        if i % 2 == 0:
            evenString += S[i]
        else:
            oddString += S[i]
    print(evenString + " " + oddString)
