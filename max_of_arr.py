def max(arr, size):
    if size==1:
        return arr[size-1]
    
    t =max(arr,size-1)
    if arr[size-1]>t:
        return arr[size-1]
    else:
        return t
    
def main():
    arr =[1,2,55,1000,6,7,8,9,100]
    print(max(arr,9))


main()
