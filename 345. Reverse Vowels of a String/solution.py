def reverseVowels(self, s: str) -> str:
        a = ''
        l = list(s)
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        e_vow = []
        i = 0
        for i in range(len(s)):
            if l[i] in vowel:
                e_vow.append(s[i])
                l[i] = ''
        
        e_vow.reverse()
        for i in range(len(s)):
            if l[i] == '':
                temp = e_vow.pop(0)
                l[i] = temp

        return a.join(l)