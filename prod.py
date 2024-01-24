def prod(arr, size):
    if size==0:
        return 1
    val =prod(arr,size-1)
    return arr[size-1]*val

arr =[1,2,3,5,6,7,8]
print(prod(arr, 7))