def decodeString(self, s: str) -> str:
        result = []
        temp = []
        num_temp = []
        start = 0
        for i in s:
            if i == ']':
                while result[-1] != '[':
                    temp.append(result.pop())
                temp = temp[::-1]
                result.pop()
                while result and result[-1].isdigit():
                    num_temp.append(result.pop())
                num = int(''.join(num_temp[::-1]))
                for _ in range(num):
                    result.append(''.join(temp))
                temp = []
                num_temp = []
            else:
                result.append(i)
        print(temp)
        print(result)
        return ''.join(result)