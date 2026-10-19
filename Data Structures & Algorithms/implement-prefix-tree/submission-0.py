class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        subtree = self.root
        for l in word:
            if l == word[-1] and subtree.get(l) == None:
                subtree[l] = {'end':True}
            elif l == word[-1]:
                subtree[l]['end'] = True
            elif subtree.get(l) == None:
                subtree[l] = {}
            subtree = subtree[l]
        

    def search(self, word: str) -> bool:
        subtree = self.root
        for l in word:
            if subtree.get(l) == None:
                return False
            subtree = subtree[l]
        else:
            if subtree.get('end') == None:
                return False
            return True

    def startsWith(self, prefix: str) -> bool:
        subtree = self.root
        for l in prefix:
            if subtree.get(l) == None:
                return False
            subtree = subtree[l]
        else:
            return True
        