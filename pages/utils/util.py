import os
import sys
from PIL import Image
from io import StringIO
def remove_existing_file(func):
    def wrapper(*args, **kwargs):
        old_stdin = sys.stdin
        sys.stdin = StringIO("y")
        stream = os.popen('cd ~ && pwd')
        root_dir = stream.read()
        sample_dir = root_dir.strip()
        # remove /home/codespace/OpenBBUserData/exports/bbands.png already
        # get last arg as export
        export = args[-1]
        temp_image = os.path.join(sample_dir, "OpenBBUserData", "exports", export)
        # if exists erase
        if os.path.exists(temp_image):
            os.remove(temp_image)
        func(*args, **kwargs)
        sys.stdin = old_stdin
        if os.path.exists(temp_image):
            return temp_image
        return None
    return wrapper