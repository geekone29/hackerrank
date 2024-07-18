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

## A Very Big Sum

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