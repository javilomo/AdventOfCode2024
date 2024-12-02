import sys
def calculateDistance():
    list1 = []
    list2 = []
    first = True

    for line in sys.stdin:
        values = line.strip().split()
        
        if len(values) < 2:
            continue
        
        if first:
            list1.append(values[0])
            list2.append(values[1])
            first = False
        else:
            inserted = False
            for i in range(len(list1)):
                if values[0] < list1[i] and values[1] < list2[i]:  
                    list1.insert(i, values[0])
                    list2.insert(i, values[1])
                    inserted = True
                    break
            if not inserted: 
                list1.append(values[0])
                list2.append(values[1])

    distance = 0
    for i in range(len(list1)):
        distance += abs(int(list1[i]) - int(list2[i]))
    return distance

print(calculateDistance())
