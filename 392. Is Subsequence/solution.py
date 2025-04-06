def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        pointer = 0
        for i in t:
            if s[pointer] == i:
                pointer += 1
            if pointer == len(s):
                return True
        return False