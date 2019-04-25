from ex14 import DoubleLinkedList

class Dictionary(object):
    # Magic function to create new dictionary instance.
    def __init__(self, num_buckets=256):
        """Initializes a Map with the given number of buckets."""
        # Dictionaries have an attribute called "map," which is a DLL.
        self.map = DoubleLinkedList()
        # Create an empty DLL for each bucket. The map is a list of lists.
        # In this case, the map is a list of 256 lists because that's how many
        # buckets we have.
        for i in range(0, num_buckets):
            self.map.push(DoubleLinkedList())

    # A function that takes a key and returns an index for the map's buckets.
    def hash_key(self, key):
        """Given a key this will create a number and then convert it to an index
        for the AMap's buckets."""
        # Returns the output of a modulo operation on the hash value of the key
        # and the total numbers of items in the map.
        return hash(key) % self.map.count()

    def get_bucket(self, key):
        """Given a key, find the bucket where it would go."""
        # Get an index for the map's buckets based on the key input to the function.
        bucket_id = self.hash_key(key)
        return self.map.get(bucket_id)

    def get_slot(self, key, default=None):
        """
        Returns either the bucket and node for a slot, or None, None
        """
        bucket = self.get_bucket(key)

        if bucket:
            node = bucket.begin
            i = 0

            while node:
                if key == node.value[0]:
                    return bucket, node
                else:
                    node = node.next
                    i +=1

        # fall through for both if and while above
        return bucket, None

    def get(self, key, default=None):
        """Gets the value in a bucket for a given key, or the default."""
        bucket, node = self.get_slot(key, default=default)
        return node and node.value[1] or node

    def set(self, key, value):
        """Sets the key to the value, replacing any existing value."""
        bucket, slot = self.get_slot(key)

        if slot:
            # the key exists, replace it
            slot.value = (key, value)
        else:
            # the key does not, append to create it
            bucket.push((key, value))

    def delete(self, key):
        """Deletes the given key from the Map."""
        bucket = self.get_bucket(key)
        node = bucket.begin

        while node:
            k, v = node.value
            if key == k:
                bucket.detach_node(node)
                break

    def list(self):
        """Prints out what's in the Map."""
        bucket_node = self.map.begin
        while bucket_node:
            slot_node = bucket_node.value.begin
            while slot_node:
                print(slot_node.value)
                slot_node = slot_node.next
            bucket_node = bucket_node.next
