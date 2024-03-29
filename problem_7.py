# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, path):
        # Insert the node as before
        self.children[path] = RouteTrieNode()
        return self

#Helper function to help visualize the trieNode when printing in debug mode
    def __repr__(self):
        return (str(self.__dict__))

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, path_ls, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root

        for path in path_ls:
            if path not in current_node.children:
                current_node = current_node.insert(path)
#                 print('**current node inserted**\n',current_node)
            current_node = current_node.children[path]
        current_node.handler = handler

        # def insert_recursion(current_node, path, handler):
        #     if not current_node.children:
        #         current_node.children[path] = current_node.insert(path, handler)
        #         return current_node
        #     found_handler = current_node.keys()
        #     if len(found_handler) > 1 and found_handler[0] == path:
        #         return found_handler[0]
        #     return insert_recursion(current_node.children, path, handler)
        # return insert_recursion(current_node, path, handler)
            


    def find(self, path_ls):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        for path in path_ls:
            # print(current_node)
            # print('current path',path)
            if path in current_node.children:
                current_node = current_node.children[path]
            else:
                current_node = None
        if current_node:
            return current_node.handler
        return None

       
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler):
        # Create a new RouteTrie for holding our routes\
        self.router = RouteTrie(handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_ls = self.split_path(path)
        # print('path list',path_ls)
        self.router.insert(path_ls, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_ls = self.split_path(path)
        # print('path list',path_ls)
        return self.router.find(path_ls)



    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if len(path) == 0 or len(path) == 1:
            return []    
        return path.split('/')



# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/about/me", "me handler")  # add a route
router.add_handler("/home/about/me/profile", "profile handler")  # add a route



# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
