import sys

scores = list(map(int,sys.arg[1:]))

total = sum(scores)
average = total/len(scores)

print("scores:", scores)
print("sum",total)
print("Average:",average)