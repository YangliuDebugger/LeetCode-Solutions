class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        # 二分查找，当前城市电力不够的时候，通过greedy的办法尽量把新建的场子往后推
        def valid(m):
            # print(m)
            current_idx = 0
            end_idx = r
            left = k
            window_power = sum(stations[:r + 1])
            t_stations = stations[:]
            while current_idx < len(t_stations):
                # print(t_stations, left, window_power, current_idx, end_idx)
                if window_power < m:
                    left -= (m - window_power)
                    t_stations[end_idx] += (m - window_power)
                    window_power = max(m, window_power)
                if left < 0:
                    return False
                # 向右移动一位
                if current_idx - r >= 0:
                    window_power -= t_stations[current_idx - r]
                current_idx += 1
                if end_idx != len(t_stations) - 1:
                    end_idx += 1
                    window_power += t_stations[end_idx]
            return True

        low, high = min(stations), sum(stations) + k
        while True:
            if high - low <= 1:
                if valid(high):
                    return high
                return low
            mid = (low + high) // 2
            if valid(mid):
                low = mid
            else:
                high = mid


