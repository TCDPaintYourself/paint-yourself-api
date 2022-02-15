from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi_cloudauth.firebase import FirebaseClaims

from paint_yourself_api.middlewares import verify_authentication
from paint_yourself_api.schemas import StyledImageThemeEnum
from paint_yourself_api.services import ImageStylerService

router = APIRouter()


@router.post("")
def create_styled_image(
    *,
    _: FirebaseClaims = Depends(verify_authentication),
    image_styler_service: ImageStylerService = Depends(ImageStylerService),
    image: UploadFile = File(..., description="Image to be styled."),
    theme: StyledImageThemeEnum,
):
    """Endpoint used to apply the theme to user submitted images."""

    themed_image = image_styler_service.create_themed_image(image.file, theme)

    return StreamingResponse(themed_image, media_type=image.content_type)
