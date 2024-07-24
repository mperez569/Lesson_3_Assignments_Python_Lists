#1. Python List Transformation
#Task 1: Given the list of grades:
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse = True)
print(grades)

#Task 2: Calculate the average grade and print it.
sum_grades = sum(grades)
avg_grade = sum_grades / len(grades)
print("The average grade is: " + str(avg_grade))

#2. Advanced List Methods and Identity Operators
#Task 1: Given the two lists:
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
if "Alice" in submitted and "Alice" in attended:
  print("Alice subitted the assignment AND went to the last class")
else:
  print("Alice didn't do one or the other")

#3. Advanced Slicing Techniques
#Task 1: Given the list of temperatures:
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
second_week = temperatures[7:14]
print(second_week)

#Task 2: Extract all the temperatures above 100. HINT: add the temperatures over 100 to a new list, or use list slicing to get the temperatures.
above_100 = []
above_100.append(temperatures[-6:len(temperatures)])
print(above_100)
