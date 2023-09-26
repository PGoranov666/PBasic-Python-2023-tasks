start_range = int(input())
end_range = int(input())
magic_number = int(input())

found_combination = False
combination_number = 0

for num1 in range(start_range, end_range + 1):
    for num2 in range(start_range, end_range + 1):
        combination_number += 1
        if num1 + num2 == magic_number:
            print(f"Combination N:{combination_number} ({num1} + {num2} = {magic_number})")
            found_combination = True
            break

    if found_combination:
        break

if not found_combination:
    print(f"{combination_number} combinations - neither equals {magic_number}")
