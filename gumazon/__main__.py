#!/usr/bin/env python

import sys

from gumazon import Application

print(Application((sys.argv[1] if len(sys.argv) > 1 else '')))
print(Application()((sys.argv[1] if len(sys.argv) > 1 else '')))
