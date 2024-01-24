#fibonnachi 0 1 1 
def fib(n):
    if n==1 or n==2:
        return (n-1)
    
    return fib(n-1)+fib(n-2)


def main():
    print(fib(10))


main()