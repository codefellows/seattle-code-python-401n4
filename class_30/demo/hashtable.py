class Hashtable:
    pass

    def __init__(self, size=10024):
        self.size = size
        self.bucket = size *[None]

        # Initializer

    def add(self, key, value):
        pass

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

        'Cat'

        'aCt'
        sum = 0

        for ch in key:
            # convert to ascii Cat
            # if first char, multiply by 11
            # if third char multiuply by 7
             sum += ord(ch)
             # C - 67
             # a - 97
             # t - 116

             # sum 280
        primed = sum * 97
        # 27160
        index = primed % self.size

        # 27160 - primed
        # 536

        return index


        # hash
        # Arguments: key
        # Returns: Index in the collection for that key

    def keys():
        pass

        # keys
        # Returns: Collection of keys
