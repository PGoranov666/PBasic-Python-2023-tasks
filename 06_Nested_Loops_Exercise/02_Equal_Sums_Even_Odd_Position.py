num_1 = int(input())
num_2 = int(input())

for number in range(num_1, num_2 +1):
    number_to_srt = str(number)
    even_sum = 0
    odd_sum = 0

    for index, digit in enumerate(number_to_srt):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if even_sum == odd_sum:
        print(number, end=' ')
