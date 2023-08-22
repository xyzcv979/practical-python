# bounce.py
#
# Exercise 1.5

height = 60
for i in range(10):
    print(i, ' ', height)
    height *= .6
    height = round(height, 4)