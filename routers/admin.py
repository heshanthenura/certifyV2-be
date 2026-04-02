from typing import Annotated
from fastapi import APIRouter, File, Form, UploadFile
from models.models import AddTemplateRequestModel
from services.database import add_template
from services.storage import upload_template

router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)


@router.post("/add/template")
async def admin_add_template(
    template: Annotated[UploadFile, File(...)],
    font_size: Annotated[str, Form(...)],
    font_color: Annotated[str, Form(...)],
    name_x_pos: Annotated[int, Form(...)],
    name_y_pos: Annotated[int, Form(...)],
):
    request_data = AddTemplateRequestModel(
        font_size=font_size,
        font_color=font_color,
        name_x_pos=name_x_pos,
        name_y_pos=name_y_pos,
    )
    upload_result = await upload_template(template)
    db_record = add_template(upload_result["public_url"], request_data)

    return {
        "ok": True,
        "message": "Template added successfully",
        "upload": upload_result,
        "template": db_record,
        "data": request_data.model_dump(),
    }

 