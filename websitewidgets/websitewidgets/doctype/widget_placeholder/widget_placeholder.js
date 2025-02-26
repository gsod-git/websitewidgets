// Copyright (c) 2018, valiantsystem and contributors
// For license information, please see license.txt

frappe.ui.form.on("Widget Placeholder", "refresh", function(frm) { 
	frm.set_query("link_data", "widget_config", function(doc, cdt, cdn) {
		return {
			filters: {
				'has_web_view': 1,
			}
		};
	});
  frm.set_query("category", function(frm) {
    return{
     filters: {
      'has_web_view': 1
     }
    }
 });
});

