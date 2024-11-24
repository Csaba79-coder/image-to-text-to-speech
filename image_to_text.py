from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import os


def generate_caption_and_save(image_path, output_dir):
    """
    Kép alapján szöveges leírás generálása és annak mentése egy fájlba.

    Args:
        image_path (str): A bemeneti kép fájlútvonala.
        output_dir (str): A mappa, ahová a generált szöveget menteni kell.

    Returns:
        tuple: (str, str) A mentett fájl teljes elérési útvonala és a generált szöveg.
    """
    # Modell és processzor betöltése a tokennel
    print("Betöltöm a modellt...")

    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

    # Kép betöltése
    print(f"Kép betöltése: {image_path}")
    image = Image.open(image_path)  # Kép megnyitása
    inputs = processor(image, return_tensors="pt")  # Kép előfeldolgozása a modell számára

    # Szöveg generálása a modell alapján
    print("Szöveg generálása...")
    caption_ids = model.generate(**inputs, max_new_tokens=50)  # Generált tokenek, maximum token 50
    caption = processor.decode(caption_ids[0], skip_special_tokens=True)  # Tokenek visszaalakítása szöveggé

    # Output mappa létrehozása, ha nem létezik
    os.makedirs(output_dir, exist_ok=True)

    # A fájlnév előállítása a kép alapján (pl. image.jpg -> image.txt)
    file_name = os.path.splitext(os.path.basename(image_path))[0] + ".txt"
    output_path = os.path.join(output_dir, file_name)  # Kimeneti fájl teljes útvonala

    # Szöveg mentése fájlba
    print(f"Szöveg mentése ide: {output_path}")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(caption)  # A generált szöveg kiírása

    print("A generálás sikerült!")
    return output_path, caption  # Visszaadjuk a fájl elérési útját és a generált szöveget
