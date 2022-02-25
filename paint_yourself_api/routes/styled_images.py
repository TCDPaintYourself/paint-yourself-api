from typing import Optional

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
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
    input_image: UploadFile = File(..., description="Image to be styled."),
    reference_image: Optional[UploadFile] = None,
    theme: Optional[StyledImageThemeEnum] = None,
):
    """Endpoint used to apply the style or theme to user submitted images."""

    if reference_image is None and theme is None:
        raise HTTPException(400, detail="Theme is missing")

    output_image = None

    if theme:
        output_image = image_styler_service.create_themed_image(input_image.file, theme)
    else:
        output_image = image_styler_service.create_styled_image(
            input_image.file, reference_image.file
        )

    return StreamingResponse(output_image, media_type=input_image.content_type)
