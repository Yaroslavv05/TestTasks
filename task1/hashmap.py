class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.map = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        if not self.map[index]:
            self.map[index] = []
        for pair in self.map[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.map[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        if self.map[index]:
            for pair in self.map[index]:
                if pair[0] == key:
                    return pair[1]
        return None

