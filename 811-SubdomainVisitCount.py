# A website domain like "discuss.leetcode.com" consists of various subdomains.
# At the top level, we have "com", at the next level, we have "leetcode.com",
# and at the lowest level, "discuss.leetcode.com". When we visit a domain like
# "discuss.leetcode.com", we will also visit the parent domains "leetcode.com"
# and "com" implicitly.

# Now, call a "count-paired domain" to be a count (representing the number of
# visits this domain received), followed by a space, followed by the address. An
# example of a count-paired domain might be "9001 discuss.leetcode.com".

# We are given a list cpdomains of count-paired domains. We would like a list of
# count-paired domains, (in the same format as the input, and in any order),
# that explicitly counts the number of visits to each subdomain.

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = collections.defaultdict(int)
        for cp in cpdomains:
            cp = cp.split(" ")
            count, domain = int(cp[0]), cp[1].split(".")
            while len(domain) > 0:
                d[".".join(domain)] = d[".".join(domain)] + count
                domain.pop(0)
        return [str(value) + " " + key for key, value in d.items()]