
class LRUCache (object):
    
    def __init__(self) -> None:
        self.cache_size = 3
        self.items = {}
        self.first = None
        self.last = None

    def get(self, key):
        item = self.items.get(key)
        if item != None:
            previous = item['previous']
            next = item['next']
            if previous != None:
                self.items[previous]['next'] = next
            if next != None:
                self.items[next]['previous'] = previous

            self.items[key]['previous'] = None
            if self.first != key:
                self.items[key]['next'] = self.first
                self.items[self.first]['previous'] = key
            self.first = key
            if previous != None and self.items[previous]['next'] == None:
                self.last = previous
        return item


    def put(self, key, value):
        item = self.items.get(key)
        previous = None
        if  item != None:
            previous = item['previous']
            next = item['next']
            if previous != None:
                self.items[previous]['next'] = next
            if next != None:
                self.items[next]['previous'] = previous
        elif len(self.items) == self.cache_size:
            previous = self.items[self.last]['previous']
            self.items[previous]['next'] = None
            del self.items[self.last]

        self.items[key] = {'value': value, 'previous': None, 'next': self.first}
        if self.first != None:
            self.items[self.first]['previous'] = key

        self.first = key
        if self.last == None:
            self.last = key

        if previous != None and self.items[previous]['next'] == None:
            self.last = previous

    def prt(self):
        if self.first != None:
            stack = [self.first]
            next = self.items[self.first]['next']
            while next != None:
                stack.append(next)
                next = self.items[next]['next']
            print(stack)
        print(self.items)

lru = LRUCache()

lru.get('a') # None

lru.put('a', 1)
lru.put('b', 2)
lru.put('c', 3)

lru.prt() # c, b, a

lru.put('a', 3)

lru.prt() # a, c, b

lru.get('x')

lru.prt() # a, c, b

lru.get('b')

lru.prt() # b, a, c

lru.put('d', 4)

lru.prt() # d, b, a

