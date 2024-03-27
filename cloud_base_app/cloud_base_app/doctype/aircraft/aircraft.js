// Copyright (c) 2024, CloudGCS and contributors
// For license information, please see license.txt

frappe.ui.form.on("Aircraft", {
	refresh: function(frm) {
		if (frappe.user.has_role('System Manager')) {
			frm.add_custom_button('Update Certificate', () => {
					frappe.call({
						method: "cloud_base_app.cloud_base_app.services.certificate_service.create_aircraft_certificate",
						args: {
							doc: frm.doc,
						},
						freeze: true,
						callback: function (r) {
							frappe.msgprint("Certificate created successfully");
							frm.reload_doc();
						},
						error: (r) => {
							frappe.msgprint("Something went wrong, please try again later\n" + r.message);
						}
					});
				
			})
		}
	},
	after_save: function(frm) {
		frm.reload_doc();
	},
	// This function is triggered when the form is loaded
	onload(frm) {
		
		// Setting the query for the Table MultiSelect field
		frm.set_query('ps_plugins', function() {
				// Return an object with the filters
				return { 
						filters: {
								'extension_type': ['=', 'PS']
						}
				};
		});

		frm.set_query('mc_plugins', function() {
				// Return an object with the filters
				return {
						filters: {
								'extension_type': ['=', 'MC']
						}
				};
		});
	},
});
