import unittest

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

class TestHashMap(unittest.TestCase):
    def setUp(self):
        self.hm = HashMap()

    def test_put_and_get_existing_key(self):
        self.hm.put('key1', 10)
        self.hm.put('key2', 20)
        self.assertEqual(self.hm.get('key1'), 10)
        self.assertEqual(self.hm.get('key2'), 20)

    def test_update_existing_key(self):
        self.hm.put('key1', 10)
        self.hm.put('key1', 100)
        self.assertEqual(self.hm.get('key1'), 100)

    def test_get_nonexistent_key(self):
        self.assertIsNone(self.hm.get('nonexistent_key'))

if __name__ == '__main__':
    unittest.main()
