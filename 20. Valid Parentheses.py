class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"}": "{", "]": "[", ")": "("}
        st = []

        for ch in s:
            if ch in mapping.values():
                st.append(ch)
            elif ch in mapping.keys():
                if not st or st.pop() != mapping[ch]:
                    return False

        return len(st) == 0
