
# coding: utf-8

# In[3]:

from calculator_body import Calculator_body
while True:
    print("#" * 25)
    print("Postfix Calculator!!")
    print("#" * 25)
    print("\n")
    
    exp = input("Input Expression : ")
    a = Calculator_body(exp)
    print("\nYour Expression to Postfix is")
    for i in a.get_postfix_exp_list():
        print(i, end = " ")
    print("\n")
    print("The Result is : {}".format(a.get_result()))

    print("END!!\n\n")
        
    


# In[ ]:



