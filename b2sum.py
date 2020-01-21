#!/usr/bin/env python

import sys
if sys.version_info[0] < 3:
    raise Exception("Python 3 please")

from hashlib import blake2b, blake2s
if sys.argv[1:]:
    is_64bits = sys.maxsize > 2**32
    for arg in sys.argv[1:]:
        if is_64bits:
            blake = blake2b(digest_size=20)
        else:
            blake = blake2s(digest_size=20)
        try:
            with open(arg, 'rb') as bfile:
                _file = bfile.read()
        except FileNotFoundError as e:
            print(e)
            continue
        blake.update(_file)
        print(str(blake.hexdigest()) + ' ' + arg)

