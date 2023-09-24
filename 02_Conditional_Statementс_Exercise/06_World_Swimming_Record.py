import math

record_seconds = float(input())
distance_meters = float(input())
seconds_per_meter = float(input())

total_time = distance_meters * seconds_per_meter

numbers_of_slowdown = math.floor(distance_meters / 15)

slowdown_time = numbers_of_slowdown * 12.5

total_time += slowdown_time

if total_time < record_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    missing_seconds = total_time - record_seconds
    print(f"No, he failed! He was {missing_seconds:.2f} seconds slower.")
