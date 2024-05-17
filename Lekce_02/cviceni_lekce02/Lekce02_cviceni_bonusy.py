# s = [6,6,6,]

# stred_index = len(s) // 2 
# stred = s[stred_index]
# print("Střed s:", stred)

# s1 = [1, 2, 3, 4, 5]
# s2 = [10, 20, 30, 40]
# s3 = [2, 4, 6, 8, 10, 12]

# stred_s1 = s1[len(s1) // 2]
# print("Střed s1:", stred_s1)

# stred_s2 = s2[len(s2) // 2]
# print("Střed s2:", stred_s2)

# stred_s3 = s3[len(s3) // 2]
# print("Střed s3:", stred_s3)

s = [6, 4, 10]
if len(s) % 2 == 0:
    stred_index = len(s) // 2 - 1
else:
    stred_index = len(s) // 2
    
stred = s[stred_index]
print("Střed:", stred)

s1 = [1, 2, 3, 4, 5]
s2 = [10, 20, 30, 40]
s3 = [0, 2, 6, 5, 4, 3]

if len(s1) % 2 == 0:
    stred_index_s1 = len(s1 // 2 - 1)
else:
    stred_index_s1 = len(s1) // 2
stred_s1 = s1[stred_index_s1]
print("Střed s1:", stred_s1)

if len(s2) % 2 == 0:
    stred_index_s2 = len(s2) // 2 - 1
else:
    stred_index_s2 = len(s2) // 2
stred_s2 = s2[stred_index_s2]
print("Střed s2:", stred_s2)

if len(s3) % 2 == 0:
    stred_index_s3 = len(s3) // 2 - 1
else:
    stred_index_s3 = len(s3) // 2
stred_s3 = s3[stred_index_s3]
print("Střed s3:", stred_s3)

