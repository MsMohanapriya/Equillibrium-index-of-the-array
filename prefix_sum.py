def prefix_sum(array):
    
    for index in range(1,len(array)):
        array[index]= array[index-1]+array[index]
    return array
    
array=list(map(int,input().split()))
print(prefix_sum(array))
        