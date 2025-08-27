# 433. Minimum Genetic Mutation
# Medium
# Topics
# premium lock icon
# Companies
# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.
#
# Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.
#
# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.
#
# Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.
#
# Note that the starting point is assumed to be valid, so it might not be included in the bank.
#
#
#
# Example 1:
#
# Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
# Output: 1
# Example 2:
#
# Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
# Output: 2
#
#
# Constraints:
#
# 0 <= bank.length <= 10
# startGene.length == endGene.length == bank[i].length == 8
# startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].

from typing import List,Optional


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        return


class mySolution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # BFS, queue: add startGene to queue, add all genes form bank 1-step away from startGene
        # pop 1-step genes from queue and add all genes from bank 1-step away from these
        # repeat until endGene found and return step level
        # return -1 otherwise

        def step_diff(gene, curr):
            # todo
            stepcount = 0
            for i in range(len(gene)):
                curr_c = curr[i]
                gene_c = gene[i]
                if curr_c != gene_c:
                    stepcount += 1
            return stepcount

        # create graph
        graph = {}
        graph[startGene] = []

        queue = [(startGene, 0)]  # use deque for optimization
        while len(queue) > 0:
            for _ in range(len(queue)):
                curr, step = queue.pop(0)
                for gene in bank:
                    if step_diff(gene, curr) == 1:
                        if gene == endGene:
                            return step + 1
                        else:
                            queue.append((gene, step + 1))

        return -1


class testcase1:
    startGene = "AACCGGTT"
    endGene = "AACCGGTA"
    bank = ["AACCGGTA"]
    output = 1

class testcase2:
    startGene = "AACCGGTT"
    endGene = "AAACGGTA"
    bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    output = 2

# AI created
class testcase3:
    startGene = "AAAAACCC"
    endGene = "AACCCCCC"
    bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
    output = 3

class testcase4:
    startGene = "AAAAACCC"
    endGene = "AACCCCCC"
    bank = ["AAAACCCC","AACCCCCC"]
    output = -1


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.minMutation(testcase1.startGene, testcase1.endGene, testcase1.bank)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}")

    # test example 2
    result2 = soln.minMutation(testcase2.startGene, testcase2.endGene, testcase2.bank)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")

    # test example 3
    result3 = soln.minMutation(testcase3.startGene, testcase3.endGene, testcase3.bank)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}")

    # test example 4
    result4 = soln.minMutation(testcase4.startGene, testcase4.endGene, testcase4.bank)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {testcase4.output == result4}")