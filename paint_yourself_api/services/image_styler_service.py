import io
import typing

from paint_yourself_api.schemas import StyledImageThemeEnum
from paint_yourself_api.vgg_style_transfer import StyleTransfer
import cv2 as cv
import numpy as np

class ImageStylerService:
    """Service used to style user submitted images."""

    def create_styled_image(
        self, image: typing.BinaryIO, reference_image: typing.BinaryIO
) -> typing.BinaryIO:

        """Applies the reference image style to the image."""

        # TODO: Apply style to the image.
        with image as f:
            with reference_image as r_f:
                f_bytes = f.read()
                r_f_bytes = r_f.read()

                input_image = np.array(f_bytes, dtype=np.uint8)
                theme_image = np.array(r_f_bytes, dtype=np.uint8)
                input_path = './paint-yourself-api/paint_yourself_api/input/input.png'
                theme_path = './paint-yourself-api/paint_yourself_api/input/theme.png'
                cv.imwrite(input_image, input_path)
                cv.imwrite(theme_image, theme_path)

                styler = StyleTransfer()
                stylized = styler.paint_image('./samples/Daniel.png', './styles/Cezanne/215466.jpg')

                is_success, im_buf_arr = cv.imencode(".jpg", stylized)
                byte_im = im_buf_arr.tobytes()

                return byte_im

    def create_themed_image(
        self, image: typing.BinaryIO, theme: StyledImageThemeEnum
    ) -> typing.BinaryIO:
        """Applies a theme to the image."""

        # TODO: Apply theme to the image.
        with image as f:







            return io.BytesIO(f.read())
