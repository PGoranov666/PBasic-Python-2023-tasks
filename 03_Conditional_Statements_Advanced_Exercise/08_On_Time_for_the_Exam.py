exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time = exam_hour * 60 + exam_minute
arrival_time = arrival_hour * 60 + arrival_minute
difference = arrival_time - exam_time

if difference < -30:
    print("Early")
    hours = abs(difference) // 60
    minutes = abs(difference) % 60
    if hours > 0:
        print(f"{hours}:{minutes:02d} hours before the start")
    else:
        print(f"{minutes} minutes before the start")
elif difference <= 0:
    print("On time")
    if difference < 0:
        print(f"{abs(difference)} minutes before the start")
else:
    print("Late")
    hours = difference // 60
    minutes = difference % 60
    if hours > 0:
        print(f"{hours}:{minutes:02d} hours after the start")
    else:
        print(f"{abs(minutes)} minutes after the start")
