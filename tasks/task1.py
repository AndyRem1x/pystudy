name = "Andrew"
day = "Friday"
print(f"Good day {name}! {day} is a perfect day to learn some python.")  # way 1
print("Good day {0}! {1} is a perfect day to learn some python.".format(name, day))  # way2
print("Good day %s! %s is a perfect day to learn some python." % (name, day))  # way 3
