def gcdOfStrings(self, str1: str, str2: str) -> str:
        x=''
        f=''
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        if str1+str2 != str2+str1:
            return f
        length = gcd(len(str1),len(str2))
        return str1[:length]