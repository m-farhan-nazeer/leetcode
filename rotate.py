def rotateArr(arr, d):
        # code here
        temp = []
        for i in range(d):
                temp.append(arr[i])
        for i in range(d,len(arr)):
                arr[i-d]= arr[i]

        print(arr)

print(rotateArr([1,2,3,4,5],2))