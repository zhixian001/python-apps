
# coding: utf-8

# In[2]:

#parser
def str_into_sequential_list(expression):
    operator = ('*', '/', '+', '-', '(', ')', '^')
    nums = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    result = []
    temp = ""
    for s in expression:
        if s in nums:
            temp = temp + s
        
        else:
            if len(temp) != 0:
                result.append(eval(temp))
                temp = ""
            if s in operator:
                result.append(s)
            elif s == " ":
                pass
    if len(temp) != 0:
        result.append(eval(temp))
        
    return result

if __name__ == "__main__":
    exp = input("input expression : \n")
    exp_list = str_into_sequential_list(exp)
    print(exp_list)
            


# In[ ]:



