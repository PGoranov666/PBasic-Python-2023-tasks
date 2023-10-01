total_tickets = 0
command = input()

student_tickets = 0
standard_tickets = 0
kid_tickets = 0
while not command == "Finish":
    current_movie = command
    total_seats = int(input())
    available_seats = total_seats

    while available_seats > 0:
        current_ticket_type = input()

        if current_ticket_type == "End":
            break
        available_seats -= 1
        if current_ticket_type == "student":
            student_tickets += 1
        elif current_ticket_type == "standard":
            standard_tickets += 1
        elif current_ticket_type == "kid":
            kid_tickets += 1

    seats_bought = total_seats - available_seats
    total_tickets += seats_bought

    percentage_full = seats_bought / total_seats * 100
    print(f"{current_movie} - {percentage_full :.2f}% full.")

    command = input()

percent_students = student_tickets / total_tickets * 100
percent_standard = standard_tickets / total_tickets * 100
percent_kid = kid_tickets / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{percent_students :.2f}% student tickets.")
print(f"{percent_standard :.2f}% standard tickets.")
print(f"{percent_kid :.2f}% kids tickets.")
