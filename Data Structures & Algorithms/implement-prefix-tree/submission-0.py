class PrefixTree:

    def __init__(self):
        self.children = [None]*26
        self.end = False
        

    def insert(self, word: str) -> None:
        tree = self

        for char in word:
            index = ord(char) - ord("a")

            if not tree.children[index]:
                tree.children[index] = PrefixTree()
            
            tree = tree.children[index]
        
        tree.end = True


    def search(self, word: str) -> bool:
        tree = self

        for char in word:
            index = ord(char) - ord("a")

            if not tree.children[index]:
                return False
            
            tree = tree.children[index]
        
        return tree.end
        

    def startsWith(self, prefix: str) -> bool:

        tree = self

        for char in prefix:
            index = ord(char) - ord("a")

            if not tree.children[index]:
                return False
            
            tree = tree.children[index]
        
        return True
        
        