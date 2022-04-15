#1
##day la mot module##
"""
def square(n):
    return n*n
def cube(n):
    return n*n*n
def average(values):
    nvals = len(values)
    sum = 0.0
    for v in values:
        sum += v
    return float(sum)/nvals
"""
#1
"""
## My script using the math module ##
import mymath # Note no .py
values = [2,4,6,8,10]
print('Squares:')
for v in values:
    print(mymath.square(v))
print 'Cubes:'
for v in values:
    print(mymath.cube(v))
print('Average: ' + str(mymath.average(values)))
"""
#1
"""
import mymath as mt
print(mt.square(2))
print(mt.square(3))
"""
#2
"""
import datetime as dt
format = '%Y-%m-%dT%H:%M:%S'
t1 = dt.datetime.strptime('2008-10-12T14:45:52', format)
print('Day ' + str(t1.day))
print('Month ' + str(t1.month))
print('Minute ' + str(t1.minute))
print('Second ' + str(t1.second))
# Define todays date and time
t2 = dt.datetime.now()
diff = t2 - t1
print('How many days difference? ' + str(diff.days))
"""
#3
"""
import numpy as np
x = np.arange(12, 38)
print(x)
"""
#4
"""
orinary_list = [12,13, 14, 15 ,16 ,17 ,18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]
orinary_list.reverse()
print(orinary_list)
"""
#5

numlist = list(input("nhap list: "))
print(max(numlist))

print(min(numlist))

#6
#7
"""
import numpy as np
data_type = [('name', 'S15'), ('class', int), ('height', float)]
students_details = [('James', 5, 48.5), ('Nail', 6, 52.5),('Paul', 5,
42.10), ('Pit', 5, 40.11)]
"""
# create a structured array
"""
students = np.array(students_details, dtype=data_type)
print("Original array:")
print(students)
print("Sort by height")
print(np.sort(students, order='height'))
#9
Giải thuật kiếm nhị phan (Binary Search)
    A ← một mảng đã được sắp xếp
    n ← kích cỡ mảng
    x ← giá trị để tìm kiếm trong mảng
    gán lowerBound = 1
    gán upperBound = n
    while x not found
        if upperBound < lowerBound
            EXIT: x không tồn tại.
            
    gán midPoint = lowerBound + ( upperBound - lowerBound ) / 2
    
    if A[midPoint] < x
        gán lowerBound = midPoint + 1
    if A[midPoint] > x
        gán upperBound = midPoint - 1
    if A[midPoint] = x
        EXIT: x được tìm thấy tại midPoint
    kết thúc while
kết thúc giải thuật
"""






