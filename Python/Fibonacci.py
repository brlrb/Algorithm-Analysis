# fibonacci [0, 1, 1, 2, 3, 5, 8, 13, 21,...N]


# Recursive 
# O(2^n) time
# O(n) space
def FibonacciRecursive(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return FibonacciRecursive(n-1) + FibonacciRecursive(n-2) 

print(FibonacciRecursive(32)) # Larger the number, the slower the computation because O(n^2) time



# Recursive with Memoization
# O(n) time
# O(n) space
def FibonacciRecursiveMem(n, memoize = {1:0, 2:1}):
    if n in memoize:
        return memoize[n]
        
    else:
        memoize[n] = FibonacciRecursiveMem(n-1, memoize) + FibonacciRecursiveMem(n-2, memoize) 
        return memoize[n]

print(FibonacciRecursiveMem(256)) # Runs in O(n) time





# Iteratively
# O(n) time
# O(1) space
def FibonacciIteratively(n):
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter = counter + 1
    return lastTwo[1] if n > 1 else lastTwo[0]

print(FibonacciIteratively(512))