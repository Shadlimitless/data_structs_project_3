## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        return self
        
#     Helper function to help visualize the trieNode when printing in debug mode
    def __repr__(self):
        return (str(self.__dict__))
    
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        result = []       

#       Inner function that is recursive collecting all the suffixes
        def suffix_recursion(current_node, suffix):
            print('suffix\n', suffix)
#             Base condition 
            if not self.children:
                return []
#         Getting all letters in a node since there could be multiple of them
            current_letters = current_node.keys()
            print('all letters\n', list(current_letters))
            result_suffix = []
            for char in list(current_letters):            
                next_node = current_node[char]
#                 print('current_letter\n', char)
#                 print('***next node***\n', next_node) 
                if next_node.is_word == False:
                    result_suffix = suffix_recursion(next_node.children, suffix=suffix + char)
                elif next_node.is_word == True:  
                    suffix = suffix + char
                    result.append(suffix)                  
                    if next_node.children:
                        suffix_recursion(next_node.children, suffix)
                    return result.extend(result_suffix)
                    
        suffix_recursion(self.children, suffix)
        return result 

        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()
        
    def __repr__(self):
        return(str(self.root.__dict__))

    def insert(self, word):
        ## Add a word to the Trie        
        current_node = self.root
        for char in word:
#             print(char, current_node)
            if char not in current_node.children:
                current_node = current_node.insert(char)
#                 print('**current node inserted**\n',current_node)
            current_node = current_node.children[char]
        current_node.is_word = True
#         print(self)

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node =  self.root
        if prefix[0] not in current_node.children or not self.root.children:
            return 'did not find the prefix nodes'
        for char in prefix:
#             print(current_node)
            if char in current_node.children:
                current_node = current_node.children[char]
        return current_node
        

    
#  Test data
tree2 = Trie()
words = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in words:
    tree2.insert(word)
prefix = tree2.find('f')
print('####################################')
print('prefix\n',prefix)
print(prefix.suffixes())
        