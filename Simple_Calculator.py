import math

def parse_number(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            raise ValueError("Inputs must be valid numbers")

def Simple_Calculator(x,y,z):
    match z:
        case '+':
            return x + y
        case '-':
            return x - y
        case '*':
            return x * y
        case '/':
            if y == 0:
                raise ZeroDivisionError("Your Value Not to be Zero, Divide by Zero is not possible")
            return x / y
        case '%':
            return x % y
        case '^':
            return math.pow(x, y)
        case '//':
            return x // y
        case 'log()':
            return math.log(x, y)


def Simple_calculator_1(x,z):
    match z:
        case 'ceil':
            return math.ceil(x)
        case 'sqrt':
            return math.sqrt(x)
        case 'log':
            return math.log(x)
        case 'fact':
            return math.factorial(x)
        case 'sin':
            return math.sin(x)
        case 'cos':
            return math.cos(x)
        case 'tan':
            return math.tan(x)

def Simple_Calculator_2(x,z):
    match z:
        case '+':
            return  result+ x
        case '-':
            return result- x
        case '*':
            return result*x
        case '/':
            if x == 0:
                raise ZeroDivisionError("Your Value Not to be Zero, Divide by Zero is not possible")
            return result/x


while True:
    try:
        print("-----Welcome To Mini Calculator-----")
        Binary_Operators = ['+', '-', '/', '%', '*', '^', 'ceil', '//', 'log()']
        Unary_Operators = ['sqrt', 'log', 'ceil', 'sin', 'cos', 'tan', 'fact']

        print(Binary_Operators)
        print(Unary_Operators)
        z = input("Enter Operator: ")


        if z in Binary_Operators:
            x=input("Enter Your First Number: ")
            y=input("Enter Your Second Number: ")
            x=parse_number(x)
            y=parse_number(y)

            result=(Simple_Calculator(x,y,z))
            print(result)

            while True:
                print("Do you want to continue? (y/n)")
                A = input("Enter Your Choice: ")
                if A == 'y':
                    z = input("Enter Operator: ")
                    if z in Binary_Operators:
                        x = input("Enter your next Number: ")
                        x = parse_number(x)
                        result_1=Simple_Calculator_2(x, z)
                        print(result_1)
                    else:
                        raise TypeError("Give Correct Operator")
                    # break
                elif A=='n':
                    break

                # else:
            print(f"Your Output is : {result_1}")
            print("-----Your Output Ready-----")
                # break
            # print("-----Your Output Ready-----")
        elif z in Unary_Operators:
            x=input("Enter Your Number: ")
            x=parse_number(x)
            print(Simple_calculator_1(x,z))
            print("-----Your Output Ready-----")
        else:
            raise TypeError("Give Correct Operator")
        break
    except ValueError as Ve:
        print(f"Enter Valid Input1: {Ve}")
    except ZeroDivisionError as ZDiv:
        print(f"Enter Valid Input2: {ZDiv}")
    except TypeError as Ty:
        print(f"Enter Valid Input3: {Ty}")






