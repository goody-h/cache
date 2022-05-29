

class LRUCache (object):
    
    def __init__(self) -> None:
        self.cache_size = 5
        self.items = {}
        self.head = None
        self.tail = None
        pass

    def get(self, key):
        pass

    def put(self, key, value):
        if self.items.get(key) != None:
            head = self.items.get(key)['head']
            tail = self.items.get(key)['tail']

            if head != None:
                head['tail'] = tail
            if tail != None:
                tail['head'] = head
        elif len(self.items) == self.cache_size:
            
            pass

        self.items[key] = {'value': value, 'head': None, 'tail': self.head}
        if self.head != None:
            self.head['head'] = key

        self.head = key

        if self.tail == None:
            self.tail = key
            
        pass

