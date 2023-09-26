open_browser_tabs = int(input())
salary = float(input())

#  "Facebook" -> 150 лв.
# •	"Instagram" -> 100 лв.
# •	"Reddit" -> 50 лв.
penalty = 0

for _ in range(open_browser_tabs):
    browser = input()
    if browser == "Facebook":
        penalty += 150
        if penalty >= salary:
            print(f"You have lost your salary.")
            break
    elif browser == "Instagram":
        penalty += 100
        if penalty >= salary:
            print(f"You have lost your salary.")
            break
    elif browser == "Reddit":
        penalty += 50
        if penalty >= salary:
            print(f"You have lost your salary.")
            break
if salary > penalty:
    rest = salary - penalty
    print(f"{int(rest)}")





