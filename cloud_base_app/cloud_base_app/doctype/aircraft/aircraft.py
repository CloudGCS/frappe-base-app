# Copyright (c) 2024, CloudGCS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Aircraft(Document):
    def autoname(self):
        # Fetch the Tenant Code
        tenant_code = frappe.db.get_single_value('Tenant Settings','tenant_code')
    
        # Ensure both tenant_code and tail_no are available
        if tenant_code and self.tail_no:
            # Set the name of the aircraft
            self.name = f'{tenant_code}-{self.type}-{self.tail_no}'
        else:
            # Handle cases where the tenant code or tail no is not available
            frappe.throw('Tenant Code or Tail No is missing!')

    # def before_insert(self):
    #   doc = frappe.get_doc("Box Settings")
    #   print(doc.box_type)
    #   print(doc.box_type)
    #   print(self.tail_no)

    # def before_save(self):
    #   box_type = frappe.get_value("Box Settings", "Box Settings", "box_type")
    #   print(box_type)
    #   box_type = frappe.get_conf().get("box_type")
    #   print(box_type)
    #   print(self.tail_no)

    # def download_certificate(self, *args,**kwargs):
    #   # This fonction will be executed when the Execute Action Button will be clicked
    #   print('Hello World')
    #   # The data is transmitted via keyword argument
    #   print(args)
    #   print(kwargs)
