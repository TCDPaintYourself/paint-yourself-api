import io
import typing

import cv2 as cv
import numpy as np

from paint_yourself_api.schemas import StyledImageThemeEnum
from paint_yourself_api.services.vgg_style_transfer import StyleTransfer


class ImageStylerService:
    """Service used to style user submitted images."""

    def __init__(self):
        self.styler = StyleTransfer()

    def create_styled_image(
        self, image: typing.BinaryIO, reference_image: typing.BinaryIO
    ) -> typing.BinaryIO:
        """Applies the reference image style to the image."""

        with image as f:
            with reference_image as r_f:
                f_bytes = f.read()
                r_f_bytes = r_f.read()

                input_image = cv.imdecode(np.frombuffer(f_bytes, dtype=np.uint8), 1)
                theme_image = cv.imdecode(np.frombuffer(r_f_bytes, dtype=np.uint8), 1)

                input_path = "./paint_yourself_api/input/input.png"
                theme_path = "./paint_yourself_api/input/theme.png"

                cv.imwrite(input_path, input_image)
                cv.imwrite(theme_path, theme_image)

                stylized = self.styler.paint_image(input_path, theme_path)

                is_success, im_buf_arr = cv.imencode(".jpg", stylized)
                byte_im = im_buf_arr.tobytes()

                return io.BytesIO(byte_im)

    def create_themed_image(
        self, image: typing.BinaryIO, theme: StyledImageThemeEnum
    ) -> typing.BinaryIO:
        """Applies a theme to the image."""

        with image as f:
            reference_image = None

            f_bytes = f.read()

            input_image = cv.imdecode(np.frombuffer(f_bytes, dtype=np.uint8), 1)

            if theme == StyledImageThemeEnum.van_gogh:
                reference_image = cv.imread(f"./paint_yourself_api/themes/vangogh.jpg")
            if theme == StyledImageThemeEnum.caravaggio:
                reference_image = cv.imread(
                    f"./paint_yourself_api/themes/caravaggio.jpg"
                )
            elif theme == StyledImageThemeEnum.claude_monet:
                reference_image = cv.imread(
                    f"./paint_yourself_api/themes/claudemonet.jpg"
                )
            elif theme == StyledImageThemeEnum.da_vinci:
                reference_image = cv.imread(f"./paint_yourself_api/themes/davinci.jpg")
            elif theme == StyledImageThemeEnum.picasso:
                reference_image = cv.imread(f"./paint_yourself_api/themes/picasso.jpg")
            elif theme == StyledImageThemeEnum.rembrandt:
                reference_image = cv.imread(
                    f"./paint_yourself_api/themes/rembrandt.jpg"
                )
            elif theme == StyledImageThemeEnum.whistler:
                reference_image = cv.imread(f"./paint_yourself_api/themes/whistler.jpg")

            theme_image = reference_image
            input_path = "./paint_yourself_api/input/input.png"
            theme_path = "./paint_yourself_api/input/theme.png"

            cv.imwrite(input_path, input_image)
            cv.imwrite(theme_path, theme_image)

            stylized = self.styler.paint_image(input_path, theme_path)

            is_success, im_buf_arr = cv.imencode(".jpg", stylized)
            byte_im = im_buf_arr.tobytes()

            return io.BytesIO(byte_im)
