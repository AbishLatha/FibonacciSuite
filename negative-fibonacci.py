#Print a list of "n" number of elements in Fibonacci series towards negative side
n = int(input("Enter the number of elements to be printed towards negative side: "))
def negative_fib(n):
    sequence = [-1,0]
    n1 = sequence[0] # OR n1 = -1
    n2 = sequence[1] # OR n2 = 0
    for n in range(-n,-2):
        prev = n2 - n1
        n2 = n1
        n1 = prev
        sequence = [prev] + sequence #Adding elements to left side of the initial list
    return sequence
negative_fib(n)
