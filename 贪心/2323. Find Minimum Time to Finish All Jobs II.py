class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        # 找到一种pair关系使得 min(max(job/work))最小
        # 引理：after 一一对应之后，如果 worker[i] > worker[j]，那么job[i] > job[j]
        # 否则我们总能通过对换使得他们变得至少不会变差
        return max([(job // worker) + (job % worker != 0)  for job, worker in zip(sorted(jobs), sorted(workers))])