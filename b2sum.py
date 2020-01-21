#!/usr/bin/env python

import sys
if sys.version_info[0] < 3:
    raise Exception("Python 3 please")

from hashlib import blake2b, blake2s
if sys.argv[1:]:
    for arg in sys.argv[1:]:
        blake = blake2b(digest_size=20)
        try:
            _file = open(arg, 'rb').read()
        except FileNotFoundError as e:
            print(e)
            continue
        blake.update(_file)
        print(str(blake.hexdigest()) + ' ' + arg)

