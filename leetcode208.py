# 208. Implement Trie (Prefix Tree)
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
#
# Implement the Trie class:
#
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
#
#
# Example 1:
#
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]
#
# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
#
#
# Constraints:
#
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 104 calls in total will be made to insert, search, and startsWith.

from typing import List,Optional


# Definition for a trie node.
class TrieNode(object):
    def __init__(self, x):
        self.val = x
        self.children = {}
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode(None)
        return

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            child = node.children.get(letter)
            if child == None:
                child = TrieNode(letter)
                node.children[letter] = child

            node = child

        node.is_word = True
        return self.root

    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if node != None:
                node = node.children.get(letter)

        return node.is_word if node else False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for letter in prefix:
            if node != None:
                node = node.children.get(letter)

        return True if node else False


class myTrie:
    # python dictionary implementation of trie
    def __init__(self):
        self.words = {}

    def insert(self, word: str) -> None:
        table = self.words
        for c in word:
            table[c] = table.get(c, {})
            # move one level deeper for next char
            table = table[c]

        # add ending character key-value to mark end of word
        table['#'] = {}

    def search(self, word: str) -> bool:
        table = self.words
        for c in word:
            table = table.get(c, None)
            if table is None:
                return False

        return '#' in table  # check for ending character

    def startsWith(self, prefix: str) -> bool:
        table = self.words
        for c in prefix:
            table = table.get(c, None)
            if table is None:
                return False

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class testcase1:
    input = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    inputvals = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    output = [None, None, True, False, True, None, True]

class testcase2:
    input = ["Trie","startsWith"]
    inputvals = [[],["a"]]
    output = [None, False]

class testcase3:
    input = ["Trie","insert","insert","insert","insert","insert","insert","search","search","search","search","search","search","search","search","search","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith"]
    inputvals = [[],["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]]
    output = [None,None,None,None,None,None,None,False,True,False,False,False,False,False,True,True,False,True,True,False,False,False,True,True,True]

if __name__ == "__main__":
    # create Solution instance for each test case
    # test example 1
    soln = myTrie()
    result1 = [None] * len(testcase1.output)
    for i,call in enumerate(testcase1.input):
        if i > 0:
            func = getattr(soln, call)
            input = testcase1.inputvals[i][0]
            result = func(input)
            result1[i] = result
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    soln = myTrie()
    result2 = [None] * len(testcase2.output)
    for i,call in enumerate(testcase2.input):
        if i > 0:
            func = getattr(soln, call)
            input = testcase2.inputvals[i][0]
            result = func(input)
            result2[i] = result
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    soln = myTrie()
    result3 = [None] * len(testcase3.output)
    for i,call in enumerate(testcase3.input):
        if i > 0:
            func = getattr(soln, call)
            input = testcase3.inputvals[i][0]
            result = func(input)
            result3[i] = result
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")