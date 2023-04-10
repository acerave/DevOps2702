a = ["daniel", "shai", "roei"]
if a[0] == "asaf" or a[1] == "asaf" or a[2] == "asaf":
    print("found asaf")

if "asaf" in a:
    print("found asaf")

first_array = []
second_array = [1, 2, 3]
if not first_array:
    print("first has no items")
if second_array:
    print("second_array has items")
print(len(second_array))
if len(second_array) > 2:
    print("we have at least 3 items in second")

d = "aviel"
g = "aviel"
g = "moshe"
g = "aviel"
f = [1, 2, 3]
h = [1, 2, 3]
if f is h:
    print(d is g)
if type(d) is int:
    print("d is int")

