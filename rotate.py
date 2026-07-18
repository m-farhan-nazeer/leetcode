def rotateArr(arr, d):
        # code here
        for j in range(d):
            temp = arr[0]
            print("temp",temp)
            for i in range(1,len(arr)):
                arr[i-1]= arr[i]
                
            arr[len(arr)-1]= temp
            print("arr",arr)
        return arr

print(rotateArr([1,2,3,4,5],2))