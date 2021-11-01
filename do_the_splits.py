#/usr/bin/env python
import sys
import json

ins = sys.stdin.read().strip()
if not ins:
    outs = '[]'
else:
    outs = json.dumps(ins.split("\n"))

print(outs)
