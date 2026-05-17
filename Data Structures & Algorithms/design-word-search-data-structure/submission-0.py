class TrieNode:

    def __init__(self):
        self.children = [None]*26
        self.end = False

class WordDictionary:

    def __init__(self):
        self.tree = TrieNode()
        

    def addWord(self, word: str) -> None:
        
        temp_tree = self.tree

        for char in word:
            index = ord(char) - ord("a")

            if not temp_tree.children[index]:
                temp_tree.children[index] = TrieNode()
            
            temp_tree = temp_tree.children[index]
        
        temp_tree.end = True

    def search(self, word: str) -> bool:

        def recurse(tree, index):

            if not tree:
                return False

            if index == len(word):
                return tree.end

            char = word[index]
            if char == ".":
                res = False
                for i in range(26):
                    if tree.children[i]:
                        res = res or recurse(tree.children[i], index+1)
                return res
            else:
                return recurse(tree.children[ord(char) - ord("a")], index+1)

        return recurse(self.tree, 0)
            

        
