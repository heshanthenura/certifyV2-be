from models.models import AddCertificateRequestModel, AddTemplateRequestModel
from services.supabase_client import get_supabase_client
from utils.certificate_id import generate_certificate_id


def add_template(url: str, request: AddTemplateRequestModel) -> dict:
	client = get_supabase_client()

	payload = {
		"url": url,
		"font_size": float(request.font_size),
		"font_color": request.font_color,
		"name_x_pos": request.name_x_pos,
		"name_y_pos": request.name_y_pos,
		"template_name": request.template_name,
		"template_for": request.template_for,
		"event_name": request.event_name,
		"issuer_name": request.issuer_name,
		"notes": request.notes,
	}

	response = client.table("templates").insert(payload).execute()
	if not response.data:
		raise ValueError("Failed to insert template record")

	return response.data[0]


def add_certificate(request: AddCertificateRequestModel) -> dict:
	client = get_supabase_client()
	certificate_id = request.certificate_id or generate_certificate_id()

	payload = {
		"certificate_id": certificate_id,
		"template_id": request.template_id,
		"recipient_name": request.recipient_name,
		"recipient_email": request.recipient_email,
		"issue_reason": request.issue_reason,
		"event_name": request.event_name,
		"event_date": request.event_date,
		"event_location": request.event_location,
		"issuer_name": request.issuer_name,
		"course_name": request.course_name,
		"notes": request.notes,
	}

	response = client.table("certificates").insert(payload).execute()
	if not response.data:
		raise ValueError("Failed to insert certificate record")

	return response.data[0]
