
from requests import put


class LRUCache (object):

    def __init__(self, capacity) -> None:
        self.cache_size = capacity
        self.items = {}
        self.first = None
        self.last = None

    def get(self, key):
        try:
            value = self.items[key]['value']
        except:
            value = -1

        if value != None and value != -1:
            self.put(key, value)
        return value

    def put(self, key, value):
        item = self.items.get(key)
        previous = None
        next = None
        former_last_previous = None
        if  item != None:
            previous = item['previous']
            next = item['next']
        former_first = self.first
        former_last = self.last

        if former_last != None:
            former_last_previous = self.items[former_last]['previous']

        data = {'value': value, 'previous': None, 'next': None}
        self.items[key] = data

        if key != former_first:
            data['next'] = former_first
        else:
            data['next'] = next

        if previous != None:
            self.items[previous]['next'] = next
        else:
            previous = key

        if next != None:
            self.items[next]['previous'] = previous
        if former_first != None and former_first != key:
            self.items[former_first]['previous'] = key

        self.first = key

        if len(self.items) > self.cache_size:
            if former_last_previous != None:
                self.items[former_last_previous]['next'] = None
            elif self.items[former_last]['previous'] == key:
                data['next'] = None
            del self.items[former_last]

        if next == None:
            if former_last_previous != None and self.items[former_last_previous]['next'] == None:
                self.last = former_last_previous
            elif self.items[previous]['next'] == None:
                self.last = previous

    def prt(self):
        if self.first != None:
            stack = [self.first]
            next = self.items[self.first]['next']
            while next != None:
                stack.append(next)
                next = self.items[next]['next']
            print(stack)
        print(self.first)
        print(self.last)
        print(self.items)



lru = LRUCache(3)

["put","put","put","put","get","get","get","get","put","get","get","get","get","get"]
arr = [[1,1],[2,2],[3,3],[4,4],[4],[3],[2],[1],[5,5],[1],[2],[3],[4],[5]]

l = 2
for a in arr:
    if len(a) == 1:
        lru.get(a[0])
    else: lru.put(a[0], a[1])
    print('### Next')
    print(l)
    l += 1







# lru.get('a') # None

# lru.put('a', 1)
# lru.prt() # c, b, a
# lru.put('a', 1)
# lru.prt() # c, b, a

# lru.get('a') # None
# lru.get('a') # None
# lru.put('b', 1)
# lru.prt() # c, b, a
# lru.put('b', 2)
# lru.prt() # c, b, a
# lru.put('c', 3)

# lru.prt() # c, b, a

# lru.put('a', 3)

# lru.prt() # a, c, b

# lru.get('x')

# lru.prt() # a, c, b

# lru.get('b')

# lru.prt() # b, a, c

# lru.put('d', 4)

# lru.prt() # d, b, a

