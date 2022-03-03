import io
import typing

import cv2 as cv
import numpy as np
from fastapi import Depends

from paint_yourself_api.schemas import StyledImageThemeEnum
from paint_yourself_api.services.vgg_style_transfer import (
    StyleTransfer,
    get_style_transfer,
)


class ImageStylerService:
    """Service used to style user submitted images."""

    def __init__(self, styler: StyleTransfer):
        self.styler = styler

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
            f_bytes = f.read()

            input_image = cv.imdecode(np.frombuffer(f_bytes, dtype=np.uint8), 1)

            reference_image = cv.imread(
                f"./paint_yourself_api/themes/{StyledImageThemeEnum[theme].value}.jpg"
            )

            theme_image = reference_image
            input_path = "./paint_yourself_api/input/input.png"
            theme_path = "./paint_yourself_api/input/theme.png"

            cv.imwrite(input_path, input_image)
            cv.imwrite(theme_path, theme_image)

            stylized = self.styler.paint_image(input_path, theme_path)

            is_success, im_buf_arr = cv.imencode(".jpg", stylized)
            byte_im = im_buf_arr.tobytes()

            return io.BytesIO(byte_im)


def get_image_styler_service(
    styler: StyleTransfer = Depends(get_style_transfer),
) -> ImageStylerService:
    return ImageStylerService(styler)
