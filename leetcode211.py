# 211. Design Add and Search Words Data Structure
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Design a data structure that supports adding new words and finding if a string matches any previously added string.
#
# Implement the WordDictionary class:
#
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
#
#
# Example:
#
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
#
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
#
#
# Constraints:
#
# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 2 dots in word for search queries.
# At most 104 calls will be made to addWord and search.

from typing import List,Optional

# using TrieNode helper class
class TrieNode(object):
    def __init__(self, x):
        self.val = x
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode(None)

    def addWord(self, word: str) -> None:
        cur = self.root
        for letter in word:
            child = cur.children.get(letter)
            if child == None:
                child = TrieNode(letter)
                cur.children[letter] = child
            cur = child

        cur.is_word = True

        return

    def search(self, word: str) -> bool:
        nodes = [self.root]
        # cur = self.root
        ncount = 1
        for letter in word:
            for i in range(ncount):
                cur = nodes.pop(0)
                if letter == '.':
                    # add all children
                    nodes.extend(cur.children.values())
                else:
                    child = cur.children.get(letter)
                    if child != None:
                        nodes.append(child)

            ncount = len(nodes)
            if ncount == 0:
                return False

        found = any([node.is_word for node in nodes])
        return found


class myWordDictionary:
    # create a trie to store characters of each word, ending with special ending char
    # use nested dictionary as structure
    def __init__(self):
        self.words = {}

    def addWord(self, word: str) -> None:
        table = self.words
        for c in word:
            table[c] = table.get(c, {})
            # set table to one level deeper
            table = table[c]

        # add special end char #
        table['#'] = {}

    def search(self, word: str) -> bool:
        # table = self.words
        table = None
        queue = [self.words]
        for c in word:
            for _ in range(len(queue)):
                table = queue.pop(0)
                # add all values if c is wildcard and table is not empty
                # add table at c if exists
                if c == '.' and len(table) > 0:
                    queue.extend(list(table.values()))
                elif c in table:
                    queue.append(table.get(c))

        # check for ending char in queue items
        for table in queue:
            if '#' in table:
                return True
        # if table is not None and '#' in table:
        #     return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

class testcase1:
    input = ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"]
    inputvals = [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]
    output = [None, None, None, None, False, True, True, True]

if __name__ == "__main__":
    # create class instance
    soln = myWordDictionary()

    # todo: implement testcases for class creation problems
    print(soln.addWord("bad"))
    print(soln.addWord("dad"))
    print(soln.addWord("mad"))
    print(soln.search("pad"))
    print(soln.search("bad"))
    print(soln.search(".ad"))
    print(soln.search("b.."))