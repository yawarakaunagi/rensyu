import numbers
import os


def mkdir():
    os.mkdirs("test", exist_ok=True)

print("テストです。")
for i in range(10):
    print(i+3)
