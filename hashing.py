class HashTable:
    '''
    Two lists are created that implement the Map abstract data type
    - One is called slots, which will hold the key items
    - The other is called data, which whill hold the data values
    When we look up a key, the corresponding position in the data list will hold the associated data value
    We will treat the key list as a hash table
    It is important the size be prime number so that the collision resolutuion algorithm can be as efficient as possible 
    '''

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))
        # Assumes that there will eventually be an empty slot unless the key is already present in the self.slots
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                # Computes the original hash value and if that slot is not empty, iterates the rehash function until an empty slot occurs
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and \
                        self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))
                # If a nonempty slot already contains the key, the old data value is replaced with the new data value
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace

    def hashfunction(self, key, size):
        # implements the simple remainder method
        return key % size

    def rehash(self, oldhash, size):
        # collision resolution technique is linear probing with a 'plus 1'
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        # computes the intitial hash value
        while self.slots[position] != None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                # if the value is not in the initial slot, rehash is used to locate the next possible position
                position = self.rehash(position, len(self.slots))
                # guarentee that the search will terminate by checking to make sure that we have not returned to the initial slot
                if position == startslot:
                    stop = True  # exhausted all possible slots and the item must not be present
        return data

    # methods that provide additional dictionary functionality. Overload the __getitem__ and __setitem__ methods to allow access using '[]'. This means once a HashTable has been created, the familiar index operator will be available.
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
H.slots
[77, 44, 55, 20, 26, 93, 17, None, None, 31, 54]
H.data
['bird', 'goat', 'pig', 'chicken', 'dog', 'lion',
       'tiger', None, None, 'cow', 'cat']

print(H[17])
