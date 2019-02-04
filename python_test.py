# for any given array of integers, find where array contains numbers 1, 3 and 4 in the following order: 1,3,4

some_array1 = [0,2,3,4,5,6,7,8,9,10,11,12,1,3,4,13,14,1,2,3,4,1,3,4,0,0,0,1,3,3,1,3,4,0]
result1 = "False"
counter1 = -1

some_array2 = [0,2,3,5,6,7,8,9,10,11,12,1,3,13,14,1,2,3,1,3,0,0,0,1,3,3,1,3,0]
result2 = "False"
counter2 = 0

for i in some_array1:
    if (i == 1 and some_array1[some_array1.index(i)+1] == 3 and some_array1[some_array1.index(i)+2] == 4):
        counter1 += 1
        result1 = "True"
        continue
    else:
        continue

print(result1)
print "Result: array of 1,3,4 found roughly " + str(counter1) + " times in some_array1"

for i in some_array2:
    if (i == 1 and some_array2[some_array2.index(i)+1] == 3 and some_array2[some_array2.index(i)+2] == 4):
        counter2 += 1
        result2 = "True"
        continue
    else:
        continue

print(result2)
print "Result: array of 1,3,4 found roughly " + str(counter2) + " times in some_array2"
