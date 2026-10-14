class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.replace('?', '')
        s = s.replace('!','')
        s = s.replace(',','')
        s = s.replace('.','')
        s = s.replace("'","")
        s = s.replace(":","")
        s = s.lower()
        farr = []
        barr = []
        for n in s:
            farr.append(n)
            barr.insert(0,n)
            print(farr, barr)
        if barr == farr:
            return True
        return False