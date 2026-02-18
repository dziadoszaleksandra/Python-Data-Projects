import time
from pathlib import Path


class FileLock:
    def __init__(self, filepath, timeout=10):
        self.filepath = Path(filepath)
        self.lock_path = Path(str(self.filepath) + ".lock")
        self.timeout = timeout
        self.lock_acquired = False

    def __enter__(self):
        start_time = time.time()

        while self.lock_path.exists():
            if time.time() - start_time > self.timeout:
                raise TimeoutError(
                    f"Nie można uzyskać blokady pliku {self.filepath} - timeout"
                )
            time.sleep(1)

        self.lock_path.touch()
        self.lock_acquired = True
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.lock_acquired and self.lock_path.exists():
            self.lock_path.unlink()
