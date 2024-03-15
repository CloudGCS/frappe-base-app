// Copyright (c) 2024, CloudGCS and contributors
// For license information, please see license.txt

frappe.ui.form.on("Aircraft", {
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
