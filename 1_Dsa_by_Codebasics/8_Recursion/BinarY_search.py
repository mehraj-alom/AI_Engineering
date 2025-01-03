def binary_search(arr,low,high,key):
        if low > high:
            return -1
        mid = (low + high) // 2
        if key == arr[mid]:
            return mid 
        elif key < arr[mid]:
            high = mid - 1
            return binary_search(arr,low,high,key)
        else :
            low = mid + 1
            return binary_search(arr,low,high,key)
            
listt = [2]
listt = []
listt = [1,2,3,4,5]
listt = [5,4,3,2,1]
listt = [34,56,89,90,100,50]
length = len(listt) - 1
print("The number is at ", binary_search(listt,0,length,34))
        
                