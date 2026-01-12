names = ["Mia", "Ashie", "Glaiza"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday ", "Friday"]

steps = [
[9000, 7800, 8600, 9800, 8700],
[8400, 7500, 7900, 8500, 8200],
[9600, 8300, 8700, 9800, 8900]
]

totals = []
for person_steps in steps:
    totals.append(sum(person_steps))

highesttotal = max(totals)
lowesttotal = min(totals)

highestindex = totals.index(highesttotal)
highestname = names[highestindex]

print("Total steps:", totals)
print("Highest total steps:", highestname, "-", highesttotal)
print("Difference between highest and lowest:", highesttotal - lowesttotal)
