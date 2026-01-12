import numpy as np
names = ["Mia", "Ashie", "Glaiza"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday ", "Friday"]
arr = np.array([
    [9000, 7800, 8600, 9800, 8700],
    [8400, 7500, 7900, 8500, 8200],
    [9600, 8300, 8700, 9800, 8900]
])

print("Daiy steps taken from Monday to Friday: ")

for i in range(len(names)):
    print(names[i], ":", arr[i])

print("\nTotal Steps per Day: \n")
for j in range(len(days)):
    total = arr[:, j].sum()
    print(days[j], "total:", total)


REFLECTION: 
1) I chose this dataset as I felt it would be the easiest to process and make. Furthermore, I feel like coding this would be very useful for personal use compared to the other given datasets. Other than that, I feel comfortable working with it.
2) A 2D array helps organize this kind of data by arranging it into rows and columns, making it easier to comprehend and analyse. Each row can represent a person, while each column represents a day, so the data is structured and easy to understand. It also allows quick access to specific values. In summary, a 2D array makes the data easier to manage, compare, and analyze.
