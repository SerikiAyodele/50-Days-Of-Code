problems from a tutorial [https://www.youtube.com/watch?v=tN2sqeFOQXk] to help me understand functions

## Problem 1
Write a Python function called max_of_three to find the maximum value between three numbers. Do not use the max() function.

```
def max_of_two( x, y ):
    if x > y:
        return x
    return y

def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )

print(max_of_three(3, 6, -5))
```
## Problem 2
Write a Python function called multiply to multiply all of the numbers in a list together and return that value. The function should be created in such a way that it will work for both lists, tuples, and sets.

```
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  

testList = [8, 2, 3, -1, 7]

print(multiply(testList))
```
## Problem 3
Write a Python function called caseCounter that counts the number of lowercase and uppercase characters in a string. If you're up to it, store the lowercase and uppercase variables in a dictionary within the function. The function should print two sentences that state the number of uppercase and lowercase characters.
```
def caseCounter(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("No. of uppercase characters : ", d["UPPER_CASE"])
    print ("No. of lowercase Characters : ", d["LOWER_CASE"])
    
print(caseCounter('Nicholas McCullum'))
```

## Problem 4
Write a Python function called duplicateEliminator that takes in a list, eliminates any duplicate values, and returns a set.
```
def duplicateEliminator(l):
    return set(l)

print(duplicateEliminator([1,1,2,2]))
```