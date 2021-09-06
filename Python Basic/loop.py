# print '0,1,2,3,4,5,6,7,8,9'
for i in range(10):
    print(i)

# for loop
# print 't,e,s,t,A,B,C'
for letter in "testABC":
    print(letter)

# print 'A1,A2,A3,B1,B2,B3,C1,C2,C3'
for letter in "ABC":
    for i in range(3):
        print(letter + str(i+1))

# while loop
# print '1,2,3,4,5'
w = 0
while w < 5:
    w = w + 1
    print(w)

# break
# print '1,2,3,4,5'
for i in range(10):
    if i == 5:
        break
    print(i+1)

# continue
# print '2,4,6,8,10'
for i in range(10):
    if i % 2 == 0:
        continue
    print(i+1)
