import datetime
import traceback

from example_game import ExampleGame
from example_view import ExampleView
from pygametemplate import log
from pygametemplate.exceptions import CaughtFatalException

if __name__ == "__main__":
    #! Decide how the window should be when the game opens. (fullscreen/borderless/windowed)?
    # How big should it be? User's monitor dimensions? Something else?
    try:
        game = ExampleGame(ExampleView)
    except Exception:
        with open("log.txt", "a") as error_log:
            error_log.write("%s - UNCAUGHT FATAL EXCEPTION\n" % datetime.datetime.utcnow())
            error_log.write(traceback.format_exc() + "\n")
    else:
        try:
            game.run()
        except CaughtFatalException:
            pass
        except Exception: # Catches all exceptions that weren't caught in the rest of the code
            log("UNCAUGHT FATAL EXCEPTION")
