// Copyright (c) 2025, boq and contributors
// For license information, please see license.txt


frappe.ui.form.on("Bill of Quantities", {
    refresh: function(frm) {
        if (frm.doc.status === "Submitted") {
            frm.add_custom_button(__("Create Quotation"), function() {
                frappe.call({
                    method: "boq.boq.doctype.bill_of_quantities.bill_of_quantities.create_quotation_from_boq",
                    args: { boq_name: frm.doc.name },
                    callback: function(r) {
                        if (!r.exc) {
                            frappe.msgprint(__("Quotation Created: " + r.message));
                            frappe.set_route("Form", "Quotation", r.message);
                        }
                    }
                });
            }, __("Create"));
        }

        if (frm.doc.status === "Quoted") {
            frm.add_custom_button(__("Create Project"), function() {
                frappe.call({
                    method: "boq.boq.doctype.bill_of_quantities.bill_of_quantities.create_project_from_boq",
                    args: { boq_name: frm.doc.name },
                    callback: function(r) {
                        if (!r.exc) {
                            frappe.msgprint(__("Project Created: " + r.message));
                            frappe.set_route("Form", "Project", r.message);
                        }
                    }
                });
            }, __("Create"));
        }
    }
});





