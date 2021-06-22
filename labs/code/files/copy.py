import sys

src = sys.argv[1]
trg = sys.argv[2]

with open(src, "rb") as f:
    contents = f.read()

with open(trg, "wb") as f:
    f.write(contents)
