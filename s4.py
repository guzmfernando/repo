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

if __name__ == "__main__":
    while True:
        user_text = input("Ingrese una frase (o escriba 'salir' para terminar): ")

        if user_text.lower() == "salir":
            break

        translated_text = translate(user_text)

        print(f"Texto original: {user_text}")
        print(f"Texto traducido: {translated_text}")
