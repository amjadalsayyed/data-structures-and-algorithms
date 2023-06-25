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


# x = Hashtable()
# x.set('x',70)
# x.set('a',20)
# x.set('s',30)
# # x.set('d',40)
# x.set('r',50)
# # print(x.hash)
# print(x.has('d'))

