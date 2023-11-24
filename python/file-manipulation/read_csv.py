import csv

with open("nobel-prize-winners.csv", "r") as f:
    reader = csv.DictReader(f)
    nobelPrizeWinners = list(reader)

for winner in nobelPrizeWinners:
    if winner["Full Name"] == "Albert Einstein":
        print(winner)