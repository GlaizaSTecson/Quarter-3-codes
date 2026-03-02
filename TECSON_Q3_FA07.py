import numpy as np

names = ["Mia", "Ashie", "Glaiza"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

arr = np.array([
    [9000, 7800, 8600, 9800, 8700],
    [8400, 7500, 7900, 8500, 8200],
    [9600, 8300, 8700, 9800, 8900]
])

print("Daily steps taken from Monday to Friday:\n")

for i in range(len(names)):
    print(names[i], ":", arr[i])

print("\nTotal and Average Steps per Person:\n")

for i in range(len(names)):
    total = arr[i].sum()
    average = arr[i].mean()
    print(names[i], "- Total:", total, "| Average:", round(average, 2))

print("\nTotal Steps per Day:\n")

for j in range(len(days)):
    total = arr[:, j].sum()
    print(days[j], "total:", total)

print("\nMaximum steps recorded:", arr.max())

print("Minimum steps recorded:", arr.min())



Short response:
Using a 2D array makes it easier to organize the step data by person and by day in a clear structure. With loops and built-in functions, calculating totals and averages became fast and accurate without repeating code. Finding the maximum and minimum values is also simple because the array allowed direct access to all data immediately.
