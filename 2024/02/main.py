safe = 0
with open('input', 'r', encoding='utf-8') as f:
    for line in f:
        report = list(map(int, line.split()))
        zipped = list(zip(report, report[1:]))
        if (all([a>b for a,b in zipped]) or all([b>a for a,b in zipped])) and all([abs(a-b) <= 3 for a,b in zipped]):
            safe += 1

print(safe)

safe = 0
with open('input', 'r', encoding='utf-8') as f:
    for line in f:
        report = list(map(int, line.split()))
        zipped = list(zip(report, report[1:]))
        if (all([a>b for a,b in zipped]) or all([b>a for a,b in zipped])) and all([abs(a-b) <= 3 for a,b in zipped]):
            safe += 1
        else:
            for i in range(0, len(report)):
                alt = report.copy()
                alt.pop(i)
                zipped = list(zip(alt, alt[1:]))
                if (all([a>b for a,b in zipped]) or all([b>a for a,b in zipped])) and all([abs(a-b) <= 3 for a,b in zipped]):
                    safe += 1
                    break

print(safe)
