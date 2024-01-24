def mul(val,n):
    if n==1:
        return val
    t =mul(val,n-1)
    return val +t

def main():

    print(mul(2,5))

main()