# Copyright (C) 2017 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - https://cuckoosandbox.org/.
# See the file 'docs/LICENSE' for copying permission.

from shellcode import Shellcode
import sys

def usage():
    print '''usage:
        echo -en "\\xcc\\xcc" | egghatch''' 
    sys.exit(-1)

def main():
    # no data on stdin 
    if sys.stdin.isatty():
        usage()
 
    payload = sys.stdin.read()
    hatch = Shellcode(payload)
    
    hatch.analyze()
    
