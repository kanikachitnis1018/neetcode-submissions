class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        st = []

        for i in range(len(temperatures)):
            while st and temperatures[i] > temperatures[st[-1]]: 
                prev_day = st.pop()
                result[prev_day] = i - prev_day
            st.append(i)
        return result
                