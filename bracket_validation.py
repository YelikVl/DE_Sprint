def valid_brackets(x):
    not_closed = []
    for char in x:
        if char == "(" or char == "{" or char == "[":
            not_closed.append(char)
        elif char == ")" and not_closed.pop() != "(":
            return False
        elif char == "]" and not_closed.pop() != "[":
            return False
        elif char == "}" and not_closed.pop() != "{":
            return False
    if len(not_closed) == 0:
        return True
    return False
