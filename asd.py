# Automated skin cancer detector (ASD) API
# MIT LICENSE

__version__ = '0.1.0'
__author__ = 'Yasin Bakhtiar, Radin Reisi'

# Import tensorflow module to load deep learning model
from tensorflow import keras, expand_dims

# Import pillow module to work with images
from PIL import Image


class SkinCancerDetector:
    """Automated Skin Cancer Detector
    """
    def __init__(self):
        self.loaded_model = keras.models.load_model("./src/models/ASD.h5")

    @classmethod
    def __check_img(cls, src) -> bool:
        """Find corrupted images

        Usage:
        src = "./address/file.png"
        print(self.__check_img(src))

        Arg:
            src: image address

        Returns:
            True: it is an image
            False: it isn't an image
        """
        try:
            img = Image.open(src)

            # It checks that is it an image or not
            img.verify()
            return True

        # If the python can't open it, the file is corrupted.
        except:
            return False

    def detect(self, src) -> str:
        """Detect skin cancer with deep learning model

        Usage:

        from asd import SkinCancerDetector
        src = "./address/file.png"
        print(SkinCancerDetector().detector(src))

        Arg:
            src: string --> image address

        Return:
            Predictions of API

        Raises:
            "Error: Unsupported file"
        """
        if SkinCancerDetector.__check_img(src):
            img = keras.preprocessing.image.load_img(src, target_size=(180, 180))
            img_array = keras.preprocessing.image.img_to_array(img)
            img_array = expand_dims(img_array, 0)  # Create batch axis
            predictions = self.loaded_model.predict(img_array)
            return str(predictions)
        else:
            return "Error: Unsupported file"
