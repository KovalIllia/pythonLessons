def sum(a, b):
    result = int(a + b)
    # print(f"Sum of this values: {result}")
    return result

def difference(a, b):
    result = int(a - b)
    # print(f"Difference of this values: {result}")
    return result

def multiplication(a, b):
    result = int(a * b)
    # print(f"Result of multiplication of this values: {result}")
    return result

def division(a, b):
    try:
        result = int(a / b)
        # print(f"Result of division of this values: {result}")
        return result
    except ZeroDivisionError:
        print("Invalid operation!")
        return 0

