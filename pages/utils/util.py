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
        # check for .openbb_terminal/env in root_dir
        if os.path.exists(os.path.join(root_dir.strip(), ".openbb_terminal", "env")) == False:
            print("Did not find .openbb_terminal/env")
            # create it
            os.mkdir(os.path.join(root_dir.strip(), ".openbb_terminal"))
            # make .env file
            env_file = open(os.path.join(root_dir.strip(), ".openbb_terminal", "env"), "w")
            
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