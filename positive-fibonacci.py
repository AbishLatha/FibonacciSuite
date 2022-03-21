### Print "n" number of positive elements in Fibonacci series
n = int(input("Enter the number of elements to be printed: "))
def positive_fib(n):
    sequence = [0,1]
    n1 = sequence[0] # OR n1 = 0;
    n2 = sequence[1] # OR n2 = 1;
    for n in range(2,n):
        nxt = n1 + n2;
        n1 = n2
        n2 = nxt
        sequence.append(nxt)
### Return a list with Fibonacci series with "n" elements   
    return sequence
positive_fib(n)
