hour = int(input())
minute = int(input())

total_minutes = hour * 60 + minute

new_total_minutes = (total_minutes + 15) % (24 * 60)

new_hour = new_total_minutes // 60

new_minute = new_total_minutes % 60

print(f"{new_hour}:{new_minute:02}")
