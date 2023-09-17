class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # my idea is to go through and find the max length of T with at most k F in the middle
        # do the same thing for the F and see what happens
        buffer_t = k
        buffer_f = k
        max_cons_t = 0
        c_t = 0
        c_f = 0
        max_const_f = 0
        e_t = 0
        e_f = 0
        s_t = 0
        s_f = 0
        for i, el in enumerate(answerKey):
            if el == 'T' and buffer_t >= 0:
                c_t += 1
            elif el == 'T' and buffer_t < 0:
                s_t = i
                c_t = 1
                buffer_t = k

            if el == 'F' and buffer_f >= 0:
                c_f += 1
            elif el == 'F' and buffer_f < 0:
                s_f = i
                c_f = 1
                buffer_f = k 
            
            if c_t > max_cons_t:
                s_t, e_t = s_t, i
                max_cons_t = max(max_cons_t, c_t)
            if c_f > max_const_f:
                s_f, e_f = s_f, i
                max_const_f = max(max_const_f, c_f)

        c_t = 0
        for el in answerKey[s_t : e_t]:
            if el == 'F':
                c_t += 1

        c_f = 0
        for el in answerKey[s_f : e_f]:
            if el == 'T':
                c_f += 1

        return max(c_t, c_f)



# no workering
s = Solution()
print(s.maxConsecutiveAnswers("TTFFTTTTTTFFFFTTT", k=2))
