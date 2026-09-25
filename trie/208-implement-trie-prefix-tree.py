class TrieNode:
    def __init__(self):
        # hashmap will store (children: trie node)
        # marking end
        self.children = {}
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # store in hashmap with the key is the first
        # checking is that character in the children map or not
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        # marking end of the inserting
        curr.is_end = True

    def search(self, word: str) -> bool:
        # checking is it in the hashmap or not -> if not -> return False
        # if is_end = True -> return True - else false
        # so return is_end
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        # flow is as same as the search, but return True if done looping
        # through the word
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
