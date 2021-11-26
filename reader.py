"""Module for reading an imaging an discerning words and characters."""

from pytesseract import image_to_string


def readImage(image="Screenshot_1", languageRead="eng") -> None:
    """Method for reading images and discerning text

    Tesseract will attempt to read the image as characters in the input
    language, then text is provided in the chosen output language.

    Arguments:
        image (String): Name of the image file to be read.
            Defaults to 'Screenshot_1'.
    Returns:
        A string consisting of the contents read by Pytesseract.
    """

    try:
        text = image_to_string(image, lang=languageRead)
        print(text, sep="\n***\n")
        return text
    except FileNotFoundError:
        print("Didn't work")
        return "Didn't work"
