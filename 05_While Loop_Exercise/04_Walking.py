goal = 10000
total_steps = 0

while total_steps < goal:
    command = input()
    if command == "Going home":
        additional_steps = int(input())
        total_steps += additional_steps
        break

    steps = int(command)
    total_steps += steps

if total_steps >= goal:
    print("Goal reached! Good job!")
    print(f"{total_steps - goal} steps over the goal!")
else:
    diff = goal - total_steps
    print(f"{diff} more steps to reach goal.")
