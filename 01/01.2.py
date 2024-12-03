list1 = []
list2 = []
first = True

with open('01/input_01', 'r') as input:
    for line in input:
        values = line.strip().split()
        list1.append(values[0])
        list2.append(values[1])

    similarity = 0
    for i in range(len(list1)):
        times = 0
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                times += 1
        similarity += int(list1[i]) * times

print(similarity)
print("Left list: ")
print(list1)
print("----------------------------------------")
print("Right list: ")
print(list2)
