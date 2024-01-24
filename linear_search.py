def linear_search(arr, size,val):
    if size==0:
        return False
    if arr[size-1]==val:
        return True
    else:
        return linear_search(arr,size-1,val)
def linear_search2(arr,size,val):
    if size==0:
        return False
    return linear_search2(arr,size-1,val) or (arr[size-1]==val)

#will return position
def linear_search3(arr,size,val):
    if size==0:
        raise Exception("Arr is empty")
    if arr[size-1]==val:
        return size-1

    v =linear_search3(arr,size-1,val)
    return v

def main():
    arr =[1,2,4,5,0,-9]
    print(linear_search(arr,6,-9))
    print(linear_search2(arr,6,90))
    print(linear_search3(arr,6,5))


main()