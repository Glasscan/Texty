"""Module for testing 'language.py'.

Run using: pytest -s
"""

from os import environ, getenv
import Texty.linguist as Linguist


def test_setCredentials():
    """Test for settings up Google Cloud permissions."""

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


def test_languageImport():
    """Test for importing the language list from languages.csv."""
    pass


def test_newLinguist(monkeypatch):
    """Test for checking the defaults for a new Linguist."""
    sampleInput = iter(["en", "en"])

    monkeypatch.setattr("builtins.input", lambda English: next(sampleInput))
    myLinguist = Linguist.Linguist()

    assert myLinguist.getLanguageRead() == "eng"
    assert myLinguist.getTranslateFrom() == "en"
    assert myLinguist.getTranslateTo() == "en"
