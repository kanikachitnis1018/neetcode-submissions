class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        pairs = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for symbol in s:
            if symbol in "([{":
                st.append(symbol)
            else: 
                if not st:
                    return False
                else:
                    if st[-1] != pairs[symbol]:
                        return False
                    st.pop()
        return not st