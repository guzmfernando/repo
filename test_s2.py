import unittest
from unittest.mock import patch
from s2 import translate_to_english

class TestTranslateToEnglish(unittest.TestCase):

    @patch('builtins.input', side_effect=["Hola, ¿cómo estás?", "salir"])
    def test_translation_valid_input(self, mock_input):
        translated = translate_to_english()
        self.assertEqual(translated, "Hello, how are you?")

    @patch('builtins.input', side_effect=["", "salir"])
    def test_empty_input(self, mock_input):
        translated = translate_to_english()
        self.assertEqual(translated, "Invalid input. Please enter a Spanish sentence.")

    @patch('builtins.input', side_effect=["Texto inexistente", "salir"])
    def test_translation_failure(self, mock_input):
        translated = translate_to_english()
        self.assertEqual(translated, "Translation failed. Please check your input.")

    @patch('builtins.input', side_effect=["Bonjour", "salir"])
    def test_translation_other_languages(self, mock_input):
        translated = translate_to_english()
        self.assertEqual(translated, "Hello")

if __name__ == '__main__':
    unittest.main()
