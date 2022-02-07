import io
import typing

from paint_yourself_api.schemas import StyledImageThemeEnum


class ImageStylerService:
    """Service used to style user submitted images."""

    def create_themed_image(
        self, image: typing.BinaryIO, theme: StyledImageThemeEnum
    ) -> typing.BinaryIO:
        """Applies a theme to the image."""

        # TODO: Apply theme to the image.
        with image as f:
            return io.BytesIO(f.read())
