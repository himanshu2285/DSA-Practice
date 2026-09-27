import sys

n = 5
st = [None] * n
top = -1

while True:
    print('\n1. Push')
    print('2. Pop')
    print('3. Display')
    print('4. Exit')
    
    try:
        num = int(input("Choose Operation : "))

        match num:
            case 1:
                if top == n-1:
                    print("Stack is already full, OverFlow condition!")
                else:
                    data = int(input("Enter value to push : "))
                    top += 1
                    st[top] = data
                    print("Inserted succesfully")
            
            case 2:
                if top == -1:
                    print("Stack is empty, Underflow condition!")
                else:
                    data = st[top]
                    st[top] = None
                    top -= 1
                    print(data, "Successfully removed.")
            
            case 3:
                if top == -1:
                    print("stack is empty, can't display elements")
                else:
                    print("Stack : ",st)
            
            case 4:
                print("Exiting...")
                sys.exit()
            
            case _:
                print("Choose valid option")
    
    except Exception:
        print("Operation terminated! Not choose valid options")
        sys.exit()