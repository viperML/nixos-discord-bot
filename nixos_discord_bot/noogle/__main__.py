from . import from_str
import sys

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        data = f.read()

    doc = from_str(data)
    print(doc)
