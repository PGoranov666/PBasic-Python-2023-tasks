import math
serial_name = str(input())
episode_timing = int(input())
break_time = int(input())

lunch_time = break_time * 0.125
chill_time = break_time * 0.25

break_time_left = break_time - lunch_time - chill_time

if episode_timing <= break_time_left:
    remaining_time = math.ceil(break_time_left - episode_timing)
    print(f"You have enough time to watch {serial_name} and left with {remaining_time} minutes free time.")
else:
    necessary_time = math.ceil(episode_timing - break_time_left)
    print(f"You don't have enough time to watch {serial_name}, you need {necessary_time} more minutes.")
