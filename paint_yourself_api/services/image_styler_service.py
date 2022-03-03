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
        self, input_image: typing.BinaryIO, reference_image: typing.BinaryIO
    ) -> typing.BinaryIO:
        """Applies the reference image style to the image."""

        with input_image as image_file:
            with reference_image as reference_image_file:
                image_bytes = image_file.read()
                reference_image_bytes = reference_image_file.read()

                stylized = self.styler.paint_image(image_bytes, reference_image_bytes)

                _, im_buf_arr = cv.imencode(".jpg", stylized)
                byte_im = im_buf_arr.tobytes()

                return io.BytesIO(byte_im)

    def create_themed_image(
        self, input_image: typing.BinaryIO, theme: StyledImageThemeEnum
    ) -> typing.BinaryIO:
        """Applies a theme to the image."""

        theme_image_path = f"./paint_yourself_api/themes/{theme.value}.jpg"

        with input_image as input_image_file:
            with open(theme_image_path, "rb") as theme_image_file:
                image_bytes = input_image_file.read()
                theme_bytes = theme_image_file.read()
                stylized = self.styler.paint_image(image_bytes, theme_bytes)

                _, im_buf_arr = cv.imencode(".jpg", stylized)
                byte_im = im_buf_arr.tobytes()

                return io.BytesIO(byte_im)


def get_image_styler_service(
    styler: StyleTransfer = Depends(get_style_transfer),
) -> ImageStylerService:
    return ImageStylerService(styler)
