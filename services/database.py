from models.models import AddTemplateRequestModel
from services.supabase_client import get_supabase_client


def add_template(url: str, request: AddTemplateRequestModel) -> dict:
	client = get_supabase_client()

	payload = {
		"url": url,
		"font_size": float(request.font_size),
		"font_color": request.font_color,
		"name_x_pos": request.name_x_pos,
		"name_y_pos": request.name_y_pos,
	}

	response = client.table("templates").insert(payload).execute()
	if not response.data:
		raise ValueError("Failed to insert template record")

	return response.data[0]
