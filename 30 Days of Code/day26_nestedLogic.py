# Day 26: Nested Logic
# Fines for turning in the borrowed book late

# Enter your code here. Read input from STDIN. Print output to STDOUT

date_returned = str(input()).split()
date_due = str(input()).split()
delta = [
    int(date_returned[2]) - int(date_due[2]),
    int(date_returned[1]) - int(date_due[1]),
    int(date_returned[0]) - int(date_due[0])
]

if delta[0] > 0:
    print(10000)
elif delta[1] > 0 and delta[0] == 0:
    print(500*delta[1])
elif delta[2] > 0 and delta[1] == 0 and delta[0] == 0:
    print(15*delta[2])
else:
    print(0)