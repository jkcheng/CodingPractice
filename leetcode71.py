# 71. Simplify Path
# Medium
# Topics
# premium lock icon
# Companies
# You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.
#
# The rules of a Unix-style file system are as follows:
#
# A single period '.' represents the current directory.
# A double period '..' represents the previous/parent directory.
# Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
# Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
# The simplified canonical path should follow these rules:
#
# The path must start with a single slash '/'.
# Directories within the path must be separated by exactly one slash '/'.
# The path must not end with a slash '/', unless it is the root directory.
# The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
# Return the simplified canonical path.
#
#
#
# Example 1:
#
# Input: path = "/home/"
#
# Output: "/home"
#
# Explanation:
#
# The trailing slash should be removed.
#
# Example 2:
#
# Input: path = "/home//foo/"
#
# Output: "/home/foo"
#
# Explanation:
#
# Multiple consecutive slashes are replaced by a single one.
#
# Example 3:
#
# Input: path = "/home/user/Documents/../Pictures"
#
# Output: "/home/user/Pictures"
#
# Explanation:
#
# A double period ".." refers to the directory up a level (the parent directory).
#
# Example 4:
#
# Input: path = "/../"
#
# Output: "/"
#
# Explanation:
#
# Going one level up from the root directory is not possible.
#
# Example 5:
#
# Input: path = "/.../a/../b/c/../d/./"
#
# Output: "/.../b/d"
#
# Explanation:
#
# "..." is a valid name for a directory in this problem.
#
#
#
# Constraints:
#
# 1 <= path.length <= 3000
# path consists of English letters, digits, period '.', slash '/' or '_'.
# path is a valid absolute Unix path.

from typing import List

class Solution:
    def simplifyPath(self, path: str) -> str:

        return


class mySolution:
    def simplifyPath(self, path: str) -> str:
        # . = remove from path
        # .. = remove self and previous folder from path
        # / remove trailing slash
        # // = replace multiple slashes with single

        # split string on '/'
        pathlist = path.split('/')
        newpath = []

        for s in pathlist:
            if s == '..':
                if len(newpath) > 0:
                    newpath.pop()
            elif s == '.':
                pass
            elif s == '':
                pass
            else:
                newpath.append(s)

        return '/' + '/'.join(newpath)

class testcase1:
    path = "/home/"
    output = "/home"

class testcase2:
    path = "/home//foo/"
    output = "/home/foo"

class testcase3:
    path = "/home/user/Documents/../Pictures"
    output = "/home/user/Pictures"

class testcase4:
    path = "/../"
    output = "/"

class testcase5:
    path = "/.../a/../b/c/../d/./"
    output = "/.../b/d"

if __name__ == "__main__":
    # Create solution instance
    solution = mySolution()

    # Test with example 1
    result1 = solution.simplifyPath(testcase1.path)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # Test with example 2
    result2 = solution.simplifyPath(testcase2.path)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # Test with example 3
    result3 = solution.simplifyPath(testcase3.path)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")

    # Test with example 4
    result4 = solution.simplifyPath(testcase4.path)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {result4 == testcase4.output}")

    # Test with example 5
    result5 = solution.simplifyPath(testcase5.path)
    print(f"Example 5 - Expected: {testcase5.output}, Got: {result5}, Correct: {result5 == testcase5.output}")
