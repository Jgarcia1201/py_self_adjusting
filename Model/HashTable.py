class ChainingHashTable:

    # Constructor
    # Space Complexity: O(1)
    # Time Complexity: O(N)
    def __init__(self, size):
        self.table = []
        for i in range(size):
            self.table.append([])

    def _get_bucket_list(self, key):
        bucket = hash(key) % len(self.table)
        current_list = self.table[bucket]
        return current_list

    def insert(self, key, item):
        bucket_list = self._get_bucket_list(key)
        bucket_list.append([key, item])

    def delete(self, key):
        bucket_list = self._get_bucket_list(key)
        for pair in bucket_list:
            if pair[0] == key:
                bucket_list.remove(pair)
                return True
        return False

    def search(self, key):
        search_list = self._get_bucket_list(key)
        for pair in search_list:
            if pair[0] == key:
                return pair[1]
        return None

    def update(self, key, item):
        bucket_list = self._get_bucket_list(key)
        for pair in bucket_list:
            if pair[0] == key:
                pair[1] = item
                return True
        return False

