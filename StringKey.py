class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        hashValue = self.calculate_hash_value(string)
        if(self.table[hashValue] == None):
            self.table[hashValue] = []
        self.table[hashValue].append(string)
        #print self.table[hashValue]
        pass

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hashValue = self.calculate_hash_value(string)
        if((self.table[hashValue] != None) and (string in self.table[hashValue])):
            return hashValue
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        firstLetter = ord(string[0])
        secondLetter = ord(string[1])
        hashValue = firstLetter*100 + secondLetter
        return hashValue
		
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')
