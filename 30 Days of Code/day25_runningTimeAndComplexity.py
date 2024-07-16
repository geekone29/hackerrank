# Day 24: Running Time and Complexity

# Read the number of inputs
for _ in range(int(input())):
    # Read each input number
    num = int(input())
    
    # Check if the number is 1
    if num == 1:
        print("Not prime")  # 1 is not a prime number
    else:
        # Check if the number is even and greater than 2
        if(num % 2 == 0 and num > 2):
            print("Not prime")  # Even numbers greater than 2 are not prime
        else:
            # Check odd divisors from 3 to sqrt(num)
            for i in range(3, int(num**(1/2))+1, 2):
                if num % i == 0:
                    print("Not prime")  # Found a divisor, so not prime
                    break
            else:
                print("Prime")  # No divisors found, so prime
