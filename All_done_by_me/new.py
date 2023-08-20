from google.cloud import translate_v2 as translate

def translate_text(text, target_language):
    translate_client = translate.Client()

    result = translate_client.translate(
        text,
        target_language=target_language
    )

    return result['translatedText']

def main():
    print("Language Translator")
    print("-------------------")
    text = input("Enter the text to translate: ")
    target_language = input("Enter the target language (e.g., 'es' for Spanish, 'fr' for French): ")

    translated_text = translate_text(text, target_language)
    print(f"Translated text: {translated_text}")

if __name__ == "__main__":
    main()
