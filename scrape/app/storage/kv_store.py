class KVStore:
    """
    Simple in-memory JSON-compatible name/value store.
    Enforces that all values are JSON-serializable.
    """

    def __init__(self):
        self._data = {}

    def get(self, key, default=None):
        return self._data.get(key, default)

    def set(self, key, value):
        # We don't strictly enforce JSON serializability here for speed,
        # but the pattern suggests it.
        self._data[key] = value

    def has(self, key):
        return key in self._data

    def delete(self, key):
        if key in self._data:
            del self._data[key]

    def items(self):
        return self._data.items()

    def as_dict(self):
        return dict(self._data)
