from pathlib import Path

from python1course.zaj05.fibonacci.fibonacci_iterator import FibonacciIterator
from python1course.zaj05.file_lock.file_lock import FileLock
from python1course.zaj05.generatory.days_generator import days_of_week_generator

print("FIBONACCI ITERATOR")
for number in FibonacciIterator(10):
    print(number, end=" ")
print("\n")

print("GENERATOR DNI TYGODNIA")
print("Wszystkie dni:")
for day in days_of_week_generator():
    print(f" - {day}")

print("\nPierwsze 3 dni:")
days_gen = days_of_week_generator()
for _ in range(3):
    print(f" - {next(days_gen)}")

print("\n" + "=" * 50)
print("FILELOCK – PRZYKŁADY")
print("=" * 50)

# 1. Normalne użycie FileLock
print("\n1. Normalne użycie:")
with FileLock("data.txt"):
    with open("data.txt", "a") as f:
        f.write("Dane\n")
    print("   ✓ Plik został zapisany")

# 2. Sprawdzenie pliku lock
print("\n2. Sprawdzenie lock:")
lock_path = Path("data.txt.lock")
with FileLock("data.txt"):
    print(f"   Czy lock istnieje? {lock_path.exists()}")
print(f"   Czy lock usunięty? {not lock_path.exists()}")

# 3. Timeout
print("\n3. Test timeout:")
lock_path.touch()

try:
    with FileLock("data.txt", timeout=2):
        print("   To się nie wyświetli")
except TimeoutError as e:
    print(f"   ✓ Oczekiwany timeout: {e}")

if lock_path.exists():
    lock_path.unlink()

Path("data.txt").unlink(missing_ok=True)
