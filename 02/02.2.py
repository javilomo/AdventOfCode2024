def is_safe(report):
    if len(report) < 2:
        return True

    inc = report[1] > report[0]

    for i in range(1, len(report)):
        diff = abs(report[i] - report[i - 1])
        if diff < 1 or diff > 3:
            return False
        if inc and report[i] <= report[i - 1]:
            return False
        if not inc and report[i] >= report[i - 1]:
            return False

    return True


def safeControl():
    safe_count = 0

    with open(r'C:\Users\javier.lopez.morale\Documents\GitHub\AdventOfCode2024\02\input_02.txt', 'r') as input2:
        for line in input2:
            report = line.strip().split()

            if len(report) < 2:
                continue

            report = [int(x) for x in report]

            if is_safe(report):
                safe_count += 1
                print(f"Safe: {report}")
                continue


            for i in range(len(report)):
                modified_report = report[:i] + report[i + 1:]
                if is_safe(modified_report):
                    safe_count += 1
                    print(f"Safe by removing {report[i]}: {report}")
                    break

    return safe_count


print(safeControl())
