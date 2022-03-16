class Hashtable:
    pass

    def __init__(self, size=1024):
        self.size = size
        self.bucket = size *[None]

        # Initializer

    def set(self, key, value):
        #200
        hashed_key = self.hash(key)
        if not self.bucket[hashed_key]:
            self.bucket[hashed_key] = LinkedList()
        # check the key and replace if it exists.    
        current = self.bucket[hashed_key].head
        while current:
            if current.value[0] == key:
                current.vaule[1] == value
            current = current.next
        self.bucket[hashed_key].add([key, value])



        # Add
        # Arguments: key, value
        # Returns: nothing
        # This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
        # Should a given key already exist, replace its value from the value argument given to this method.

    def get(self, key):
        pass

        # get
        # Arguments: key
        # Returns: Value associated with that key in the table

    def contains():
        pass

        # contains
        # Arguments: key
        # Returns: Boolean, indicating if the key exists in the table already.

    def hash(self, key):

        sum = 0
        for ch in key:
             sum += ord(ch)
        primed = sum * 97
        index = primed % self.size
        return index

    def keys():
        pass

        # keys
        # Returns: Collection of keys
