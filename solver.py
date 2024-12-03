#!/env/bin/python

import sys

l1 = []
l2 = []
solutions = []
with open(sys.argv[1]) as f:
    for line in f.readlines():
        line = line.rstrip("\n")
        l1.append(int(line.split("   ")[0]))
        l2.append(int(line.split("   ")[1]))

l1.sort()
l2.sort()

# lets assume they're sorted correctly
for i in range(len(l1)):
    delta = l1[i] - l2[i] if l1[i] > l2[i] else l2[i] - l1[i]
    solutions.append(delta)
    
print(sum(solutions))