class IndexOutOfBounds(Exception):
    def __init__(self, message = 'Index out of bounds!'):
        self.message = message
        super().__init__(self.message)

class NotFound(Exception):
    def __init__(self, message = 'Value not found in list'):
        self.message = message
        super().__init__(self.message)

class Empty(Exception):
    def __init__(self, message = 'The list is empty!'):
        self.message = message
        super().__init__(self.message)

class NotOrdered(Exception):
    def __init__(self, message = 'The list is not ordered'):
        self.message = message
        super().__init__(self.message)

class ArrayList:
    def __init__(self):
        self.cap = 4
        self.arr = [0] * self.cap
        self.size = 0
        self.ordered = True

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        if self.size != 0:
            return_string = str(self.arr[0])
            for i in range(1, self.size):
                return_string += ', ' + str(self.arr[i])
            return return_string
        return ''

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        self.needs_resize()
        for i in range(self.size-1, -1, -1):
            self.arr[i+1] = self.arr[i]
        self.arr[0] = value
        self.size += 1
        self.ordered = False

    def needs_resize(self):
        if self.size == self.cap:
            self.resize()

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        self.needs_resize()
        if index == 0:
            self.prepend(value)
        elif 0 < index < self.size:
            for i in range(self.size - 1, index-1, -1):
                self.arr[i+1] = self.arr[i]
            self.arr[index] = value
            self.size += 1
        elif index == self.size:
            self.append(value)
        else:
            raise IndexOutOfBounds()
        self.ordered = False

    #Time complexity: O(1) - constant time
    def append(self, value):
        self.needs_resize()
        self.arr[self.size] = value
        self.size += 1
        self.ordered = False

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if 0 <= index < self.size:
            self.arr[index] = value
            self.ordered = False
        else:
            raise IndexOutOfBounds()

    #Time complexity: O(1) - constant time
    def get_first(self):
        if self.size != 0:
            return self.arr[0]
        else:
            raise Empty()

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        if 0 <= index < self.size:
            return self.arr[index]
        else:
            raise IndexOutOfBounds()

    #Time complexity: O(1) - constant time
    def get_last(self):
        if self.size != 0:
            return self.arr[self.size-1]
        else:
            raise Empty()

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        temp = [0] * self.cap * 2
        for i in range(self.size):
            temp[i] = self.arr[i]
        self.cap *= 2
        self.arr = temp

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        if self.size != 0 and 0 <= index < self.size:
            if index == self.size - 1:
                self.arr[self.size-1] = 0
            else:
                for i in range(index, self.size - 1):
                    self.arr[i] = self.arr[i+1]
                self.arr[self.size - 1] = 0
            self.size -= 1
        else:
            raise IndexOutOfBounds()

    #Time complexity: O(1) - constant time
    def clear(self):
        self.arr = [0] * self.cap
        self.size = 0
        self.ordered = True

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        if not self.ordered:
            raise NotOrdered()
        else:
            if self.size == 0:
                self.arr[0] = value
                self.size += 1
            elif self.arr[self.size - 1] <= value:
                self.append(value)
            elif self.arr[0] > value:
                self.prepend(value)
            else:
                for i in range(self.size - 1):
                    if self.arr[i] <= value < self.arr[i+1]:
                        self.insert(value, i+1)
                        break
            self.ordered = True

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        if self.size > 0:
            if self.ordered:
                return self.binary(value)
            else:
                return self.linear(value)

    def binary(self, value):
        """LARGE PROBLEMS WITH THE SEARCH, SOMETIMES
        IT DOESNT FIND VALUES THAT ARE ON THE LIST, 
        SOMETIMES IT FINDS THE VALUE AT WRONG INDEX,
        NOT CONSISTAND WHETER LOWER OR HIGHER INDEX"""
        high = self.size - 1
        low = 0
        while low != high:
            mid = (low + high)//2
            if self.arr[mid] == value:
                return mid
            elif self.arr[mid] > value:
                high = mid - 1
            elif self.arr[mid] < value:
                low = mid + 1
        raise NotFound()

    def linear(self, value):
        for i in range(self.size):
            if self.arr[i] == value:
                return i
        raise NotFound()

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        index = self.linear(value)
        self.remove_at(index)

if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()
    for i in range(4):
        arr_lis.append(i)
    print(arr_lis.arr, arr_lis.size)
    arr_lis.remove_at(3)
    print(arr_lis.arr, arr_lis.size)
