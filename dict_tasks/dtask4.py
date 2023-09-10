days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
days_dict = {number + 1: day for number, day in enumerate(days)}
reverse_dict = {number: day for day, number in days_dict.items()}
print(days_dict)
print(reverse_dict)
