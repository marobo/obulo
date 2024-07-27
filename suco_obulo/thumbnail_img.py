from io import BytesIO
from django.core.files import File
from PIL import Image


def make_thumbnail(image, size=(500, 500)):
    """Makes thumbnails of given size from given image"""

    img = Image.open(image)
    exif = img.info.get('exif')
    if exif is not None:
        """
        RGB is a very common color mode for digital images.
        It uses 3 channels to represent color Red-Green-Blue.
        It also works with image file types such as jpg and bpm.

        RGBA on the other hand is a color mode that can represent
        “transparency” through its Alpha channel.
        This type of image can only be saved as PNG or
        GIF image file formats which support transparency.
        """
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")  # convert mode
        img.thumbnail(size)  # resize image
        thumb_io = BytesIO()  # create a BytesIO object
        img.save(thumb_io, 'JPEG', quality=85, exif=exif)  # save image to BytesIO object
    else:
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")  # convert mode
        img.thumbnail(size)  # resize image
        thumb_io = BytesIO()  # create a BytesIO object
        img.save(thumb_io, 'JPEG', quality=85)  # save image to BytesIO object
    thumbnail = File(thumb_io, name=image.name)  # create a django friendly File object
    return thumbnail
