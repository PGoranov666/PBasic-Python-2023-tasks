count_of_numbers = int(input())
even_sum = 0
odd_sum = 0
for numbers in range(1, count_of_numbers +1):
    num = int(input())
    if numbers % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    diff = abs(even_sum - odd_sum)
    print("No")
    print(f"Diff = {diff}")
