import sys
import operator


class Stack:
    # Define a stack class
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


# Define the valid operators
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}


def evaluate(expression):
    # Split the expression into tokens
    tokens = expression.split()

    stack = Stack()  # Create an empty stack

    # Process each token
    for token in reversed(tokens):
        if token.isdigit():
            # If the token is a number, push it onto the stack
            stack.push(int(token))
        elif token in ops:
            # If the token is an operator, pop the top two numbers from the stack,
            # apply the operator to them, and push the result back onto the stack
            arg1 = stack.pop()
            arg2 = stack.pop()
            if (token == '/' and arg2 == 0):
                return "Integer divide by zero!"
            result = ops[token](arg1, arg2)
            stack.push(result)

    # The final result is the only thing left on the stack
    return stack.pop()


def tokenize(expr):
    # turn expression into format handled by evaluate
    # the handled format is a string that contains only
    # digits and valid operators
    for i in expr:
        if i not in "1234567890+-/* ":
            expr = expr.replace(i, "")
    return expr


if __name__ == "__main__":
    expression = ""
    for i in sys.argv[1:]:
        expression += i + " "
    expression = tokenize(expression)

    print(expression)
    result = evaluate(expression)
    print(result)
