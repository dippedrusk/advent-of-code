list1, list2 = [], []

with open('input', 'r', encoding='utf-8') as f:
    for line in f:
        num1, num2 = list(map(int, line.split()))
        list1.append(num1)
        list2.append(num2)

diffs = []
for a, b in zip(sorted(list1), sorted(list2)):
    diffs.append(abs(a-b))

print(sum(diffs))

scores = []
for a in list1:
    scores.append(a * list2.count(a))

print(sum(scores))
