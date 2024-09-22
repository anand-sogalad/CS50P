def main():
    expression = get_user_input()
    result = evaluate_expression(expression)
    print(result)


def get_user_input():
    return input("Expression: ").strip()


def evaluate_expression(expr):
    return float(eval(expr))


if __name__ == "__main__":
    main()
