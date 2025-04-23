from enum import Enum


class JobType(str, Enum):
    BATCH = "BATCH"
    STREAMING = "STREAMING"

    def __str__(self) -> str:
        return str(self.value)
