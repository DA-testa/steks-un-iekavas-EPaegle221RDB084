# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return left + right in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i + 1))
        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                #next != {'(': ')', '{': '}', '[': ']'}[opening_brackets_stack[-1][0]]:
                return i + 1
            opening_brackets_stack.pop()\

    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    else:
        return "Success"

def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == "Succcess":
        print("Success")
    else:
        print(mismatch)

if __name__ == "__main__":
    main()
