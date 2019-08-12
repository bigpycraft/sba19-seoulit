# 삼각형1
for i in range(1, 10, 2):
    mark = "*" * i
    print(mark)

# 삼각형2
for i in range(1, 10, 2):
    mark = " " * int((10-i)/2) + "*" * i
    print(mark)