# Problem: Number of Ways to reconstruct a Tree - https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/

class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        relations = defaultdict(set)
        for x, y in pairs:
            relations[x].add(y)
            relations[y].add(x)
        descendants = defaultdict(set)
        roots, multiple = 0, 0

        def add(v):
            nonlocal roots, multiple
            sub_nodes = descendants.pop(v, set())
            if not (relations[v] >= sub_nodes):
                return False
            d = sorted(relations[v] - sub_nodes, key=lambda x: len(relations[x]))
            if len(d) == 0:
                roots += 1
                return roots == 1
            if len(relations[d[0]]) < len(relations[v]):
                return False
            for u in d:
                if len(relations[d[0]]) != len(relations[u]):
                    break
                descendants[u] |= sub_nodes | {v}
            if len(relations[d[0]]) == len(relations[v]) or len(d) > 1 and len(relations[d[0]]) == len(relations[d[1]]):
                multiple += 1
            return True

        if any(not add(v) for v in sorted(relations.keys(), key=lambda x: len(relations[x]))):
            return 0
        return 2 if multiple else 1