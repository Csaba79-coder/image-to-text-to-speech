from gtts import gTTS
import os
import pygame
import time


def text_to_speech_gtts(text, text_hu, output_dir, txt_filename):
    """
    Szövegek hangfájllá alakítása és mentése MP3 formátumban angol és magyar nyelven,
    majd lejátszásuk egymás után.

    Args:
        text (str): Az angol nyelvű bemeneti szöveg.
        text_hu (str): A magyar nyelvű bemeneti szöveg.
        output_dir (str): A mappa, ahová a fájlokat menteni kell.
        txt_filename (str): A bemeneti szöveges fájl neve (pl. 'couple.txt').

    Returns:
        tuple: Az elkészült hangfájlok teljes elérési útvonalai (angol és magyar).
    """
    # Kimeneti mappa ellenőrzése vagy létrehozása
    os.makedirs(output_dir, exist_ok=True)

    # Angol hangfájl neve és elérési útvonala
    english_filename = os.path.splitext(txt_filename)[0] + ".mp3"
    english_output_path = os.path.join(output_dir, english_filename)

    # Magyar hangfájl neve és elérési útvonala
    hungarian_filename = os.path.splitext(txt_filename)[0] + "_hu.mp3"
    hungarian_output_path = os.path.join(output_dir, hungarian_filename)

    # Angol hang generálása és mentése
    tts_en = gTTS(text, lang="en")  # Angol nyelv
    tts_en.save(english_output_path)  # Hangfájl mentése
    print(f"Angol hangfájl mentve: {english_output_path}")

    # Magyar hang generálása és mentése
    tts_hu = gTTS(text_hu, lang="hu")  # Magyar nyelv
    tts_hu.save(hungarian_output_path)  # Hangfájl mentése
    print(f"Magyar hangfájl mentve: {hungarian_output_path}")

    return english_output_path, hungarian_output_path


def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # Várakozás, amíg be nem fejeződik a lejátszás -> playsound egymás után nem tudott 2 fájlt lejátszani!
        time.sleep(0.1)
