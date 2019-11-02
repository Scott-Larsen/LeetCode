# A query word matches a given pattern if we can insert lowercase letters to the
# pattern word so that it equals the query. (We may insert each character at any
# position, and may insert 0 characters.)

# Given a list of queries, and a pattern, return an answer list of booleans,
# where answer[i] is true if and only if queries[i] matches the pattern.

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for query in queries:
            i, j = 0, 0
            while i < len(query):
                if j < len(pattern) and query[i] == pattern[j]:
                    j += 1
                elif query[i].isupper() and query[i] not in pattern[j:]:
                    res.append(bool(0))
                    break
                if i == len(query) - 1:
                    if j >= len(pattern):
                        res.append(bool(1))
                    else:
                        res.append(bool(0))
                i += 1
        return res