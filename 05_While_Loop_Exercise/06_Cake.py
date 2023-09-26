cake_length = int(input())
cake_width = int(input())
cake_pieces = cake_width * cake_length

cake_pieces_count = 0
command = input()

while cake_pieces > cake_pieces_count:
    if command == "STOP":
        difference_pieces = cake_pieces - cake_pieces_count
        print(f"{difference_pieces} pieces are left." )
        break
    cake_pieces_count += int(command)
    if cake_pieces_count > cake_pieces:
        difference_pieces = cake_pieces_count - cake_pieces
        print(f"No more cake left! You need {difference_pieces} pieces more.")
        break
    command = input()
