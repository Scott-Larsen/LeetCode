# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

# Given a list of folders, remove all sub-folders in those folders and return in
# any order the folders after removing.

# If a folder[i] is located within another folder[j], it is called a sub-folder
# of it.

# The format of a path is one or more concatenated strings of the form: /
# followed by one or more lowercase English letters. For example, /leetcode and
# /leetcode/problems are valid paths while an empty string and / are not.

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key = len, reverse=True)
        res = [folder.pop()]
        res = set(res)
        while folder:
            f = folder.pop()
            entry, f = f[:], f[1:]
            f = f.split('/')
            for i in range(len(f)):
                if '/' + '/'.join(f[0:i + 1]) in res:
                    break
                elif i == len(f) - 1:
                    res.add(entry)
        return res