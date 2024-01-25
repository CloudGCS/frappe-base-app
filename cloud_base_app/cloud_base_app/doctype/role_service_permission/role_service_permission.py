# Copyright (c) 2024, CloudGCS and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RoleServicePermission(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		role: DF.Link | None
		service: DF.Link | None
		service_permission: DF.Link | None
	# end: auto-generated types
	pass
