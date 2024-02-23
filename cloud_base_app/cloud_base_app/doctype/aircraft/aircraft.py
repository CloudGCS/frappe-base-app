# Copyright (c) 2024, CloudGCS and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Aircraft(Document):
	pass

	# def before_insert(self):
	# 	doc = frappe.get_doc("Box Settings")
	# 	print(doc.box_type)
	# 	print(doc.box_type)
	# 	print(self.tail_no)

	# def before_save(self):
	# 	box_type = frappe.get_value("Box Settings", "Box Settings", "box_type")
	# 	print(box_type)
	# 	box_type = frappe.get_conf().get("box_type")
	# 	print(box_type)
	# 	print(self.tail_no)

	# def download_certificate(self, *args,**kwargs):
  #   # This fonction will be executed when the Execute Action Button will be clicked
	# 	print('Hello World')
	# 	# The data is transmitted via keyword argument
	# 	print(args)
	# 	print(kwargs)
  	