# python3
# Arvīds Toms Spūlis 221RDB160

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):

        if next in "([{":
            if next in "(":
                opening_brackets_stack.append(1)
            if next in "[":
                opening_brackets_stack.append(2)
            if next in "{":
                opening_brackets_stack.append(3)

        if next in ")]}":
            if len(opening_brackets_stack)>0:
                if next in ")" and opening_brackets_stack[len(opening_brackets_stack) - 1]==1:
                    opening_brackets_stack.pop()
                elif next in "]" and opening_brackets_stack[len(opening_brackets_stack) - 1]==2:
                    opening_brackets_stack.pop()
                elif next in "}" and opening_brackets_stack[len(opening_brackets_stack) - 1]==3:
                    opening_brackets_stack.pop()
                else:
                    return i+1
            else:
                
                return i+1          
    if len(opening_brackets_stack)>0:
        return i+1


def main():
    text = input()
    if text == "I":
        text2 = input()
    else:
        text2 = input()
    mismatch = find_mismatch(text2)
    # Printing answer, write your code here
    if mismatch is None:
        print("Success")
    else:
        print(mismatch)
if __name__ == "__main__":
    main()
