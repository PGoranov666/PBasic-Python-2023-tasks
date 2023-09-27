floors_number = int(input())
rooms_number = int(input())

floor_letter = ""

for current_floor in range(floors_number, 0, -1):
    if current_floor == floors_number:
        floor_letter = "L"
    elif current_floor % 2 == 0:
        floor_letter = "O"
    else:
        floor_letter = "A"
    for current_room in range(rooms_number):
        print(f"{floor_letter}{current_floor}{current_room}", end = " ")
    print()
