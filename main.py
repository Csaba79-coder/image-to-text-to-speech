import os

from image_to_text import generate_caption_and_save
from text_to_speech import text_to_speech_gtts, play_audio
from tranlation import translate_to_hungarian, only_translate_to_hungarian


def main():
    # Bemeneti és kimeneti mappák megadása
    input_dir = "input"
    output_dir = "output"

    # Képek fájl elérési útja
    image_paths = [
        os.path.join(input_dir, "couple.jpg"), # araffe coule ... a rough helyett
        os.path.join(input_dir, "xmas.jpg") # helyes output az input alapján, bár örültem volna, ha a karácsonyfát is felismeri még! de nem ... :)
    ]

    for image_path in image_paths:
        # 1. Képhez generált szöveg mentése
        output_txt_path, caption = generate_caption_and_save(image_path, output_dir)
        print(f"Generált szöveg angolul a képről {image_path}: {caption}")

        # 2. Fordítás meghívása
        translated_text = translate_to_hungarian(caption, image_path, output_dir)
        print(f"Fordított magyar szöveg: {translated_text}")

        # 3. A generált szöveget hangfájlra alakítjuk
        # Itt a txt fájl neve alapján generáljuk a hangfájl nevét
        txt_filename = os.path.basename(output_txt_path)  # A txt fájl neve
        audio_paths = text_to_speech_gtts(caption, translated_text, output_dir, txt_filename)
        print(f"Hangfájl mentve: {audio_paths}")

        # audio_paths most egy tuple, ami tartalmazza mindkét fájl elérési útvonalát
        english_output_path = audio_paths[0]  # Az angol fájl elérési útvonala
        hungarian_output_path = audio_paths[1]  # A magyar fájl elérési útvonal

        # Hangfájlok lejátszása
        print(f"Angol verzió lejátszása a képről {image_path}: Blah blah blah ...")
        play_audio(english_output_path)

        print(f"Magyar verzió lejátszása a képről {image_path}: blablabla ...")
        play_audio(hungarian_output_path)

    print("---------------------------------------------------")
    # couple.jpg helyes input szöveg:
    correct_input_text =  "A rough couple kissing in front of the Eiffel Tower in Paris"
    print("Hallás utáni szöveg angolul: " + correct_input_text)
    # annak fordítása:
    correct_translated_text = only_translate_to_hungarian(correct_input_text)
    print("A vélt korrekt input magyar fordítása: " + correct_translated_text)


if __name__ == "__main__":
    main()
