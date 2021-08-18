from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = [[] for _ in range(len(searchWord) + 1)]
        for i in range(1, len(searchWord) + 1):
            for word in products:
                if word.startswith(searchWord[:i]):
                    res[i].append(word)
        for i, lst in enumerate(res):
            if len(lst) > 3:
                res[i] = lst[:3]
        return res[1:]