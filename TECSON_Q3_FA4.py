names = ["Mia", "Ashie", "Glaiza"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday ", "Friday"]

steps = [
[9000, 7800, 8600, 9800, 8700],
[8400, 7500, 7900, 8500, 8200],
[9600, 8300, 8700, 9800, 8900]
]

totals = []
for i in range(len(steps)):
    total = sum(steps[i])
    totals.append(total)
    print(names[i], "total steps:", total)

highesttotal = max(totals)
lowesttotal = min(totals)

highestindex = totals.index(highesttotal)
highestname = names[highestindex]

print("\nPerson with the highest total steps:")
print(highestname, "-", highesttotal)

print("\nDifference between highest and lowest total:")
print(highesttotal - lowesttotal)
