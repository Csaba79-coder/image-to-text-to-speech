from transformers import MarianMTModel, MarianTokenizer
import os


def translate_to_hungarian(text, input_image_path, output_dir):
    """
        Ez a függvény angol nyelvű szöveget fordít magyarra a helyi MarianMT modell segítségével.

        Args:
            text (str): Az angol nyelvű bemeneti szöveg, amit le kell fordítani.
            input_image_path (str): Az input képfájl elérési útja, amelyből a szöveg származik.
            output_dir (str): A kimeneti mappa, ahová a lefordított szöveget tartalmazó fájlt mentjük.

        Returns:
            str: A lefordított magyar nyelvű szöveg.
    """
    # Helyi modell betöltése
    model = MarianMTModel.from_pretrained("./local_models/opus-mt-en-hu")
    tokenizer = MarianTokenizer.from_pretrained("./local_models/opus-mt-en-hu")

    # Szöveg tokenizálása és fordítás
    tokenized_text = tokenizer(text, return_tensors="pt", padding=True)  # Tokenizálás
    translated = model.generate(**tokenized_text)  # Fordítás

    # A lefordított szöveg visszaalakítása
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

    __save_to_file(input_image_path, translated_text, output_dir)

    return translated_text


# A couple kép probléma miatt egy override segítségével a fordítást ellenőrizzük, ha az input helyes!
def only_translate_to_hungarian(text):
    """
    Ez a függvény angol nyelvű szöveget fordít magyarra a helyi MarianMT modell segítségével.

    Args:
        text (str): Az angol nyelvű bemeneti szöveg, amit le kell fordítani.

    Returns:
        str: A lefordított magyar nyelvű szöveg.
    """
    # Helyi modell betöltése
    model = MarianMTModel.from_pretrained("./local_models/opus-mt-en-hu")
    tokenizer = MarianTokenizer.from_pretrained("./local_models/opus-mt-en-hu")

    # Szöveg tokenizálása és fordítás
    tokenized_text = tokenizer(text, return_tensors="pt", padding=True)  # Tokenizálás
    translated = model.generate(**tokenized_text)  # Fordítás

    # A lefordított szöveg visszaalakítása
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

    return translated_text


def __save_to_file(input_image_path, translated_text, output_dir):
    """
        A lefordított szöveget menti egy fájlba a megadott kimeneti mappába.

        Args:
            input_image_path (str): Az input képfájl elérési útja, amely alapján a fájl nevét generáljuk.
            translated_text (str): A lefordított szöveg, amelyet menteni kell.
            output_dir (str): A mappa, ahová a fájlokat mentjük.

        Returns:
            None
    """
    # A képfájl neve alapján generáljuk az output fájl nevét
    file_name = os.path.splitext(os.path.basename(input_image_path))[0] + "_hu.txt"
    output_file_path = os.path.join(output_dir, file_name)

    # A lefordított szöveg mentése a fájlba
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(translated_text)

    print(f"Fordított fájl elmentve: {output_file_path}")
