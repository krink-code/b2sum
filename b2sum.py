#!/usr/bin/env python

import sys
if sys.version_info[0] < 3:
    raise Exception("Python 3 please")

from hashlib import blake2b, blake2s

import threading
threads = []

def b2sum(_file):
    is_64bits = sys.maxsize > 2**32
    if is_64bits:
        blake = blake2b(digest_size=20)
    else:
        blake = blake2s(digest_size=20)
    try:
        with open(_file, 'rb') as bfile:
            _f = bfile.read()
    except FileNotFoundError as e:
        return print(str(e))

    blake.update(_f)
    return print(str(blake.hexdigest()) + ' ' + _file)

if sys.argv[1:]:
    for arg in sys.argv[1:]:
        t = threading.Thread(target=b2sum, args=(arg,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

