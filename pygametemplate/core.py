"""Module containing the core functions of pygametemplate."""
import os
import sys
import traceback as traceback
from datetime import datetime
import ctypes as ctypes

from pygametemplate.exceptions import CaughtFatalException


PATH = os.getcwd()


def path_to(*path):
    """Returns the complete absolute path of the path given."""
    return os.path.join(PATH, *"/".join(path).split("/"))


LOG_FILE = path_to("log.txt")

def log(*error_message, fatal=True):
    """Takes 1 or more variables and concatenates them to create the error message."""
    error_message = "".join(map(str, error_message))
    with open(LOG_FILE, "a") as log_file:
        log_file.write("{} - {}.\n".format(datetime.utcnow(), error_message))
        log_file.write(traceback.format_exc() + "\n")

    if fatal:
        text = ("An error has occurred:\n\n    {}.\n\n\n"
                "Please check log.txt for details.").format(error_message)
        ctypes.windll.user32.MessageBoxA(0, text, "Error", 0)   # Error popup
        raise CaughtFatalException(sys.exc_info()[1])
    else:
        pass    # TODO: Add some code here to show an error message in game
