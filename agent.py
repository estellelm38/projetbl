import cv2
import numpy as np
import cv2
import cv2
import easyocr

class Agent:
    
    def get_color(hue_value):

        color_thresholds = {
            "Rouge": ([0, 32], [160, 170]),
            "Jaune": ([23, 38],),
            "Vert": ([40, 124],),
            "Bleue": ([125, 200],),
        }

        for color_name, hue_ranges in color_thresholds.items():
            for hue_range in hue_ranges:
                if hue_value in range(hue_range[0], hue_range[-1] + 1):
                    dominant_color_name = color_name
                    break

        return dominant_color_name

    def __init__(self, grayscale_image_path, color_image_path):
        self.grayscale_image_path = grayscale_image_path
        self.color_image_path = color_image_path

    def identify_color(self):
        color_image = cv2.imread(self.color_image_path)

        # Error handling for image loading
        if color_image is None:
            print("Erreur lors du chargement de l'image.")
            return None

        # Convert color image to HSV
        color_hsv = cv2.cvtColor(color_image, cv2.COLOR_BGR2HSV)

        # Calculate histogram for hue values
        hist = cv2.calcHist([color_hsv], [0], None, [256], [0, 256])

        # Find the dominant color bin
        dominant_bin = np.argmax(hist)
        dominant_hue = int(dominant_bin * 2)  # Convert bin to hue value

        # Define color thresholds for HSV hue values and their respective names
        color_thresholds = {
            "Rouge": ([0, 32], [160, 170]),
            "Jaune": ([23, 38],),
            "Vert": ([40, 124],),
            "Bleue": ([125, 200],),
        }
        print(dominant_hue)
        # Match the dominant hue to a color range
        dominant_color_name = "Undefined"
        for color_name, hue_ranges in color_thresholds.items():
            for hue_range in hue_ranges:
                if dominant_hue in range(hue_range[0], hue_range[-1] + 1):
                    dominant_color_name = color_name
                    break

        return dominant_color_name
    
    def identify_word():

        # Chemin vers l'image
        image_path = '/home/estelle/robotlearn/projetbl/pictures/testmot.jpg'

        # Charger l'image avec OpenCV
        image = cv2.imread(image_path)

        # Convertir l'image en RGB (easyocr exige les images en RGB)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Utiliser EasyOCR pour reconnaître le texte
        reader = easyocr.Reader(['en'])  # Spécifiez les langues que vous voulez reconnaître ici
        result = reader.readtext(image_rgb)

        # Récupérer le texte extrait
        extracted_text = [entry[1] for entry in result]

        # Afficher le texte extrait
        return extracted_text


    print(identify_word())
            


# grayscale_image_path = '/home/estelle/robotlearn/projetbl/pictures/herbe.jpg'
# color_image_path = '/home/estelle/robotlearn/projetbl/pictures/herbe.jpg'

# color_identifier = Agent(grayscale_image_path, color_image_path)
# dominant_color = color_identifier.identify_color()
# print("La couleur dominante dans l'image en couleur est :", dominant_color)

# grayscale_image_path = '/home/estelle/robotlearn/projetbl/pictures/citrouilles.jpg'
# color_image_path = '/home/estelle/robotlearn/projetbl/pictures/citrouilles.jpg'

# color_identifier = Agent(grayscale_image_path, color_image_path)
# dominant_color = color_identifier.identify_color()
# print("La couleur dominante dans l'image en couleur est :", dominant_color)

# grayscale_image_path = '/home/estelle/robotlearn/projetbl/pictures/ocean.jpg'
# color_image_path = '/home/estelle/robotlearn/projetbl/pictures/ocean.jpg'

# color_identifier = Agent(grayscale_image_path, color_image_path)
# dominant_color = color_identifier.identify_color()
# print("La couleur dominante dans l'image en couleur est :", dominant_color)

# grayscale_image_path = '/home/estelle/robotlearn/projetbl/pictures/testmot.jpg'
# color_image_path = '/home/estelle/robotlearn/projetbl/pictures/testmot.jpg'

# color_identifier = Agent(grayscale_image_path, color_image_path)
# dominant_color = color_identifier.identify_color()
# print("La couleur dominante dans l'image en couleur est :", dominant_color)

# grayscale_image_path = '/home/estelle/robotlearn/projetbl/pictures/noir.jpg'
# color_image_path = '/home/estelle/robotlearn/projetbl/pictures/noir.jpg'

# color_identifier = Agent(grayscale_image_path, color_image_path)
# dominant_color = color_identifier.identify_color()
# print("La couleur dominante dans l'image en couleur est :", dominant_color)
