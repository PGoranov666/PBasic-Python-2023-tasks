n1 = int(input())
n2 = int(input())
operator = input()

result = 0
is_even = False

if operator == "+":
    result = n1 + n2
    is_even = result % 2 == 0
    print(f"{n1} {operator} {n2} = {result} - {'even' if is_even else 'odd'}")

elif operator == "-":
    result = n1 - n2
    is_even = result % 2 == 0
    print(f"{n1} {operator} {n2} = {result} - {'even' if is_even else 'odd'}")
elif operator == "*":
    result = n1 * n2
    is_even = result % 2 == 0
    print(f"{n1} {operator} {n2} = {result} - {'even' if is_even else 'odd'}")
elif operator == "/":
    if n2 != 0:
        result = n1 / n2
        print(f"{n1} {operator} {n2} = {result:.2f}")
    else:
        print(f"Cannot divide {n1} by zero")
elif operator == "%":
    if n2 != 0:
        result = n1 % n2
        print(f"{n1} % {n2} = {result}")
    else:
        print(f"Cannot divide {n1} by zero")
