// Copyright (c) 2025, boq and contributors
// For license information, please see license.txt

frappe.query_reports["BOQ Flow"] = {
	"filters": [
		{
			"fieldname": "customer",
			"label": __("Customer"),
			"fieldtype": "Link",
			"options": "Customer",
			"reqd": 0
		}
	]
};

