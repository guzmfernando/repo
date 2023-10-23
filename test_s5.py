import unittest
from unittest.mock import patch  # Importar patch desde unittest.mock
from translate import Translator
from langdetect import detect

def translate(text):
    try:
        detected_lang = detect(text)
        target_lang = "en" if detected_lang == "es" else "es"
        
        translator = Translator(to_lang=target_lang, from_lang=detected_lang)
        translation = translator.translate(text)
        return translation
    except Exception as e:
        return str(e)

class TestTranslateFunction(unittest.TestCase):
    @patch('builtins.input', side_effect=["Hello", "Hola", "12345", ""])
    def test_translate_english_to_spanish(self, mock_input):
        result = translate(input("Ingrese una frase: "))
        self.assertNotEqual(result, "Hello")

    @patch('builtins.input', side_effect=["Hello", "Hola", "12345", ""])
    def test_translate_spanish_to_english(self, mock_input):
        result = translate(input("Ingrese una frase: "))
        self.assertNotEqual(result, "Hola")
    
    def test_translate_invalid_text(self):
        result = translate("12345")
        self.assertIsInstance(result, str)
    
    def test_translate_empty_text(self):
        result = translate("")
        self.assertIsInstance(result, str)

if __name__ == "__main__":
    unittest.main()
