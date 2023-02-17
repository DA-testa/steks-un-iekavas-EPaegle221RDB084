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
                return i + 1
            opening_brackets_stack.pop()

    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    else:
        return "Success"
    
def main():

    # text = input().strip()
    # mismatch = find_mismatch(text)

    input_type = input()

    if input_type == "F":
        file_name = input()
        with open(file_name) as f:
            text = f.read().strip()
        mismatch = find_mismatch(text)
    elif  "I" in input_type:
        text = input().strip()
        mismatch = find_mismatch(text)
    else:
        print("Invalid input type.")
        return

    if mismatch == "Success":
        print("Success")
    else:
        print(mismatch)

if __name__ == "__main__":
    main()
