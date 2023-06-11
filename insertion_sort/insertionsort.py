def insert (sorted,int):
    """
    take a sorted list and insert the value of the int in so it keep the list sorted correctly
    """
    i = 0
    while i < len(sorted) and int > sorted[i]:
        i+=1
    while i < len(sorted):
        temp = sorted[i] 
        sorted[i] = int
        int = temp
        i += 1
    sorted.append(int)
    

def insertsort (input):
    """
    take a none sorted list and return the list in a new sorted list ascendant 
    """
    sorted = [] 
    sorted.append(input[0]) 
    for i in range(1,len(input)):
        insert(sorted,input[i])
    return sorted    


print(insertsort([8,4,23,42,16,15]))