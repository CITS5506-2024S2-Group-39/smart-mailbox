from datetime import datetime, timezone


class ISODateTime(datetime):
    def __new__(
        cls, year=1970, month=1, day=1, hour=0, minute=0, second=0, microsecond=0
    ):
        return super().__new__(
            cls,
            year,
            month,
            day,
            hour,
            minute,
            second,
            microsecond,
            tzinfo=timezone.utc,
        )

    def __str__(self):
        return self.isoformat()

    @staticmethod
    def now():
        current_time = datetime.now(timezone.utc)
        return ISODateTime(
            current_time.year,
            current_time.month,
            current_time.day,
            current_time.hour,
            current_time.minute,
            current_time.second,
            current_time.microsecond,
        )

    @classmethod
    def from_string(cls, iso_string):
        # Parse the ISO string back into a datetime object
        dt = datetime.fromisoformat(iso_string)
        # Convert it to an ISODateTime instance
        return cls(
            dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond
        )

    def to_string(self):
        return self.isoformat()
