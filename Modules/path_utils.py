import os
import re
import sys


def normalize_path(raw: str) -> str:
    p = raw.strip().strip('"').strip("'")

    if sys.platform != "win32":
        m = re.match(r'^([A-Za-z]):[\\/](.*)$', p)
        if m:
            drive = m.group(1).lower()
            rest = m.group(2).replace('\\', '/')
            p = f'/mnt/{drive}/{rest}'

    return p
