from utilities import get_lines_from_file

calorie_list = get_lines_from_file()

max_calories = 0
sub_total_calories = 0
for calorie in calorie_list:
    if calorie.isnumeric():
        sub_total_calories += int(calorie)
    else:
        max_calories = max(max_calories, sub_total_calories)
        sub_total_calories = 0

print(max_calories)
# 68442
