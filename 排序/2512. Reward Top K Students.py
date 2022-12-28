class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        r = []
        positive_feedback, negative_feedback = set(positive_feedback), set(negative_feedback)
        for s, s_id in zip(report, student_id):
            score = 0
            for w in s.split():
                if w in positive_feedback:
                    score += 3
                if w in negative_feedback:
                    score -= 1
            r.append((-score, s_id))
        r.sort()
        return [s_id for score, s_id in r][:k]