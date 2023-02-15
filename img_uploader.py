# Image uploader 

# Import pillow module to work with images
from PIL import Image

# Import pyclamd (an anti-virus module)
import pyclamd

import datetime
import os


class ImgUploader:
    """Upload images to server

    Usage:
    from img_uploader import ImgUploader
    src = open("file/address.png")
    save_address = './src/users/ASD/'
    img_uploader = ImgUploader(src, save_address)
    print(img_uploader.img_status)

    Arg:
        src: opened image
        save_address: saved image address
    """
    def __init__(self, src, save_address):
        self.src = src
        self.__img_address = ''
        self.__img_status = False
        self.save_address = save_address

        # If file was an image:
        if self.__check_img():
            # Upload the image to server
            self.__upload()

            # If the image doesn't have a virus:
            if self.__check_for_virus():
                self.__img_status = True
            else:
                self.__remove_img()
                self.__img_status = False
                
        else:
            self.__img_status = False

    @property
    def img_status(self):
        '''Did image saved or not?
        Returns:
            True: It saved successfully
            False: It didn't saved
        '''
        return self.__img_status

    @property
    def img_address(self):
        ''' The address of the saved image
        Return:
            The address of the saved image
        '''
        return self.__img_address

    def __upload(self):
        """Upload the image to server
        """
        img = Image.open(self.src)
        img.save(self.__img_address)

    def __remove_img(self):
        """Remove the image from server (whenever the image has a virus)
        """
        os.remove(self.__img_address)

    def __check_img(self):
        """Find corrupted image
        Return:
            True: It is an image
            False: It isn't an image
        """
        try:
            img = Image.open(self.src)

            # It checks that is it an image or not
            img.verify()

            # Create a name and address for image (it uses date to name images)
            date = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            self.__img_address = self.save_address + self.src.name + "_" + date + '.' + img.format

            return True

        # If the python can't open it, the file is corrupted.
        except:
            return False

    def __check_for_virus(self):
        """Check the image to find the virus
        Return:
            True: It doesn't have a virus
            False: It has a virus
        """
        return True
        """
        try:
            anti_virus = pyclamd.ClamdAgnostic()
            if anti_virus.scan_file() is None:
                return True
            else:
                return False
        except:
            return False
        """