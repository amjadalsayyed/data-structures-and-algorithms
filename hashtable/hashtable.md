# Code Challenge 30

---

## Class of hash table

## takes a an optional parameter called size which represents the size of the hash table

---

## set function

### arguments : key and value

### returns: nothing

---

## Approach

### it takes the key and pass it to the hash function which returns the index

### then it checks if the table contains the any key and value in the same position if it does not it inatializes a new list at the position and add the key and value as a list of two elements key and value

---

## get function

### arguments : key

### returns: the value of the key in the hash table

### Approach

### it takes the key and pass it to the hash function which returns the index

### then it checks if the table contains the key after that it search for the key in the table and gets it value

---

## keys function

### arguments : None

### returns: a list of the keys in the hash table

### Approach

### it loops through the hash table and another nested loop loops through the elements in the hash table and access the key value and adds it to the list

---

## has function

### arguments : key

### returns: Boolean

### Approach

### it call the keys function then checks if the key exists in the list of keys

## Solution:

```python
class Hashtable:
    def __init__(self,size=5):
        self.size = size
        self.table = [None]*size

    def set (self,key,val):
        hashed_key = self.custom_hash(key)
        if self.table[hashed_key] is None:
            self.table[hashed_key]=[]
        self.table[hashed_key].append([key,val])

    def get(self,key):
        hashed_key = self.custom_hash(key)
        if self.has(key):
            if len(self.table[hashed_key])==1:
                return self.table[hashed_key][0][1]
            else:
                for i in self.table[hashed_key]:
                    if i[0] == key :
                        return i[1]
        else:
            return "KEY NOT FOUND"

    def has(self,key):
        keys = self.keys()
        if key in keys :
            return True
        return False

    def keys (self):
        keys_coll = []
        for i in self.table :
            if i is not None :
                for x in i :
                    keys_coll.append(x[0])
        return keys_coll

    def custom_hash(self, key):
        sum_of_asccii = 0
        for ch in key:
            asccii_of_ch = ord(ch)
            sum_of_asccii += asccii_of_ch
        temp = sum_of_asccii*599
        indx = temp%self.size
        return indx
```
