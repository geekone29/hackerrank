# Language: Python 3
## 1. Simple Array Sum

Complete the simpleArraySum function in the editor below. It must return the sum of the array elements as an integer.

simpleArraySum has the following parameter(s):

- ar: an array of integers

``` python
def simpleArraySum(ar):
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
```

## 2. Solve Me First

**Function Description**

Complete the solveMeFirst function in the editor below.

solveMeFirst has the following parameters:

- int a: the first value
- int b: the second value

Returns
- int: the sum of  and 

``` python
def solveMeFirst(a,b):
    return a + b

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)

```

## 3. Compare the Triplets

Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).

The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].

- If a[i] > b[i], then Alice is awarded 1 point.
- If a[i] < b[i], then Bob is awarded 1 point.
- If a[i] = b[i], then neither person receives a point.
Comparison points is the total points a person earned.

Given a and b, determine their respective comparison points.

**Example**

a = [1, 2, 3]
b = [3, 2, 1]
- For elements *0*, Bob is awarded a point because a[0] .
- For the equal elements a[1] and b[1], no points are earned.
- Finally, for elements 2, a[2] > b[2] so Alice receives a point.
The return array is [1, 1] with Alice's score first and Bob's second.

**Function Description**

Complete the function compareTriplets in the editor below.

compareTriplets has the following parameter(s):

- int a[3]: Alice's challenge rating
- int b[3]: Bob's challenge rating
Return

- int[2]: Alice's score is in the first position, and Bob's score is in the second.

```python
def compareTriplets(a, b):
    alice = 0 
    bob = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
        else:
            pass
    return [alice, bob]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
```

## 4. A Very Big Sum

In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

**Function Description**

Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.

aVeryBigSum has the following parameter(s):

int ar[n]: an array of integers .

**Return**

long: the sum of all array elements

```python
def aVeryBigSum(ar):
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
```

## 5. Diagonal Difference

Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix `arr`  is shown below:

```python
1 2 3
4 5 6
9 8 9 
```
The left-to-right diagonal = `1+5+9 = 15`. The right to left diagonal = `3+5+9 = 17`. Their absolute difference is `|15-17| = 2`.

**Function description**

Complete the  function in the editor below.

diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers
Return

int: the absolute diagonal difference

```python
def diagonalDifference(arr):
    first_d = 0
    second_d = 0
    n = len(arr)
    for i in range(n):
        first_d += arr[i][i]
        second_d += arr[i][n - 1 - i]
    return abs(first_d-second_d)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
```

## 6. Plus Minus

**Function Description**

Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):
- int arr[n]: an array of integers

**Print**
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with `6` digits after the decimal. The function should not return a value.

```python
def plusMinus(arr):
    n = len(arr)
    positive = 0
    negative = 0
    zeros = 0
     
    for num in arr:
        if num > 0:
            positive += 1
        elif num == 0:
            zeros += 1
        else:
            negative += 1
    return [positive / n, negative /n, zeros / n]

if __name__ == '__main__':    
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = plusMinus(arr)
    
    print(f"{result[0]:.6f}")
    print(f"{result[1]:.6f}")
    print(f"{result[2]:.6f}")
```

## 7. Staircase

Staircase detail

This is a staircase of size :
```
   #
  ##
 ###
####
```
Its base and height are both equal to . It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size .

**Function Description**

Complete the staircase function in the editor below.

staircase has the following parameter(s):

- int n: an integer

**Print**

Print a staircase as described above.

```python
def staircase(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(' ', end='')
        for k in range(i):
            print('#', end='')
        print()

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)

```