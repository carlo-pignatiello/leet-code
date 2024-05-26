def valid_bracket(s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    stack = []
    for b in s:
        if b in "({[":
            stack.append(b)
        else:  # closing bracket
            if (
                not stack
                or (b == ")" and stack[-1] != "(")
                or (b == "}" and stack[-1] != "{")
                or (b == "]" and stack[-1] != "[")
            ):
                return False
            stack.pop()
    return not stack


res = valid_bracket("()[]{ss}")
print(res)
