import random
import time

def countingSort(input, maxValue):
    size = len(input)
    count = [0] * (maxValue + 1)
    output = [0] * size

    for i in range(0, size):
        count[input[i]] += 1
    
    for i in range(1, maxValue + 1):
        count[i] += count[i - 1]
    
    i = size - 1
    while i >= 0:
        output[count[input[i]] - 1] = input[i]
        count[input[i]] -= 1
        i -= 1

    return output 

def main():
    maxValue = 100
    size = 1000000

    start = time.perf_counter()
    comprehensionList = [random.randint(0,maxValue) for i in range(0, size)]
    finish = time.perf_counter()
    print("comprehension list time to create: " + "{:0.4f}".format(finish - start) + " seconds\n")

    start = time.perf_counter()
    loopList = [0]
    for i in range(size):
        loopList.append(random.randint(0,maxValue))
    finish = time.perf_counter()
    print("loop list time to create: " + "{:0.4f}".format(finish - start) + " seconds\n")

    start = time.perf_counter()
    sortedList = countingSort(comprehensionList, maxValue)
    finish = time.perf_counter()
    print("Counting sort time: " + "{:0.4f}".format(finish - start) + " seconds\n")

    start = time.perf_counter()
    comprehensionList.sort()
    finish = time.perf_counter()
    print("Python sort time: " + "{:0.4f}".format(finish - start) + " seconds\n")

    if comprehensionList == sortedList:
        print("The lists are idenitical")
    else:
        print("The lists are different")

if __name__=="__main__":
    main()
