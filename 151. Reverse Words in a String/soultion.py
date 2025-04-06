def reverseWords(self, s: str) -> str:
        reverse = []
        queue = s.split()
        return  " ".join(queue[::-1])