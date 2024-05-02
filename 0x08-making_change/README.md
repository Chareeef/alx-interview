# Making Change

## Description
I have a fascinating task at hand: determining the fewest number of coins needed to meet a given total amount using a pile of coins with different values.

## Prototype
```python
def makeChange(coins, total)
```

## Parameters
- `coins`: A list of the values of the coins in my possession. The value of a coin will always be an integer greater than 0.
- `total`: The amount total to be met with the coins.

## Return
The function should return the fewest number of coins needed to meet the total amount. If the total is 0 or less, it should return 0. If the total cannot be met by any number of coins I have, it should return -1.

## Example
```python
print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
```

## Note
- In the first example, with coins of values 1, 2, and 25, the fewest number of coins needed to make a total of 37 is 7 (25 + 2 + 2 + 2 + 2 + 2 + 2).
- In the second example, it's not possible to meet the total of 1453 with the available coins, hence the output is -1.

I'm excited to tackle this challenge using the greedy algorithm! Let's dive in and find the optimal solution together! 🚀
