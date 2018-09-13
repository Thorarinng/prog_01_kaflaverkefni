# Your function definition goes here
def fibo(tala):
    n1, n2 = 0, 1
    print(1, end=' ')
    for i in range(tala-1):
        fib = n1 + n2
        n1 = n2
        n2 = fib
        print(fib, end=' ')


n = int(input("Input the length of Fibonacci sequence (n>=1): "))
# Call your function here   
fibo(n)