import math

tournamets = int(input())
string_points = int(input())

win_points = 0
wins = 0
for _ in range(tournamets):
    tournamet_phase = input()
    if tournamet_phase == "W":
        wins += 1
        win_points += 2000
    elif tournamet_phase == "F":
        win_points += 1200
    elif tournamet_phase == "SF":
        win_points += 720

avg_points = math.floor(win_points / tournamets)
wins_percent = wins / tournamets * 100

print(f"Final points: {string_points + win_points}")
print(f"Average points: {avg_points}")
print(f"{wins_percent :.2f}%")
