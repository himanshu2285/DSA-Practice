import sys

top = -1
size = 6
stack = [None]*size # hashmap

while True:
    print('''
        1. Push into stack
        2. Pop from stack
        3. Display stack
        4. Exit''')
    
    try: 
        operation = eval(input("Choose a operation : "))
        match operation:
            case 1: # push opn
                if top==size-1:
                    print("Stack is full, Stack overflow condition")
                else:
                    number = int(input("Enter the number to insert : "))
                    top += 1
                    stack[top]=number
                    print("Inserted successfully")
            
            case 2: #pop opn
                if top == -1:
                    print("Stack is empty, Underflow condition")
                else:
                    data = stack[top]
                    stack[top] = None
                    top -= 1
                    print(f"{data} deleted successfully from stack")
            
            case 3:
                if top == -1:
                    print("stack is empty")
                else:
                    print(f"Stack : {stack}")
            
            case 4:
                print("Exiting...")
                sys.exit()
                
            case _:
                print("Enter valid option.")
    
    except NameError as e:
        print("I think! you have entered wrong option {e}")