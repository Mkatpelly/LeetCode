class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        prefix = ""
        for ch in searchWord:
            prefix += ch
            # first index where product >= prefix
            i = bisect.bisect_left(products, prefix)
            suggestions = []
            # check up to next 3 products starting from i
            for j in range(i, min(i + 3, len(products))):
                if products[j].startswith(prefix):
                    suggestions.append(products[j])
                else:
                    break
            res.append(suggestions)
        return res