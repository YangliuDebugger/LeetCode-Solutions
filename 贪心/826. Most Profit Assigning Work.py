class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # worker will pick the max profit job under his difficulty
        task = [[i, j] for i, j in zip(difficulty, profit)]
        task.sort()
        worker.sort()
        current_max_profit = 0
        total_profit = 0
        w_idx = 0
        task_idx = 0
        while w_idx < len(worker):
            while task_idx < len(task) and task[task_idx][0] <= worker[w_idx]:
                current_max_profit = max(current_max_profit, task[task_idx][1])
                task_idx += 1
            total_profit += current_max_profit
            w_idx += 1
        return total_profit
