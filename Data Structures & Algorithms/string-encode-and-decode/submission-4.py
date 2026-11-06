class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            for c in s:
                encoded_string = encoded_string + str(ord(c)) + ","
            if s == '':
                encoded_string = encoded_string +  "@"
            encoded_string = encoded_string +  "."
        encoded_string = encoded_string[:-1]
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        strs = []
        print(s)
        spl1 = s.split(".")
        print(spl1, "h1")
        for s in spl1:
            if s == "@":
                strs.append('')
                continue
            s = s[:-1]
            spl2 = s.split(",")
            temp = ""
            print(spl2, "h2")
            for l in spl2:
                print(l, "h3")
                temp = temp + chr(int(l))
            else:
                strs.append(temp)
        return strs