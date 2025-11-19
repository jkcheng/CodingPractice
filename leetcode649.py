# 649. Dota2 Senate
# Medium
# Topics
# premium lock icon
# Companies
# In the world of Dota2, there are two parties: the Radiant and the Dire.
#
# The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:
#
# Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
# Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
# Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.
#
# The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.
#
# Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".
#
#
#
# Example 1:
#
# Input: senate = "RD"
# Output: "Radiant"
# Explanation:
# The first senator comes from Radiant and he can just ban the next senator's right in round 1.
# And the second senator can't exercise any rights anymore since his right has been banned.
# And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
# Example 2:
#
# Input: senate = "RDD"
# Output: "Dire"
# Explanation:
# The first senator comes from Radiant and he can just ban the next senator's right in round 1.
# And the second senator can't exercise any rights anymore since his right has been banned.
# And the third senator comes from Dire and he can ban the first senator's right in round 1.
# And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
#
#
# Constraints:
#
# n == senate.length
# 1 <= n <= 104
# senate[i] is either 'R' or 'D'.

from typing import List, Optional


class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        return


from collections import deque
class mySolution:
    def predictPartyVictory(self, senate: str) -> str:
        # O((n/2)^2)?, two revolving queues of index values
        # compare first values of two queues, eliminate larger
        # move smaller non-elminated index to end of it's queue and add n for it's releative positioning next round
        # continue until one queue empty

        # create list and count values
        # qR, qD = [], []
        qR, qD = deque(), deque()
        for i,c in enumerate(senate):
            if c == 'R':
                qR.append(i)
            else:
                qD.append(i)


        # process each senator and move to end of queue
        n = len(senate)
        while len(qR) > 0 and len(qD) > 0:
            # iR = qR.pop(0)
            # iD = qD.pop(0)
            iR = qR.popleft()
            iD = qD.popleft()

            if iR < iD:
                qR.append(iR + n)
            else:
                qD.append(iD + n)

        return 'Radiant' if len(qR) > 0 else 'Dire'


class testcase1:
    senate = "RD"
    output = "Radiant"

class testcase2:
    senate = "RDD"
    output = "Dire"

# ai generated
class testcase3:
    senate = "RDDRD"
    output = "Dire"


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.predictPartyVictory(testcase1.senate)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.predictPartyVictory(testcase2.senate)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.predictPartyVictory(testcase3.senate)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")
