room_width = int(input())
room_length = int(input())
room_heigth = int(input())

room_space = room_width * room_length * room_heigth

boxes_count = 0

command = input()

while room_space > boxes_count:
    if command == "Done":
        free_space = room_space - boxes_count
        print(f"{free_space} Cubic meters left." )
        break
    boxes_count += int(command)
    if boxes_count > room_space:
        difference = boxes_count - room_space
        print(f"No more free space! You need {difference} Cubic meters more.")
        break

    command = input()
