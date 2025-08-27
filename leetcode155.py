# 155. Min Stack
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# Implement the MinStack class:
#
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.
#
#
#
# Example 1:
#
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# Output
# [null,null,null,null,-3,null,0,-2]
#
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
#
#
# Constraints:
#
# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.

from typing import List


class MinStack:
    # add (val, current_min_val) to stack
    # current_min_val is the current minimum value at the time val is added to stack
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            oldmin = self.stack[-1][1]
            curmin = min(val, oldmin)
        else:
            curmin = val

        self.stack.append((val, curmin))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


class myMinStack:
    # store items in stack as tuple with (val, current_min)

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # update minval to new value if lower than current
        # check if stack is empty
        if len(self.stack) > 0:
            minval = min(val, self.stack[-1][1])
        else:
            minval = val

        self.stack.append((val,minval))
        return

    def pop(self) -> None:
        val,oldmin = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

class testcase1:
    input = ["MinStack","push","push","push","getMin","pop","top","getMin"]
    inputvals = [[],[-2],[0],[-3],[],[],[],[]]
    output = [None,None,None,None,-3,None,0,-2]

class testcase2:
    input = ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
    inputvals = [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
    output = [None,None,None,None,2147483647,None,2147483646,None,2147483646,None,None,2147483647,2147483647,None,-2147483648,-2147483648,None,2147483647]

class testcase3:
    input = ["MinStack","push","push","getMin","getMin","push","getMin","getMin","top","getMin","pop","push","push","getMin","push","pop","top","getMin","pop"]
    inputvals = [[],[-10],[14],[],[],[-20],[],[],[],[],[],[10],[-7],[],[-7],[],[],[],[]]
    output = [None,None,None,-10,-10,None,-20,-20,-20,-20,None,None,None,-10,None,None,-7,-10,None]

if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    obj = myMinStack()

    # Test with example 1
    result1 = []
    for i in range(len(testcase1.input)):
        if testcase1.input[i] == "push":
            obj.push(testcase1.inputvals[i][0])
            result1.append(None)
        elif testcase1.input[i] == "pop":
            obj.pop()
            result1.append(None)
        elif testcase1.input[i] == "top":
            result1.append(obj.top())
        elif testcase1.input[i] == "getMin":
            result1.append(obj.getMin())
        else:
            result1.append(None)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # Test with example 2
    obj = myMinStack()
    result2 = []
    for i in range(len(testcase2.input)):
        if testcase2.input[i] == "push":
            obj.push(testcase2.inputvals[i][0])
            result2.append(None)
        elif testcase2.input[i] == "pop":
            obj.pop()
            result2.append(None)
        elif testcase2.input[i] == "top":
            result2.append(obj.top())
        elif testcase2.input[i] == "getMin":
            result2.append(obj.getMin())
        else:
            result2.append(None)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # Test with example 3
    obj = myMinStack()
    result3 = []
    for i in range(len(testcase3.input)):
        if testcase3.input[i] == "push":
            obj.push(testcase3.inputvals[i][0])
            result3.append(None)
        elif testcase3.input[i] == "pop":
            obj.pop()
            result3.append(None)
        elif testcase3.input[i] == "top":
            result3.append(obj.top())
        elif testcase3.input[i] == "getMin":
            result3.append(obj.getMin())
        else:
            result3.append(None)
    print(f"Example 2 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")


