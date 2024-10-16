from datetime import datetime


class TimedValue:
    def __init__(self, default, expiration=60):
        self.default = default
        self.expiration = expiration
        self.updated = datetime(1970, 1, 1, 0, 0, 0)  # Never
        self.value = default

    # Returns (value, expired)
    def get_with_expired(self):
        now = datetime.now()
        diff = now - self.updated
        interval = diff.total_seconds()
        if interval < self.expiration:
            return (self.value, False)
        else:
            return (self.default, True)

    def get(self):
        (value, expired) = self.get_with_expired()
        return value

    def set(self, value):
        now = datetime.now()
        self.value = value
        self.updated = now

    def clear(self):
        self.updated = datetime(1970, 1, 1, 0, 0, 0)  # Never
