# Day 01

Things to Know in python.
→ User Input/Output.
→ Data Types
→ If Else statement
→ Switch Statement
→ Arrays , Strings
→ For Loop
→ While Loop
→ Function
→ Time Complexity

=================
## what is Big-O
It's the time it takes for an algorithm to execute as the input size of the algorithm grows

=================
## O(1) -Constant growth
No matter the size of the input or how much it grows the time complexity of O(1) time algorithms is always the same, these are the most efficient algorithms

### Array
nums = [1, 2, 3]
nums.append(4)    # push to end
nums.pop()        # pop from end
nums[0]           # lookup
nums[1]
nums[2]

### HashMap / Set
hashMap = {}
hashMap["key"] = 10     # insert
print("key" in hashMap) # lookup
print(hashMap["key"])   # lookup
hashMap.pop("key")      # remove

==================
## O(n) -Linear Growth
As the input size grows the time is going to grow proportionately 

nums = [1, 2, 3]
sum(nums)           # sum of array
for n in nums:      # looping
    print(n)

nums.insert(1, 100) # insert middle
nums.remove(100)    # remove middle
print(100 in nums)  # search

import heapq
heapq.heapify(nums) # build heap

- sometimes even nested loops can be O(n) (e.g. monotonic stack or sliding window)

=====================
## O(n^2)