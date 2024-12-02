from heapq import heapify, heappush, heappop 

left = [] 
right = []

heapify(left) 
heapify(right) 

rightFreq = dict()
leftNums = []

with open("input.txt") as f:
    for line in f.readlines():
        line = line.strip().split("   ")
        leftNum = int(line[0])
        rightNum = int(line[1])
        heappush(left, leftNum) 
        heappush(right, rightNum) 
        leftNums.append(leftNum)
        if rightNum in rightFreq:
            rightFreq[rightNum] += 1
        else:
            rightFreq[rightNum] = 1 

sum = 0
for i in range(len(left)):
    sum += abs(heappop(left) - heappop(right))

print(f'Total distance: {sum}')

sum = 0
for num in leftNums:
    if num in rightFreq:
        sum += rightFreq[num] * num

print(f'Freq: {sum}')