class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:
        d = {}
        for idx, feat in enumerate(features):
            d[feat] = [idx, 0]
        for res in responses:
            for word in set(res.split()):
                if word in d:
                    d[word][1] += 1
        features.sort(key = lambda x:[-d[x][1], d[x][0]])
        return features