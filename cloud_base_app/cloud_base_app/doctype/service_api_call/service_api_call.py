# Copyright (c) 2024, CloudGCS and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ServiceAPICall(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		endpoint: DF.Data | None
		host_url: DF.Data
		method: DF.Literal["get", "put", "post", "delete", "patch"]
		module: DF.Link
		request_payload: DF.JSON | None
		response_payload: DF.Text | None
		response_status: DF.Data | None
		service: DF.Data
	# end: auto-generated types
	pass
