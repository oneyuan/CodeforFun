class TrieNode:

    def __init__(self):
        self.links = [None for _ in range(26)]
        self.isend = False

    def containsKey(self, ch):
        return self.links[ord(ch)-ord('a')] != None

    def get(self, ch):
        return self.links[ord(ch)-ord('a')]

    def put(self, ch, node):
        self.links[ord(ch)-ord('a')] = node

    def setEnd(self):
        self.isend = True

    def isEnd(self):
        return self.isend


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for i in range(len(word)):
            cur = word[i]
            if not node.containsKey(cur):
                node.put(cur, TrieNode())
            node = node.get(cur)
        node.setEnd()

    def searchPrefix(self, word):
        node = self.root
        for i in range(len(word)):
            cur = word[i]
            if node.containsKey(cur):
                node = node.get(cur)
            else:
                return None
        return node

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.searchPrefix(word)
        return node != None and node.isEnd()

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.searchPrefix(prefix)
        return node != None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


class Trie0:

    def __init__(self): 
        self.__root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.__root
        for x in word:
            if x not in current:
                current[x] = {}
            current = current[x]
        # Using True instead of {}, the time cut down 40 ms
        current['end'] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.__root
        for x in word:
            if x not in current:
                return False
            current = current[x]
        return 'end' in current

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.__root
        for x in prefix:
            if x not in current:
                return False
            current = current[x]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
