# 1268. Search Suggestions System
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an array of strings products and a string searchWord.
#
# Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.
#
# Return a list of lists of the suggested products after each character of searchWord is typed.
#
#
#
# Example 1:
#
# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
# Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
# After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"].
# Example 2:
#
# Input: products = ["havana"], searchWord = "havana"
# Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
# Explanation: The only word "havana" will be always suggested while typing the search word.
#
#
# Constraints:
#
# 1 <= products.length <= 1000
# 1 <= products[i].length <= 3000
# 1 <= sum(products[i].length) <= 2 * 104
# All the strings of products are unique.
# products[i] consists of lowercase English letters.
# 1 <= searchWord.length <= 1000
# searchWord consists of lowercase English letters.
#

from typing import List, Optional


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:


        return


class mySolution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # problem description: return top 3 autocomplete results after each character in searchWord
        # len(output) == len(searchWord)

        # sort products to process them in lexographic order
        products = sorted(products)
        # build prefix trie, also storing whole words at each char level
        trie = {}
        for product in products:
            curr = trie
            for c in product:
                table = curr.get(c, {})
                # add product to list
                product_list = table.get('products', [])
                product_list.append(product)
                table['products'] = product_list
                # update trie
                curr[c] = table
                # move lower one level
                curr = table

        # return trie

        # find word
        output = []
        curr = trie
        for c in searchWord:
            d = curr.get(c, {})
            matching_products = d.get('products', [])
            output.append(matching_products[:3])

            # update curr
            curr = d

        return output


class testcase1:
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"
    output = [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]

class testcase2:
    products = ["havana"]
    searchWord = "havana"
    output = [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

class testcase3:
    products = ["havana"]
    searchWord = "titania"
    output = [[],[],[],[],[],[],[]]


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.suggestedProducts(testcase1.products, testcase1.searchWord)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.suggestedProducts(testcase2.products, testcase2.searchWord)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.suggestedProducts(testcase3.products, testcase3.searchWord)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")