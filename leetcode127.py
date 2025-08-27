# 127. Word Ladder
# Solved
# Hard
# Topics
# premium lock icon
# Companies
# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
#
#
#
# Example 1:
#
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:
#
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
#
#
# Constraints:
#
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.

from typing import List,Optional

# idea: build adjacency list (graph) of words that differ by 1 letter, then find shortest path from beginWord -> endWord using BFS
class Solution:
    def buildGraph(self, beginWord, wordList):
        # naive approach: compare every word to each other O(n^2)
        # optimized approach: construct adj_list with wildcard patterns as key (e.g. hot -> *ot, h*t, ho*) and list of words as values
        adj_list = {}

        words = wordList + [beginWord]
        for word in words:
            for c in range(len(word)):
                pattern = word[0:c] + '*' + word[c + 1:]
                adj_list[pattern] = adj_list.get(pattern, [])  # or use defaultdict to avoid this line
                adj_list[pattern].append(word)

        return adj_list

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # build pattern adjacency list
        adj_list = self.buildGraph(beginWord, wordList)

        # bfs
        # queue = [beginWord] # or use deque() and popleft for optimization
        queue = collections.deque([beginWord])
        visited = set()
        ans = 1
        while len(queue) > 0:
            for i in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return ans

                visited.add(word)
                for c in range(len(word)):
                    pattern = word[0:c] + '*' + word[c + 1:]
                    neighbors = adj_list[pattern]
                    for nei in neighbors:
                        if (nei not in visited) and (nei not in queue):
                            queue.append(nei)

            ans += 1
        return 0

# naive BFS, passes but terrible run time
class mySolution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS, queue: create queue with beingWord, then add words 1-step away from beginWord
        # pop words from queue to add words 1-step away from these, increment step for each level
        # return step when endword found, otherwise return 0
        # turn wordlist into set and remove words as encountered

        def edit_dist(word, other_word):
            dist = 0
            for i in range(len(word)):
                c = word[i]
                other_c = other_word[i]
                if c != other_c:
                    dist += 1

            return dist

        wordList = set(wordList)
        queue = [(beginWord, 1)] # use deque for optimization
        visited = set()
        # other_words = wordList.copy() # shallow good enough because str immutable
        while len(queue) > 0:

            for _ in range(len(queue)):
                word,dist = queue.pop(0)
                visited.add(word)
                other_words = list(wordList)
                for other_word in other_words:
                    # if edit distance == 1, add to queue
                    if other_word not in visited and edit_dist(word, other_word) == 1:
                        # return edit distance if endWord found
                        if other_word == endWord:
                            return dist + 1
                        else:
                            queue.append((other_word, dist+1))
                            wordList.remove(other_word)

        return 0


class testcase1:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    output = 5

class testcase2:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    output = 0

# AI testcases: fail to meet problem constraints

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.ladderLength(testcase1.beginWord, testcase1.endWord, testcase1.wordList)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}")

    # test example 2
    result2 = soln.ladderLength(testcase2.beginWord, testcase2.endWord, testcase2.wordList)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")