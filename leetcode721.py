


from typing import List

class mySolution():
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        seen = set()
        merged = {}
        for account in accounts:
            name = account[0]
            emails = account[1:]
            newentry = True
            for email in emails:
                if email in seen:
                    merged[name] = merged.get(name, set()).union(emails)
                    newentry = False
                    break
                else:
                    seen.add(email)

            if newentry:
                merged[name] = set(emails)

        return merged

class testcase1:
    accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]