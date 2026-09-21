# LeetCode 213 - House Robber II

## Problem Description

You are given an array `nums` where each element represents the amount of money in a house.

The houses are arranged in a circle, so the first and last houses are neighbors.

You cannot rob two adjacent houses.

Return the maximum amount of money that can be robbed without robbing two adjacent houses.

## Example

Input:

nums = [2,3,2]

We cannot rob both the first and last houses because they are adjacent.

The maximum amount is:

3

Output:

3

## Approach

This problem is similar to House Robber, but the houses are arranged in a circle.

Because the first and last houses are connected, we cannot rob both of them.

So, we divide the problem into two cases:

1. Exclude the first house and consider the remaining houses.
2. Exclude the last house and consider the remaining houses.

For each case, we solve the normal House Robber problem using dynamic programming.

Finally, we return the maximum result from the two cases.

## Algorithm

1. If there is only one house, return its value.
2. Solve the problem excluding the first house.
3. Solve the problem excluding the last house.
4. Take the maximum of the two results.
5. Return the answer.

## Time Complexity

**O(n)**

Each house is processed a constant number of times.

## Space Complexity

**O(1)**

Only a few variables are used for the dynamic programming calculation.

## Key Concepts

- Dynamic Programming
- Arrays
- Two Cases
- Circular Array
- House Robber

## Author

T.nandhini
