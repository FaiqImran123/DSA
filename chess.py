#Faiq Imran

def positions(arr, queen_postion,size, flag=0):
    if queen_postion[0]<0 or queen_postion[0]>=size or queen_postion[1]<0 or queen_postion[1]>=size:
        return 0
    
    elif arr[queen_postion[0]] [queen_postion[1]]=="x":
        return 0
    elif flag==0:
        a =positions(arr, (queen_postion[0]-1, queen_postion[1]+1),size, flag=1)
        b =positions(arr,(queen_postion[0]-1, queen_postion[1]-1),size, flag=2)
        c =positions(arr, (queen_postion[0]+1, queen_postion[1]+1),size, flag=3)
        d =positions(arr, (queen_postion[0]+1, queen_postion[1]-1),size, flag=4)
        e =positions(arr, (queen_postion[0]-1, queen_postion[1]),size, flag=5)
        f =positions(arr, (queen_postion[0]+1, queen_postion[1]),size, flag=6)
        g =positions(arr, (queen_postion[0], queen_postion[1]+1),size, flag=7)
        h =positions(arr, (queen_postion[0], queen_postion[1]-1),size, flag=8)
        return a +b+c+d+e+f+g+h

    elif flag==1:
        return 1+positions(arr, (queen_postion[0]-1, queen_postion[1]+1),size, flag=1)
    elif flag==2:
        return 1+positions(arr,(queen_postion[0]-1, queen_postion[1]-1),size, flag=2)
    elif flag==3:
        return 1+positions(arr, (queen_postion[0]+1, queen_postion[1]+1),size, flag=3)

    elif flag==4:
        return 1+positions(arr, (queen_postion[0]+1, queen_postion[1]-1),size, flag=4)
    elif flag==5:
        return 1+positions(arr, (queen_postion[0]-1, queen_postion[1]),size, flag=5)
    elif flag==6:
        return 1+positions(arr, (queen_postion[0]+1, queen_postion[1]),size, flag=6)

    elif flag==7:
        return 1+positions(arr, (queen_postion[0], queen_postion[1]+1),size, flag=7)
    elif flag==8:
        return 1+positions(arr, (queen_postion[0], queen_postion[1]-1),size, flag=8)

    
        




def main():
    size, num_of_obstacles =map(int, input().split())
    queen_postion =tuple(map(int, input().split()))
    queen_postion =(queen_postion[0]-1, queen_postion[1]-1)
    arr =[[0 for i in range(size)] for j in range(size)]

    for _ in range(num_of_obstacles):
        val =tuple(map(int, input().split()))
        val =(val[0]-1, val[1]-1)
   
        arr[val[0]][val[1]] ="x"
   
    print(positions(arr, queen_postion, size))
        

    
    





main()