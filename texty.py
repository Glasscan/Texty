"""Module for a 'Texty' client."""

import linguist as Lang
import reader as Reader
import os.path
from time import sleep


class Texty:
    """Texty intro

   *** Texty explanation***

    Attributes:
        _Linguist (Linguist): An instance of a class for handling languages.
    """

    def __init__(self):
        """Create an instance of Texty

        A 'Texty' has a Linguist, a Translator, ...
        """

        self._linguist = Lang.Linguist()

    def start(self):
        """Method to start the Texty client

        Currently only takes screenshots as inputs.
        """
        while(1):
            screenshots = []
            directory = os.listdir("assets/images")
            for f in directory:
                if (f[-4:] == ".png"
                        and "Screenshot" in f and f not in screenshots):
                    screenshots.append(f)
            for s in screenshots:
                imagePath = "assets/images/" + s
                if os.path.exists(imagePath):
                    text = Reader.readImage(
                        image=imagePath,
                        languageRead=self._linguist.getLanguageRead())
                    self._linguist.translate(text)
                screenshots.remove(s)
            sleep(1)
