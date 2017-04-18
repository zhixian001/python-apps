
# coding: utf-8

# In[ ]:




# In[4]:

class Stack(list):
    push = list.append
    
    def isEmpty(self):
        if not len(self):
            return True
        else:
            return False
    
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self[-1]
        
    def pop(self):
        if self.isEmpty():
            return None
        else:
            ret = self[-1]
            del(self[-1])
            return ret

    
if __name__ == "__main__":
    a = Stack()
    
    a.push(1)
    a.push(2)
    a.push(3)
    a.push(4)
    a.push(5)
    
    
    
    if a.isEmpty():
        print("There is no data")
    else:
        while(not a.isEmpty()):
            print(a.pop(), end="  ")
            
#ADT만 준수하면 방법은 상관이 없다.


# In[ ]:




