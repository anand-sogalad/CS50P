def calculator(operand1, operand2, operator):
    try:
        if isinstance(operand1, str) or isinstance(operand2, str):
            raise ValueError
        match operator:
            case "+":
                return operand1 + operand2
            case "-":
                return operand1 - operand2
            case "*":
                return operand1 * operand2
            case "/":
                return operand1 / operand2
            case "%":
                return operand1 % operand2
            case "**":
                return operand1 ** operand2
            case "//":
                return operand1 // operand2
    except ValueError:
        print("Error: string type operands not supported in calculator")
    except ZeroDivisionError:
        print(f"Error: operand2 can't be zero for {operator} operation")
    except TypeError:
        print(f"Error: un supported operands for {operator} operation")


def main():
    operand1 = int(input("Enter operand1: "))
    operand2 = int(input("Enter operand2: "))
    operator = input("Enter operator: ")
    result = calculator(operand1, operand2, operator)
    print(result)


if __name__ == "__main__":
    main()
