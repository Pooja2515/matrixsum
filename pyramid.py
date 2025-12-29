from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom, allowed):
        rules = defaultdict(list)

        for a in allowed:
            rules[(a[0], a[1])].append(a[2])

        def dfs(row):
            if len(row) == 1:
                return True

            def build_next(i, curr):
                if i == len(row) - 1:
                    return dfs(curr)

                pair = (row[i], row[i + 1])
                if pair not in rules:
                    return False

                for ch in rules[pair]:
                    if build_next(i + 1, curr + ch):
                        return True

                return False

            return build_next(0, "")

        return dfs(bottom)
