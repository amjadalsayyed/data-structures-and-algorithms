
def duck_duck_goose (k,arr):
  counter = 0
  index = 0
  while len(arr) != 1:
    counter+=1
    if index ==len(arr):
      index =0
    if counter == k:
      arr.pop(index)
      index-=1
      counter = 0
    index+=1
  return arr[0]


def duckduckgoose(k, arr):
    count = 0
    indx = 0
    while len(arr) > 1:
        count += 1
        if count == k:
            print(f"{arr[indx]} has been removed")
            arr.pop(indx)
            count = 0
            indx -= 1
        indx = (indx + 1) % len(arr)
    
    return f"{arr[0]} is the one remaining"

def Duck_Duck_Goose_h(k,arr):
    dict= {}
    c = 1
    indx = 0
    while len(dict) != len(arr)-1:
        if indx == len(arr):
            indx = 0    
        if arr[indx] in dict:
            indx+=1
            continue
        if c == k:
            dict[arr[indx]] = arr[indx]
            c = 0 
            indx+=1
            continue
        c+=1
        indx+=1
    for x in arr:
        if x not in dict :
            return x        
             


print(Duck_Duck_Goose_h(10,["A", "B", "C", "D", "E"]))