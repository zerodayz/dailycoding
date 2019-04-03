# Hashing table


class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000

    def store(self, string):
        hash_value = self.calculate_hash_value(string)
        if self.table[hash_value]:
            self.table[hash_value].append(string)
        else:
            self.table[hash_value] = [string]
        pass

    def lookup(self, string):
        hash_value = self.calculate_hash_value(string)
        if self.table[hash_value]:
            if string in self.table[hash_value]:
                return hash_value
            else:
                return -1
        else:
            return -1

    def calculate_hash_value(self, string):
        return (ord(string[0]) * 100) + ord(string[1])


# Setup
hash_table = HashTable()

# Should return 8269
print(hash_table.calculate_hash_value('REDHAT'))
# Should return -1 as the value doesn't exist
print(hash_table.lookup('REDHAT'))

# Insert REDHAT into hashing table
hash_table.store('REDHAT')

# This will return -1 as it doesn't exist in the hash table
print(hash_table.lookup('REAL'))

# Insert REAL into hashing table
hash_table.store('REAL')
print(hash_table.lookup('REAL'))
