#!/usr/bin/env python

__version__ = '0.0.1'

import sys
if sys.version_info[0] < 3:
    raise Exception("Python 3 please")

from hashlib import blake2b, blake2s

def usage():
    print(sys.argv[0] + ''' [option]... [file]...
Print or check blake2 checksums.
With no FILE, or when FILE is -, read standard input.

    options:

        --help             display this help
        --version          output version information

The sums are computed using blake2b or blake2s, depending on 
the hardware architecture is_64bits.

Version: {} '''.format(__version__))

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
        return str(e)

    blake.update(_f)
    return str(blake.hexdigest())

def b2checksum(_string):
    is_64bits = sys.maxsize > 2**32
    if is_64bits:
        blake = blake2b(digest_size=20)
    else:
        blake = blake2s(digest_size=20)

    s = _string.encode('utf-8')

    blake.update(s)
    return str(blake.hexdigest())


def main():

    BUFFER_SIZE = 4096
    _stdin = None

    if sys.argv[1:]:

        if sys.argv[1] == '--version':
            print(__version__)
            sys.exit(0)

        elif sys.argv[1] == '--help':
            usage()
            sys.exit(0)

        else:
            #import threading
            #threads = []
            #for arg in sys.argv[1:]:
            #    t = threading.Thread(target=b2sum, args=(arg,))
            #    t.start()
            #    threads.append(t)
            #for t in threads:
            #    t.join()

            for arg in sys.argv[1:]:
                print(b2sum(arg) + '  ' + arg)

    else:
        while True:
            if sys.stdin.isatty():
                mode, _stdin = 'text', sys.stdin.readline(BUFFER_SIZE)
            else:
                mode, _stdin = 'binary', sys.stdin.read(BUFFER_SIZE)

            if not _stdin:
                break
            else:
                break

    if _stdin:
        print(b2checksum(_stdin) + '  -')


if __name__ == '__main__':
    sys.exit(main())


