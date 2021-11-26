"""Module for housing language values and methods

    Note that Google Translate utilizes IETF language codes (ISO-639-1), and
    Pytesseract uses its own unique set.
"""


from google.cloud import translate_v2 as GoogleTranslate

# ************************************************* #
# Pytesseract Language Codes

ENGLISH = "eng"

JAPANESE = "jpn"
JAPANESE_VERT = "jpn_vert"

KOREAN = "kor"

CHINESE = "chi_sim"
CHINESE_VERT = "chi_sim_vert"


# ************************************************* #
# IETF Language Codes

TRANSLATE_JAPANESE = "ja"
TRANSLATE_CHINESE = "zh-CN"
TRANSLATE_KOREAN = "ko"
TRANSLATE_ENGLISH = "en"


class Linguist:
    """A class to handle languages.

    Attributes:
        _languageRead (String): Pytesseract code for the language it will read.
        _translateFrom (String): IETF code for the language that Google
            Translate will translate from.
        _translateTo (String): IETF code for the language that Google
            Translate will translate into.
    """

    def __init__(self) -> None:
        """Constructor for a Linguist.

        The defaults for the languages is English. The languages are to be
        selected on construction.
        """

        self._languageRead = "eng"
        self._translateFrom = "en"
        self._translateTo = "en"
        self._translator = GoogleTranslate.Client()

        self.chooseLanguageRead()  # replace with GUI
        self.chooseLanguageOutput()  # replace with GUI

    def chooseLanguageRead(self) -> None:
        """Method to choose/change the input language.

        This method will modify both _languageRead and _translateFrom.
        """

        while(1):
            lang = input("Language to be read?: j/jv/k/c/cv/en ")
            if(lang == "j"):
                self._languageRead = JAPANESE
                self._translateFrom = TRANSLATE_JAPANESE
                return
            elif(lang == "jv"):
                self._languageRead = JAPANESE_VERT
                self._translateFrom = TRANSLATE_JAPANESE
                return
            elif(lang == "k"):
                self._languageRead = KOREAN
                self._translateFrom = TRANSLATE_KOREAN
                return
            elif(lang == "c"):
                self._languageRead = CHINESE
                self._translateFrom = TRANSLATE_CHINESE
                return
            elif(lang == "cv"):
                self._languageRead = CHINESE_VERT
                self._translateFrom = TRANSLATE_CHINESE
                return
            elif(lang == "en"):
                self._languageRead = ENGLISH
                self._translateFrom = TRANSLATE_ENGLISH
                return
            else:
                return

    def chooseLanguageOutput(self) -> None:
        """Method to select the output language for Google Translate."""

        while(1):
            lang = input("Language to be written?: j/k/c/en ")
            if(lang == "j"):
                self._translateTo = TRANSLATE_JAPANESE
                return
            elif(lang == "k"):
                self._translateTo = TRANSLATE_KOREAN
                return
            elif(lang == "c"):
                self._translateTo = TRANSLATE_CHINESE
                return
            elif(lang == "en"):
                self._translateTo = TRANSLATE_ENGLISH
                return
            else:
                pass

    def getLanguageRead(self) -> str:
        """Method to get Pytesseracts input language."""

        return self._languageRead

    def getTranslateFrom(self) -> str:
        """Method to get Google Translate's first language."""

        return self._translateFrom

    def getTranslateTo(self) -> str:
        """Nethod to get Google Translate's second language."""

        return self._translateTo

    def translate(self, text) -> None:
        """Method for translating text

        The languages are chosen through the linguist. Will not translate
        if both language input and output are the same.

        Arguments:
            text (String): Text to be translated.
        """
        if(self._translateFrom == self._translateTo):
            return
        translation = self._translator.translate(
                values=text,
                source_language=self._translateFrom,
                target_language=self._translateTo)
        print(translation, end="\n***\n")
        return
