class Collection:
    def __init__(self):
        self._data = list()

    class Iterator:
        def __init__(self, col):
            self._col = col
            self._index = 0

        def __next__(self):
            if self._index == len(self._col):
                raise StopIteration
            self._index += 1
            return self._col[self._index - 1]

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __iter__(self):
        return self.Iterator(self._data)
    
    def __delitem__(self, index):
        del self._data[index]

    def remove(self, value):
        i = 0
        while i < len(self._data):
            if self._data[i] == value:
                del self._data[i]
            else:
                i = i+1

    def index(self, value):
        i = 0
        for i in range(0, len(self._data)):
            if self._data[i] == value:
                return i

    def __str__(self):
        return str(self._data)
    
    def append (self, value):
        self._data.append(value)

    def __len__(self):
        return len(self._data)

def sort(list, comp_func, order):
    '''
        comp_func = the comparison function, applied on a and b, let's say, which returns:
                    > -1 if a < b
                    > 0 if a = b
                    > 1 if a > b
    '''
    gap = len(list)//2
    while gap > 0:
        for i in range(gap, len(list)):
            elem = list[i]
            j = i
            while j >= gap and comp_func(list[j - gap], elem) == order:
                list[j] = list[j-gap]
                j = j - gap
            list[j] = elem
        gap = gap // 2
    return list

def filter(list, accept_function, *args):
    '''
    accept_func = the acceptance function, applied on a, which returns:
                    > 0 if a does not pass the filter
                    > 1 otherwise.
    '''
    new_list = Collection()
    for elem in list:
        if accept_function(elem, *args) == 1:
            new_list.append(elem)
    return new_list


