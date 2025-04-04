# Copyright (C) 2017 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - https://cuckoosandbox.org/.
# See the file 'docs/LICENSE' for copying permission.

def str_as_db(s):
    r1 = []
    for ch in s:
        if isinstance(ch, int):
            # In Python 3, iterating over bytes gives integers
            if ch == ord("'") or ch == ord('"'):
                r1.append(ch)
            elif ch < 0x20 or ch >= 0x7f:
                r1.append(ch)
            else:
                r1.append(chr(ch))
        else:
            # For backwards compatibility with Python 2
            if ch in ("'", '"'):
                r1.append(ord(ch))
            elif ord(ch) < 0x20 or ord(ch) >= 0x7f:
                r1.append(ord(ch))
            else:
                r1.append(ch)

    r2, idx = [], 0
    while idx < len(r1):
        if isinstance(r1[idx], int):
            r2.append("%s" % r1[idx])
            idx += 1
            continue
        jdx = idx
        while idx < len(r1) and isinstance(r1[idx], str):
            idx += 1
        r2.append("'%s'" % "".join(r1[jdx:idx]))

    return ",".join("%s" % x for x in r2)
