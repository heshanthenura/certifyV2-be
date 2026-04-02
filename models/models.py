from fastapi import UploadFile
from pydantic import BaseModel


class AddTemplateRequestModel(BaseModel):
	font_size: str
	font_color: str
	name_x_pos: int
	name_y_pos: int
