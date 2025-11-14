# 735. Asteroid Collision
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.
#
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
#
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
#
#
#
# Example 1:
#
# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
# Example 2:
#
# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# Example 3:
#
# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
# Example 4:
#
# Input: asteroids = [3,5,-6,2,-1,4]
# Output: [-6,2,4]
# Explanation: The asteroid -6 makes the asteroid 3 and 5 explode, and then continues going left. On the other side, the asteroid 2 makes the asteroid -1 explode and then continues going right, without reaching asteroid 4.
#
#
# Constraints:
#
# 2 <= asteroids.length <= 104
# -1000 <= asteroids[i] <= 1000
# asteroids[i] != 0

from typing import List, Optional

# https://leetcode.com/problems/asteroid-collision/solutions/109666/python-on-stack-based-with-explanation-b-u7ki
class Solution:
    def asteroidCollision(self, asteroids):
        res = []
        for asteroid in asteroids:
            # We only need to resolve collisions under the following conditions:
            # - stack is non-empty
            # - current asteroid is -ve
            # - top of the stack is +ve
            while len(res) and asteroid < 0 and res[-1] > 0:
                # Both asteroids are equal, destroy both.
                if res[-1] == -asteroid:
                    res.pop()
                    break
                # Stack top is smaller, remove the +ve asteroid
                # from the stack and continue the comparison.
                elif res[-1] < -asteroid:
                    res.pop()
                    continue
                # Stack top is larger, -ve asteroid is destroyed.
                elif res[-1] > -asteroid:
                    break
            else:
                # -ve asteroid made it all the way to the
                # bottom of the stack and destroyed all asteroids.
                res.append(asteroid)
        return res


class mySolution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # O(n), stack, add positive numbers to stack
        # compare incoming negative numbers to top value of stack
        # repeatedly pop top value of stack if positive_top <= abs(negative)
        # append negative value if stack becomes empty

        stack = []
        for n in asteroids:
            # if n > 0:
            #     stack.append(n)
            add_neg = True

            # negative asteroid
            while n < 0 and len(stack) > 0 and stack[-1] > 0 and stack[-1] <= abs(n):
                removed = stack.pop()
                # remove negative astroid if equal value
                if removed == abs(n):
                    add_neg = False
                    break

            # add neg asteroid if stack top value is neg or empty, and no equal size encountered
            if n < 0 and ((len(stack) > 0 and stack[-1] < 0) or len(stack) == 0) and (add_neg is True):
                stack.append(n)

            if n > 0:
                stack.append(n)

        return stack

class mySolution2:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # O(n), stack, add positive numbers to stack
        # compare incoming negative numbers to top value of stack
        # repeatedly pop top value of stack if positive_top <= abs(negative)
        # append negative value if stack becomes empty

        stack = []
        for n in asteroids:
            # add_neg = True # boolean flag when not using while..else

            # negative asteroid, check stack to see if we need to remov
            while n < 0 and len(stack) > 0 and stack[-1] > 0:
                if stack[-1] < abs(n):  # top is smaller
                    stack.pop()
                elif stack[-1] == abs(n):  # top is equal
                    stack.pop()
                    # add_neg = False # boolean flag when not using while..else
                    break
                else:  # top asteroid is larger
                    # add_neg = False # boolean flag when not using while..else
                    break
            else:  # loop never terminated from break, stack is either empty or only neg values, or n > 0
                stack.append(n)

            # # without using while..else, needs add_neg boolean
            # if add_neg is True:
            #     stack.append(n)

        return stack


class testcase1:
    asteroids = [5,10,-5]
    output = [5,10]

class testcase2:
    asteroids = [8,-8]
    output = []

class testcase3:
    asteroids = [10,2,-5]
    output = [10]

class testcase4:
    asteroids = [3,5,-6,2,-1,4]
    output = [-6,2,4]

# ai generated
class testcase5:
    asteroids = [10,2,-5,4,3,2,1]
    output = [10,4,3,2,1] # corrected output


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution2()

    # test example 1
    result1 = soln.asteroidCollision(testcase1.asteroids)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.asteroidCollision(testcase2.asteroids)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.asteroidCollision(testcase3.asteroids)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")

    # test example 4
    result4 = soln.asteroidCollision(testcase4.asteroids)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {result4 == testcase4.output}")

    # test example 5
    result5 = soln.asteroidCollision(testcase5.asteroids)
    print(f"Example 5 - Expected: {testcase5.output}, Got: {result5}, Correct: {result5 == testcase5.output}")