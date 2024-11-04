#use graphics.py
from graphics import *

class myStack:
    
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def top(self):
        return self.items[-1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

"""
infix means x+3
postfix means x3+

no error checking necessary 

supports 0-9, x, +, -, /, *, ()

for loops only support integers, ex cannot be like 0-10 by 0.1
""" 
#stack class does not check if there is already -
#something on the stack, so you have to check - 
#before using like s.top() or itll break

def infixToPostfix(infix):
    s = myStack()
    numbers = "0123456789x"
    postfix = ""
    for char in infix:
        #0-9 and x immediately go to postfix string
        if char in numbers:
            postfix += char

        #* & / are priority
        if char in "*/":
            #pop */ off the stack to postfix 
            while not s.isEmpty() and s.top in "*/":
            #^check if stack empty so s.top doesn't break it
                postfix += s.pop()
            #adding new to stack
            s.push(char)

        if char in "+-":
            while not s.isEmpty() and s.top in "*/+-":
                                        #+- have no priority
                postfix += s.pop()
            s.push(char)
        #after move everything from stack to the postfix string
            
        if char == "(":
           s.push(char)

        if char == ")":
            while s.top() != "(":
                postfix += s.pop()
            s.pop() #get rid of left paren cause we DONT NEED IT
    return postfix

def evaluatePostFix(postfix, x_value):
    s = myStack()
    for char in postfix:
        if char.isdigit():
            s.push(int(char))
        elif char == 'x':
            s.push(x_value)
        else:
            right = s.pop()
            left = s.pop()
            if char == '+':
                s.push(left + right)
            elif char == '-':
                s.push(left - right)
            elif char == '*':
                s.push(left * right)
            elif char == '/':
                s.push(left / right)
    return s.pop() 

def plotGraph(expression):
    win = GraphWin("Graph of " + expression, 600, 600)
    win.setBackground("white")

    x_axis = Line(Point(0, 300), Point(600, 300))
    x_axis.setWidth(2)
    x_axis.draw(win)
    y_axis = Line(Point(300, 0), Point(300, 600))
    y_axis.setWidth(2)
    y_axis.draw(win)

    for x in range(-10, 11): 
        postfix = infixToPostfix(expression)
        y = evaluatePostFix(postfix, x)
        
        pixel_x = 300 + x * 20 
        pixel_y = 300 - y * 20
        
        point = Point(pixel_x, pixel_y)
        point.setFill("red")
        point.draw(win)

    win.getMouse()
    win.close()

def main():
    expression = input("Enter a valid expression (ex: x*x*x/(2*5)): ")
    plotGraph(expression)

if __name__ == "__main__":
    main()