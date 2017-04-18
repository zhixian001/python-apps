
# coding: utf-8

# In[51]:

#will apply cache algorithm
from parser import str_into_sequential_list
from stack_listbase import Stack

class Calculator_body:
    
    @classmethod
    def operator_weight(cls, char):
        if char in ["^"]:
            return 5
        elif char in ["*", "/"]:
            return 4
        elif char in ["+", "-"]:
            return 3
        elif char == "(":
            return 2
        elif char == ")":
            return 1
        #if stack pop or stack peek return None
        elif char == None:
            return 0
    
    
    def __init__(self, expression):
        self.expression = expression
        self.stack = Stack()
        self.original_exp_list = None
        self.postfix_exp_list = None
        self.result = None
        self.cache = {}
    
    def get_original_exp_list(self):
        if 'original_exp_list' not in self.cache:
            self.original_exp_list = str_into_sequential_list(self.expression)
            self.cache['original_exp_list'] = self.original_exp_list
            return self.cache['original_exp_list']
        else:
            return self.cache['original_exp_list']
        
    def get_postfix_exp_list(self):
        if 'postfix_exp_list' not in self.cache:
            self.postfix_exp_list = []
            for char in self.get_original_exp_list():
                #operator case
                if type(char) is int:
                    self.postfix_exp_list.append(char)
                else:
                    weight = Calculator_body.operator_weight(char)
                    
                    ############################NEW. '^' case###################################
                    if weight == 5:
                        stack_top_weight = Calculator_body.operator_weight(self.stack.peek())
                        #pop peek and push
                        if stack_top_weight > 4:
                            self.postfix_exp_list.append(self.stack.pop())
                            self.stack.push(char)
                        #just push
                        elif stack_top_weight <= 4:
                            self.stack.push(char)
                    ##############################################################################
                    
                    # '*' '/' case : stack if peek is None,'(' pop peek and push this if peek is '*', '/'
                    elif weight == 4:
                        stack_top_weight = Calculator_body.operator_weight(self.stack.peek())
                        #pop peek and push
                        if stack_top_weight > 3:
                            self.postfix_exp_list.append(self.stack.pop())
                            self.stack.push(char)
                        #just push
                        elif stack_top_weight <= 3:
                            self.stack.push(char)

                    # '+', '-' case : stack if peek is None, '(' , pop peek and push this if peek is '*', '/', '+', '-'
                    elif weight == 3:
                        stack_top_weight = Calculator_body.operator_weight(self.stack.peek())
                        #pop peek and push
                        if stack_top_weight > 2:
                            self.postfix_exp_list.append(self.stack.pop())
                            self.stack.push(char)
                        #just push
                        elif stack_top_weight <= 2:
                            self.stack.push(char)

                    # '(' case : force stack
                    elif weight == 2:
                        self.stack.push(char)

                    # ')' case : pop and save to list until '('
                    elif weight == 1:
                        temp = self.stack.pop()
                        while True:
                            self.postfix_exp_list.append(temp)
                            temp = self.stack.pop()
                            if temp == "(":
                                break
            #stack FLUSH
            if not self.stack.isEmpty():
                self.postfix_exp_list.append(self.stack.pop())
                while True:
                    if self.stack.isEmpty():
                        break
                    else:
                        self.postfix_exp_list.append(self.stack.pop())
            
            self.cache['postfix_exp_list'] = self.postfix_exp_list
            
            return self.cache['postfix_exp_list']
                        
        else:
            return self.cache['postfix_exp_list']
                        
            
                    
                                    
    def get_result(self):
        if 'result' not in self.cache:
            for i in self.get_postfix_exp_list():
                
                ###########NEW############
                if i == "^":
                    a = (self.stack.pop())
                    b = (self.stack.pop())
                    self.stack.push(b ** a)
                ###########################
                
                elif i == "+":
                    a = (self.stack.pop())
                    b = (self.stack.pop())
                    self.stack.push(b + a)
                elif i == "-":
                    a = (self.stack.pop())
                    b = (self.stack.pop())
                    self.stack.push(b - a)
                elif i == "*":
                    a = (self.stack.pop())
                    b = (self.stack.pop())
                    self.stack.push(b * a)
                elif i == "/":
                    a = (self.stack.pop())
                    b = (self.stack.pop())
                    self.stack.push(b / a)
                else:
                    self.stack.push(i)

            self.result =  self.stack.pop()
            self.cache['result'] = self.result

            #print("\nResult is : {}".format(self.result))

            return self.cache['result']
        else:
            return self.cache['result']
        
if __name__ == "__main__":
    syx = "(2+3)*3*(1/2)"
    a = Calculator_body(syx)

    a.get_original_exp_list()
    a.get_postfix_exp_list()
    a.get_result()
    print(a.get_result())
    print(a.cache)
    
    b = Calculator_body("3 + 2")
    print(b.get_result())
    




