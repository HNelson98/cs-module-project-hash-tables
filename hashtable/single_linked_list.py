class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next_node = next

    def get_value(self):
        # returns the node's data 
        return self.value

    def get_next(self):
        # returns the thing pointed at by this node's `next` reference 
        return self.next_node

    def set_next(self, new_next):
        # sets this node's `next` reference to `new_next`
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        # the first Node in the LinkedList
        self.head = None
        # the last Node in the LinkedList
        self.tail = None

    def add_to_tail(self, data):
        # wrap the `data` in a Node instance 
        new_node = Node(data)

        # what about the empty case, when both self.head = None and self.tail = None?
        if not self.head and not self.tail:
            # list is empty 
            # update both head and tail to point to the new node 
            self.head = new_node
            self.tail = new_node
        # non-empty linked list case 
        else:
            # call set_next with the new_node on the current tail node 
            self.tail.set_next(new_node)
            # update self.tail to point to the new last Node in the linked list 
            self.tail = new_node

    def remove_tail(self):
        if self.tail is None:
            return None
        # save the tail Node's data
        data = self.tail.get_value()
        # both head and tail refer to the same Node 
        # there's only one Node in the linked list 
        if self.head is self.tail:
            # set both to be None
            self.head = None
            self.tail = None
        else:
            # in order to update `self.tail` to point to the
            # the Node _before_ the tail, we need to traverse
            # the whole linked list starting from the head,
            # because we cannot move backwards from any one
            # Node, so we have to start from the beginning
            current = self.head

            # traverse until we get to the Node right 
            # before the tail Node 
            while current.get_next() != self.tail:
                current = current.get_next()

            # `current` is now pointing at the Node right
            # before the tail Node
            self.tail = current
            
        
        return data

    def remove_head(self):
        if self.head is None:
            return None
        # save the head Node's data
        data = self.head.get_value()
        # both head and tail refer to the same Node
        # there's only one Node in the linked list 
        if self.head is self.tail:
            # set both to be None 
            self.head = None
            self.tail = None
        else:
            # we have more than one Node in the linked list 
            # delete the head Node 
            # update `self.head` to refer to the Node after the Node we just deleted
            self.head = self.head.get_next()

        return data

    def contains(self, data):
        # an empty linked list can't contain what we're looking for 
        if not self.head:
            return False
            
        # get a reference to the first Node in the linked list 
        # we update what this Node points to as we traverse the linked list 
        current = self.head 

        # traverse the linked list so long as `current` is referring 
        # to a Node 
        while current is not None:
            # check if the Node that `current` is pointing at is holding
            # the data we're looking for 
            if current.get_value() == data:
                return True
            # update our `current` pointer to point to the next Node in the linked list
            current = current.get_next()
        
        # we checked the whole linked list and didn't find the data
        return False

    def get_max(self):
        if self.head is None:
            return None
        
        max_so_far = self.head.get_value()

        current = self.head.get_next()
        
        while current is not None:
            if current.get_value() > max_so_far:
                max_so_far = current.get_value()

            current = current.get_next()
        return current

def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # find index based on key passed in
        # check storage with index from above
        new_entry = HashTableEntry(key, value)
        # check to see if hash index exists
            # Look through hash index list
                # search list for key
                    # if existing key is found, replace it
                # continue looking through list until None
            # if the existing entry is not found, add to the end of hash index list.
            # automatically resize by double if load factor is greater than 0.7
        # If hash index doesn't exist, add new entry in that spot
            # automatically resize by double if load facto is greater than 0.7
    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # find index based on key passed in
        # check storage with index
        # check to see if hash index exists:
            # look through this hash index list
                # search list for key
                    # if it matches the key, set the last entry's next in list to the next index
                    # deletes but moves the following up
                        # if nothing else in list, set the next hash index to current spot
                    # continue looking through list until None
            # key is found, print warning
    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # find index based on key being passed in
        # check storage with above index
        # check to see if that hash index exists
            # look through this hash index list
                # search list for key
                    # if found, return value
                    # continue looking through list until None
            # key is not found, return None
    def resize(self, new_capacity):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Implement this.
        """
        # Step 1: make a new, bigger table/array
        # ....Update capacity on new capacity
        # ....Update storage with new capacity
        # Step 2: go through all the old elements, and hash into the new list
        # Look through each key value pair in previous storage
            # Check previous storage with i as index
            # Check to see if that hash index exists:
                # Look through this hash index list
                        # If found, rehash to new storage
                    # Continue looking through list until None           

 
            