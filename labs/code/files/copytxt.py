import sys

src = sys.argv[1]
trg = sys.argv[2]

with open(src) as f:
    contents = f.read()

with open(trg, "w") as f:
    f.write(contents)
