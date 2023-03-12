# Pezeshkeh Khodkar API
# Created by Yasin Bakhtiar and Radin Reisi
# MIT LICENSE

__version__ = '1.0.0'
__author__ = 'Yasin Bakhtiar, Radin Reisi'

# Import the Flask module
from flask import Flask, request, send_file

# Import the AI module 
from asd import SkinCancerDetector

# Import image uploader module
from img_uploader import ImgUploader

# Creating a new "app".
app = Flask(__name__)

asd = SkinCancerDetector("../models/ASD.h5")


# Main page:
@app.route("/")
def show_index():
    return open('../pages/index.html', 'r', encoding="utf-8").read()


@app.route("/api/ASD", methods=['POST', 'Get'])
def detect_skin_cancer():
    """Automated skin cancer API page
    """

    # If the method was POST, it shows results of the API
    if request.method == 'POST':
        img = request.files['img']

        uploaded_img = ImgUploader(img, '../users/ASD/')

        # If the image doesn't upload:
        if uploaded_img.img_status is False:
            return "Error: File upload failed"
        
        else:
            # Return output of the API
            return asd.detect(uploaded_img.img_address)

    # If the method was GET, it shows the error page
    else:
        return open('../pages/error.html', 'r', encoding="utf-8").read()

@app.route("/files", methods=["GET"])
def get_files():
    """The page of sources (fonts, images, ...)
    """
    try:
        # Show src
        return send_file("../pages/src/" + request.args.get('name'))
    
    except:
        # If the file isn't there, it shows an error page
        return open('../pages/error.html', 'r', encoding="utf-8").read()

@app.errorhandler(404)
def not_found_page(e):
    """Error page 404
    """
    return open('.../pages/error.html', 'r', encoding="utf-8").read()


if __name__ == "__main__":
    app.run()
