#Fish Tank
leigth = int(input())
width = int(input())
heigth = int(input())
percentage_of_occupied_space = float(input())

volume_cubic_centimeters = leigth * width * heigth
volume_liters = volume_cubic_centimeters * 0.001
occupied_space = percentage_of_occupied_space / 100

liters_needed = volume_liters * (1-occupied_space)

print(liters_needed)