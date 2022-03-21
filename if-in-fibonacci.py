#Function to find if quesry number is present in Fibonacci series

# 1st step - Building Fibonacci series 
n = int(input("Enter a number: "))
def if_in_fib(n):
    sequence = [0,1]
    n1 = sequence[0]
    n2 = sequence[1]
    i = 2
    while i < n+2:
        nxt = n1 + n2;
        n1 = n2
        n2 = nxt
        sequence.append(nxt)
        i = i+1

# Checking if the query number is present in Fibonacci series
    if n in sequence:
        print(str(n) + " is present at position {}".format(sequence.index(n)+1))
        print(sequence[:sequence.index(n)+2])
    else:
        print(str(n) + " is not present in Fibonacci series")
if_in_fib(n)
