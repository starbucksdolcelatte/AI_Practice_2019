from io import BytesIO
import requests as req
from PIL import Image

url = "https://cdn.pixabay.com/photo/2017/04/11/15/55/animals-2222007_1280.jpg"

def url_image(url):
    response = req.get(url)
    img = Image.open(BytesIO(response.content))
    return img

def main():
    im = url_image(url)
    im.show()

    size = (600,200)
    im = im.resize(size)
    im.show()

    im.transpose(method=Image.FLIP_LEFT_RIGHT).show()
    im.transpose(method=Image.FLIP_TOP_BOTTOM).show()
    im.transpose(method=Image.ROTATE_90).show()
    im.transpose(method=Image.ROTATE_180).show()
    im.transpose(method=Image.ROTATE_270).show()
    im.transpose(method=Image.TRANSPOSE).show()
    im.transpose(method=Image.TRANSVERSE).show()

    im.rotate(180).show()

main()
