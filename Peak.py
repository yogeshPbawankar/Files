def peakEle(arr):
    st = 0
    end = len(arr) -1
    while st <= end:
        mid = (st + (end -st) // 2)
        if arr[mid] > arr[mid -1] and arr[mid] > arr[mid +1]:
            return mid
            if arr[0] > arr[1]:
                return 0
            if arr[len(arr)-1]> arr[len(arr)-2]:
                return len(arr)-1
        if arr[mid] > arr[mid -1]:
            st = mid +1
        else :
            end = mid -1
    return -1

arr = [5,10,20,15]
print("Peak Element: ",peakEle(arr))
