# # task1
# n = input()
# k = 0
# ans = True
# for i in n:
#     if k < 0:
#         ans = False
#         break
#     if i == "(" or i == "<" or i == "{" or i == "[":
#         k += 1
#     else:
#         k -= 1

# if ans:
#     print("YES")
# else:
#     print("NO")

# #task2
# class MinStack:
#     def __init__(self):
#         self.stack = []
#         self.min_stack = []

#     def push(self, x):
#         self.stack.append(x)
#         if not self.min_stack or x <= self.min_stack[-1]:
#             self.min_stack.append(x)

#     def pop(self):
#         if self.stack:
#             top_element = self.stack.pop()
#             if top_element == self.min_stack[-1]:
#                 self.min_stack.pop()
#             return top_element
#         else:
#             return None

#     def get_min(self):
#         if self.min_stack:
#             return self.min_stack[-1]
#         else:
#             return None


# task 5
        
class StackMachine:
    def __init__(self):
        self.stack = []

    def num(self, x):
        self.stack.append(x)

    def pop(self):
        if self.stack:
            self.stack.pop()
        else:
            print("Stack is empty")

    def swp(self):
        if len(self.stack) >= 2:
            self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]
        else:
            print("Not enough elements in stack")

    def add(self):
        if len(self.stack) >= 2:
            self.stack.append(self.stack.pop() + self.stack.pop())
        else:
            print("Not enough elements in stack")

    def sub(self):
        if len(self.stack) >= 2:
            self.stack.append(self.stack.pop() - self.stack.pop())
        else:
            print("Not enough elements in stack")

    def mult(self):
        if len(self.stack) >= 2:
            self.stack.append(self.stack.pop() * self.stack.pop())
        else:
            print("Not enough elements in stack")

    def div(self):
        if len(self.stack) >= 2:
            divisor = self.stack.pop()
            if divisor != 0:
                self.stack.append(self.stack.pop() / divisor)
            else:
                print("Cannot divide by zero")
        else:
            print("Not enough elements in stack")

    def mod(self):
        if len(self.stack) >= 2:
            divisor = self.stack.pop()
            if divisor != 0:
                self.stack.append(self.stack.pop() % divisor)
            else:
                print("Cannot divide by zero")
   
            
stack_machine = StackMachine()


stack_machine.num(5)
stack_machine.num(10)

# Test addition
stack_machine.add()
print(stack_machine.stack)  
# Test swap
stack_machine.swp()
print(stack_machine.stack) 

# Test subtraction
stack_machine.sub()
print(stack_machine.stack) 

# Test multiplication
stack_machine.mult()
print(stack_machine.stack)

# Test division
stack_machine.num(2)
stack_machine.div()
print(stack_machine.stack) 

# test mod
stack_machine.mod()
print(stack_machine.stack)

# Test division by zero
stack_machine.num(0)
stack_machine.div() 

#BONUS 

stack_machine.num(5)
stack_machine.num(10)

