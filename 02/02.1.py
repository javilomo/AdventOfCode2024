def safeControl():
    safe_count = 0

    with open(r'C:\Users\javier.lopez.morale\Documents\GitHub\AdventOfCode2024\02\input_02.txt', 'r') as input2:
        for line in input2:
            report = line.strip().split()

            if len(report) < 2:
                continue

            report = [int(x) for x in report]

            if report[1] > report[0]:
                inc = True
            elif report[1] < report[0]:
                inc = False
            else:
                continue

            safe = True
            for i in range(1, len(report)):
                diff = report[i] - report[i - 1] if inc else report[i - 1] - report[i]

                if diff < 1 or diff > 3:
                    safe = False
                    break

                if inc and report[i] <= report[i - 1]:
                    safe = False
                    break
                if not inc and report[i] >= report[i - 1]:
                    safe = False
                    break

            if safe:
                safe_count += 1
                print(report)

    return safe_count

print(safeControl())
