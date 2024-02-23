import frappe

# will run after app is installed on site
def after_install():
    # box_type read from site config
    box_type = frappe.get_conf().get("box_type")
    # insert Box Settings with box_type
    doc = frappe.new_doc("Box Settings")
    doc.box_type = box_type
    doc.insert()

    tenant_code = frappe.get_conf().get("tenant_code")
    tenant_name = frappe.get_conf().get("tenant_name")
    tenant = frappe.new_doc("Tenant Settings")
    tenant.tenant_code = tenant_code
    tenant.tenant_name = tenant_name
    tenant.insert()
    frappe.db.commit()
    pass

