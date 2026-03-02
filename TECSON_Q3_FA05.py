names = ["Mia", "Ashie", "Glaiza"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday ", "Friday"]

steps = [
[9000, 7800, 8600, 9800, 8700],
[8400, 7500, 7900, 8500, 8200],
[9600, 8300, 8700, 9800, 8900]
]

totalperday = []

for dayindex in range(len(days)):
    daytotal = 0
    for personsteps in steps:
        daytotal += personsteps[dayindex]
    totalperday.append(daytotal)
    print(days[dayindex], "total steps:", daytotal)

maxsteps = max(totalperday)
maxindex = totalperday.index(maxsteps)
mostactiveday = days[maxindex]

print("\nMost active day overall:")
print(mostactiveday, "-", maxsteps, "steps")
