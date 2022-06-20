class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        # sliding window 的题目
        tiles.sort()
        carpet_left = tiles[0][0]
        carpet_right = carpet_left + carpetLen - 1
        global_max = 0
        tile_cnt = 0
        tile_idx = 0
        tile_left_cnt = 0
        while True:
            while tile_idx < len(tiles) and tiles[tile_idx][1] <= carpet_right:
                tile_cnt += tiles[tile_idx][1] - tiles[tile_idx][0] + 1
                tile_idx += 1
            if tile_idx == len(tiles):
                global_max = max(global_max, tile_cnt)
                break
            print(carpet_left, carpet_right, tile_cnt, tile_left_cnt)
            global_max = max(global_max, tile_cnt + max(0, carpet_right - tiles[tile_idx][0] + 1))

            tile_cnt -= (tiles[tile_left_cnt][1] - tiles[tile_left_cnt][0] + 1)
            tile_left_cnt += 1
            if tile_left_cnt == len(tiles):
                break
            carpet_left = tiles[tile_left_cnt][0]
            carpet_right = carpet_left + carpetLen - 1

        return global_max