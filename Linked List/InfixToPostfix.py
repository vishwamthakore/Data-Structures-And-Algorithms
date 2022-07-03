from doctest import OutputChecker


expr = 'a+b*(c^d-e)^(f+g*h)-i'

# If next element is lower priority then pop (as prev needs to evaluate first)
# ( can be thought of as very low priority as any operator after this will be added to stack
# If ")" then pop and append operators till "(" 

def getPriority(operator):
    if operator in ["+", "-"]:
        return 1
    elif operator in ["*", "/"]:
        return 2
    elif operator in ["^"]:
        return 3
    elif operator in ["("]:
        return 0


def infixToPostfix(expr):
    output = ""
    operators = ["+", "-", "*", "/", "^"]
    brackets = ["(", ")"]
    stack = []

    for char in expr:
        if (char == "("):
            stack.append(char)
        elif (char == ")"):
            assert len(stack) > 0, "Invalid expression"

            while (stack[-1] != "("):
                assert len(stack) > 0, "Invalid expression"
                operator = stack.pop()
                output+=operator
            stack.pop()
        elif char in operators:
            currPriority = getPriority(char)
            while (len(stack)>0):
                prevPriority = getPriority(stack[-1])
                if prevPriority < currPriority:
                    break
                else:
                    output+=stack.pop()
            stack.append(char)
        else:
            output += char

    while (len(stack)>0):
        output+=stack.pop()
    return output


expr = 'a+b*(c^d-e)^(f+g*h)-i'
print(infixToPostfix(expr))

# Output
# abcd^e-fgh*+^*+i-