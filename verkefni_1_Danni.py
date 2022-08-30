

# arraylist:
cap = 4
arr = [0,0,0,0]
size = 0
temp = [0] * 8 # use the duplicate functions
arr = [7,5,2,7,1,0,0,0]



#arr[size] = x
# arr[y] = x

arr = [0] * cap

# cant use the for elem in arr:
# can us for i in range:

class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self):
        self.cap = 4
        self.arr = [0]*self.cap
        self.size = 0

        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        # TODO: remove 'pass' and implement functionality
        return_string = ""
        return return_string

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def append(self, value):
        self.arr[self.size] = value
        self.size += 1

        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def get_first(self):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def get_last(self):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def clear(self):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

print('abs')
if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()
    print(str(arr_lis))