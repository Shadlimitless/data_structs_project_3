Im using the trieNode class to create a data structure that can hold each of the characters in a word , marking each node if the previous nodes until the char is hit make a word or not.

The function has a complexity of insertion and search is O(n) as I have to traverse the whole trie to figure out if the new word exists or not.
The suffix function has a complexity of O(n2) since a prefix can have more than two words with the same characters, example , fuN, fuNction, FuNnel, with these three words we need to check all the words that have the N included in them.

The space complexity is O(n) since we're creating a new array to return found suffixes