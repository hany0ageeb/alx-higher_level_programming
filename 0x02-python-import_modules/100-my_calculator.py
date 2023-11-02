#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def exec_operator(a, b, operator):
        import calculator_1 as calc
        result = None
        if operator == "+":
            result = calc.add(a, b)
        elif operator == "-":
            result = calc.sub(a, b)
        elif operator == "*":
            result = calc.mul(a, b)
        elif operator == "/":
            result = calc.div(a, b)
        return result
    length = len(sys.argv)
    if (length != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operators = ["+", "-", "*", "/"]
    operator = sys.argv[2]
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    result = exec_operator(a, b, operator)
    print("{} {} {} = {}".format(a, operator, b, result))
