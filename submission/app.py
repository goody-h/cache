import collections

class LRUCache (object):
    
    def __init__(self) -> None:
        self.cache_size = 3
        self.stack = collections.deque([])
        self.items = {}

    def get(self, key):
        value = self.items.get(key)
        if self.items.get(key) != None:
            self.stack.remove(key)
            self.stack.appendleft(key)
        return value

    def put(self, key, value):
        if self.items.get(key) != None:
            self.stack.remove(key)
        elif len(self.items) == self.cache_size:
            tail = self.stack.pop()
            del self.items[tail]
        self.stack.appendleft(key)
        self.items[key] = value

    def prt(self):
        print(self.stack)
        print(self.items)


lru = LRUCache()

lru.get('a') # None

lru.put('a', 1)
lru.put('b', 2)
lru.put('c', 3)

# lru.prt() # c, b, a

lru.put('a', 3)

# lru.prt() # a, c, b

lru.get('x')

# lru.prt() # a, c, b

lru.get('b')

# lru.prt() # b, a, c

lru.put('d', 4)

lru.prt() # d, b, a

