"""Run the application with 'texty' as the module.
    !/usr/projects/Texty
"""

import texty.app as app
from os import environ, getenv

if __name__ == "__main__":
    """Run main"""

    CREDENTIALS = "GOOGLE_APPLICATION_CREDENTIALS"
    if(getenv(CREDENTIALS) is None):
        try:
            envPath = open("assets/meta.txt")
            environ[CREDENTIALS] = envPath.readline().strip()
            print("Getting credentials...")
            envPath.close()
        except FileNotFoundError:
            print("The file 'meta.txt' could not be found.")
            quit()
    app.main()
