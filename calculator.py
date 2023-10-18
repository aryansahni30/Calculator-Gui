#Author Name - Aryan Sahni
#Date -05/12/2023
#file - calculator.py
#Description - calculator that will convert a command from infix to postfix

from stack import Stack
from tree import BinaryTree, ExpTree


def infix_to_postfix(infix):
    prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # precedence of operators
    oper = set(['+', '-', '*', '/', '(', ')', '^'])  # operators
    stack = []  # stack
    infix.replace(" ", "")  # removes spaces
    postfix = ''  # postfix
    skip = None
    enum = enumerate(infix)
    for j, char in enum:
        if not skip == None:
            if skip > j:
                continue
        if char not in oper:  # checks if char is an operator
            numb, sval = numbers_in_infix(infix[j:])  # checks if the next char is a number and if it is it will add it to the postfix
            skip = sval + j
            postfix += numb + " "
        elif char == '(':  # checks for left parathese
            stack.append('(')  # adds to stack
        elif char == ')':  # checks for right parathese
            # adds to postfix until it finds a left parathese
            while (stack and stack[-1] != '('):
                postfix += stack.pop() + " "
            stack.pop()
        else:
            while (stack and stack[-1] != '(') and (prec[char] <= prec[stack[-1]]):
                postfix += stack.pop() + " "
            stack.append(char)
    while stack:
        postfix += stack.pop() + " "
    return postfix[:-1]


def numbers_in_infix(init_infix):
    numbers = []
    for i in range(len(init_infix)):
        if init_infix[i].isdigit() or init_infix[i] == ".":
            numbers.append(init_infix[i])
            continue
        else:
            break
    nums = "".join(numbers)
    lennums = len(numbers)
    return nums, lennums


def calculate(infix):  # calculates the value of the infix expression

    postfix = infix_to_postfix(infix).split()  # converts infix to postfix
    value = ExpTree.make_tree(postfix)  # makes a tree with the postfix expression
    returnval = float(ExpTree.evaluate(value))  # evaluates the tree

    return returnval


# a driver to test calculate module
if __name__ == '__main__':
   
    print("Welcome to Calculator Program!")
    while True:
        inputvalue = input("Please enter your expression here. To quit enter 'quit' or 'q':\n")
        if inputvalue.upper() == "Q" or inputvalue.upper() == "QUIT":
            print("Goodbye!")
            break
        else:
            print(calculate(inputvalue))


    assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    assert infix_to_postfix('5+2*3') == '5 2 3 * +'
    # test calculate function
    assert calculate('(5+2)*3') == 21.0
    assert calculate('5+2*3') == 11.0



