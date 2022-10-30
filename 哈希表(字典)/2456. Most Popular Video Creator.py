class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        creators_dict = {}
        creators_videos = {}

        maxv = 0

        for c, idx, v in zip(creators, ids, views):
            if c not in creators_dict:
                creators_dict[c] = 0
                creators_videos[c] = []
            creators_dict[c] += v
            creators_videos[c].append((-v, idx))
            maxv = max(maxv, creators_dict[c])
        res = []
        for c in creators_dict:
            if creators_dict[c] == maxv:
                creators_videos[c].sort()
                res.append([c, creators_videos[c][0][1]])
        return res


