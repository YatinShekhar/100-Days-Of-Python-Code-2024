# Exercise 5: Datatypes

two_digit_number = input()
print(int(two_digit_number[0]) + int(two_digit_number[1]))


# Exercise 6: BMI Calculator

height = input()
weight = input()
print(int(float(weight)/float(height)**2))


# Exercise 7: Life in Weeks

age = input()
total_weeks = 90 * 52
current_weeks = int(age) * 52
remaining_weeks = total_weeks - current_weeks 
print(f"You have {remaining_weeks} weeks left.")
